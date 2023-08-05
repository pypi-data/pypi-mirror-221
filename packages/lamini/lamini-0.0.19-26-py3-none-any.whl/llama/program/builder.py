import os
import time
from typing import List, Optional
from llama.program.program import Program
from llama.program.function import Function
from llama.program.util.config import edit_config
from llama.program.util.run_ai import (
    query_run_program,
    fuzzy_is_duplicate,
    query_run_embedding,
)

from llama.types.type import Type

from llama.program.operations.llama_operation import LlamaOperation
from llama.program.operations.batch_llama_operation import BatchLlamaOperation
from llama.program.operations.metric_operation import MetricOperation
from llama.program.operations.call_operation import CallOperation
from llama.program.operations.get_element_operation import GetElementOperation
from llama.program.operations.get_field_operation import GetFieldOperation
from llama.program.operations.return_operation import ReturnOperation
from llama.program.operations.feedback_operation import FeedbackOperation

import inspect

from llama.program.util.api_actions import (
    gen_queue_batch,
    gen_submit_data,
    gen_submit_training_job,
    gen_check_job_status,
    gen_job_results,
    gen_cancel_job,
    gen_multiple_values,
    gen_value,
    gen_clear_data,
    gen_training_job_status,
    gen_all_training_job_status,
    gen_cancel_training_job,
    gen_cancel_training_jobs,
    gen_training_eval,
)
from llama.prompts.prompt import BasePrompt


class Builder:
    """Build a program for execution by the Llama large language model engine."""

    def __init__(
        self,
        id: str,
        model_name: str = None,
        prompt: Optional[BasePrompt] = None,
        config={},
    ):
        self.id = id
        self.program = Program(self, id, prompt)
        self.current_function = self.program.main
        self.value_cache = {}
        self.model_name = model_name
        self.prompt = prompt
        edit_config(config)

    def __call__(self, input, output_type, *args, **kwargs):
        # Reset program
        self.program = Program(self, self.id, self.prompt)
        self.current_function = self.program.main
        if isinstance(input, list):
            values = self.add_model(input, output_type, *args, **kwargs)
            results = gen_multiple_values(values)
            if isinstance(results[0], list):
                return [value for sublist in results for value in sublist]
            return results
        else:
            value = self.add_model(input, output_type, *args, **kwargs)
            result = gen_value(value)
            return result

    def add_model(self, input, output_type, *args, **kwargs):
        if isinstance(input, list):

            def partition(l, n):
                for i in range(0, len(l), n):
                    yield l[i : i + n]

            chunks = list(partition(input, 20))
            if self.model_name is not None:
                kwargs["model_name"] = self.model_name
            operations = []
            for chunk in chunks:
                new_operation = self.current_function.add_operation(
                    BatchLlamaOperation(chunk, output_type, *args, **kwargs)
                )
                operations.append(new_operation)
            return operations
        else:
            if self.model_name is not None:
                kwargs["model_name"] = self.model_name
            new_operation = self.current_function.add_operation(
                LlamaOperation(input, output_type, *args, **kwargs)
            )
            return new_operation

    def submit_job(self, input, output_type, *args, **kwargs):
        if isinstance(input, list):
            values = self.add_model(input, output_type, *args, **kwargs)
            results = gen_queue_batch(values)
            return results
        else:
            new_input = [input]
            values = self.add_model(new_input, output_type, *args, **kwargs)
            results = gen_queue_batch(values)
            return results

    def check_job_status(self, job_id: str):
        status = gen_check_job_status(job_id)
        return status

    def get_job_results(self, job_id: str, output_type=None):
        results = gen_job_results(job_id, output_type)
        return results

    def cancel_job(
        self,
        job_id: str,
    ):
        results = gen_cancel_job(job_id)
        return results

    def train(
        self,
        **kwargs,
    ):
        job = self.submit_training_job(**kwargs)

        environment = os.environ.get("LLAMA_ENVIRONMENT")
        if environment == "LOCAL":
            url = "http://localhost:3000"
        elif environment == "STAGING":
            url = "https://staging.powerml.co"
        else:
            url = "https://app.lamini.ai"
        print(
            f"Training job submitted! Check status of job {job['job_id']} here: {url}/train"
        )

        try:
            status = self.get_training_job_status(job["job_id"])
            if status["status"] == "FAILED":
                print(f"Job failed: {status}")
                return status

            while status["status"] not in ("COMPLETED", "FAILED", "CANCELLED"):
                if kwargs.get("verbose", False):
                    print(f"job not done. waiting... {status}")
                time.sleep(30)
                status = self.get_training_job_status(job["job_id"])
                if status["status"] == "FAILED":
                    print(f"Job failed: {status}")
                    return status
                elif status["status"] == "CANCELLED":
                    print(f"Job canceled: {status}")
                    return status
            print(
                f"Finetuning process completed, model name is: {status['model_name']}"
            )
        except KeyboardInterrupt as e:
            print("Cancelling job")
            return self.cancel_training_job(job["job_id"])
        return status

    def eval(self, job_id: str):
        return gen_training_eval(job_id)

    def submit_training_job(self, **kwargs):
        templates = None
        if self.prompt:
            templates = {
                "prompt": self.prompt.prompt_template,
                "input": self.prompt.input_template,
            }
        results = gen_submit_training_job(
            self.id,
            self.model_name,
            kwargs.get("task", None),
            kwargs.get("enable_peft", False),
            kwargs.get("finetune_args", {}),
            templates,
        )
        job_id = results["job_id"]
        if kwargs.get("verbose", False):
            print(f"job id: {job_id}")
        # wait until data part is done
        results = self.get_training_job_status(job_id)
        return results

    def get_training_job_status(self, job_id):
        status = gen_training_job_status(job_id)
        return status

    def list_all_training_jobs(
        self,
    ):
        results = gen_all_training_job_status()
        return results

    def cancel_training_job(
        self,
        job_id: str,
    ):
        results = gen_cancel_training_job(job_id)
        return results

    def cancel_all_training_jobs(
        self,
    ):
        results = gen_cancel_training_jobs()
        return results

    def sample(
        self,
        input,
        output_type,
        n: int = 1,
        max_similarity: float = 0.99,
        *args,
        **kwargs,
    ):
        input_value = input
        if self.model_name is not None:
            kwargs["model_name"] = self.model_name
        new_operations = []
        cache_len = 5  # NOTE: should use actual cache length
        max_iter = cache_len
        temperature = 0.7  # NOTE: should use actual random temperature
        random = True
        attributes = [
            attribute
            for attribute, field in output_type.__fields__.items()
            if field.type_ == str
        ]
        attribute_embeddings = {attribute: [None, []] for attribute in attributes}
        for i in range(n):
            new_operation = None
            attribute_embeddings = {
                attribute: [None, embeddings[1]]
                for attribute, embeddings in attribute_embeddings.items()
            }
            j = 0
            while any(
                [
                    fuzzy_is_duplicate(
                        attribute_embedding,
                        attribute_reference_embeddings,
                        max_similarity,
                    )
                    for attribute_embedding, attribute_reference_embeddings in attribute_embeddings.values()
                ]
            ) or fuzzy_is_duplicate(
                list(attribute_embeddings.values())[0][0],
                [
                    attribute_embedding
                    for attribute_embedding, _ in list(attribute_embeddings.values())[
                        1:
                    ]
                ],
                max_similarity,
            ):
                if j == max_iter:
                    max_iter += cache_len
                    random = False
                    temperature += 0.1  # NOTE: this could be set differently
                new_operation = self.current_function.add_operation(
                    LlamaOperation(
                        input_value,
                        output_type,
                        random=random,
                        temperature=temperature,
                        *args,
                        **kwargs,
                    )
                )
                new_operation = gen_value(new_operation)
                for attribute in attributes:
                    attribute_embeddings[attribute][0] = query_run_embedding(
                        getattr(new_operation, attribute)
                    )
                j += 1
            if j == max_iter:
                continue
            for (
                attribute_embedding,
                attribute_reference_embeddings,
            ) in attribute_embeddings.values():
                attribute_reference_embeddings.append(attribute_embedding)
            if not new_operation:
                new_operation = self.current_function.add_operation(
                    LlamaOperation(
                        input_value,
                        output_type,
                        random=random,
                        temperature=temperature,
                        *args,
                        **kwargs,
                    )
                )
                new_operation = gen_value(new_operation)
            new_operations.append(new_operation)

        return new_operations

    def set_data(self, data):
        if isinstance(data, list):
            data = data[:100]
        else:
            data = [data]
        self.program.add_data(examples=data)

    def add_data(self, data):
        self.save_data(data)

    def save_data(self, data):
        if not isinstance(data, list):
            data = [data]
        self.program.examples = []
        self.program.add_data(examples=data)
        results = gen_submit_data(self.program, self.id)
        return results

    def clear_data(self):
        return gen_clear_data(self.id)

    def improve(
        self,
        on: str,
        to: str,
        good_examples: List = [],
        bad_examples: List = [],
        temperature: float = 0.0,
        version: str = "",
    ):
        new_operation = self.current_function.add_operation(
            FeedbackOperation(
                on=on,
                to=to,
                good_examples=good_examples,
                bad_examples=bad_examples,
                temperature=temperature,
                version=version,
            )
        )

        return new_operation

    def function(self, function):
        signature = inspect.signature(function)
        input_types = [value.annotation for value in signature.parameters.values()]

        main = self.current_function
        new_function = Function(
            program=self.program, name=function.__name__, input_arguments=input_types
        )
        self.program.functions[new_function.name] = new_function
        self.current_function = new_function
        output_value = function(*new_function.operations)
        self.current_function.add_operation(ReturnOperation(output_value))
        self.current_function = main

        return Lambda(self, new_function, output_value)

    def parallel(self, function):
        return self.function(function=function)

    def add_call(self, function, input_value, output_value):
        new_operation = self.current_function.add_operation(
            CallOperation(function, input_value, output_value)
        )

        result = new_operation

        if isinstance(output_value, tuple):
            result = []

            for index, value in enumerate(output_value):
                result.append(
                    self.current_function.add_operation(
                        GetElementOperation(new_operation, value.type, index)
                    )
                )

        return result

    def get_field(self, value, field_name):
        return self.current_function.add_operation(
            GetFieldOperation(
                value, value._type._get_field_type(field_name), field_name
            )
        )

    def add_metric(self, metric):
        new_operation = self.current_function.add_operation(
            MetricOperation(metric.input, metric.get_metric_type())
        )

        return new_operation

    def make_metric(
        self, input: Type, metric_type: type, fit: bool = True, higher_is_better=True
    ):
        new_operation = self.current_function.add_operation(
            MetricOperation(input, metric_type)
        )

        return new_operation

    def metrics(self):
        requested_values = [
            op._index for op in self.program.functions["main"].operations
        ]

        params = {
            "program": self.program.to_dict(),
            "requested_values": requested_values,
        }
        response = query_run_program(params)
        response.raise_for_status()

        data = [response[str(index)]["data"] for index in requested_values]

        return data


class Lambda:
    def __init__(self, builder: Builder, function: Function, output_value: Type):
        self.output_value = output_value
        self.builder = builder
        self.function = function

    def __call__(self, *args, **kwargs):
        input_value = self._get_input(*args, **kwargs)
        return self.builder.add_call(self.function, input_value, self.output_value)

    def _get_input(self, *args, **kwargs):
        # TODO: support more than one input LLM arg

        if len(args) > 0:
            return args[0]

        return next(iter(kwargs.values()))
