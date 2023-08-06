from __future__ import annotations
from enum import Enum
import json
import time
import openai
import tiktoken
import os


class GPTModel(Enum):
    """
    The OPENAI GPT models available.
    Only those that support functions are listed, so just:
    gpt-3.5-turbo-0613, gpt-3-5-turbo-16k-0613, gpt-4-0613
    """

    GPT_3_5_TURBO = ("gpt-3.5-turbo-0613", 4096, 0.0015, 0.002)
    GPT_3_5_TURBO_16K = ("gpt-3.5-turbo-16k-0613", 16384, 0.003, 0.004)
    GPT_4 = ("gpt-4-0613", 8192, 0.03, 0.06)

    def __init__(self, string, max_tokens, price_1k_tokens_in, price_1k_tokens_out):
        self.string = string
        self.max_tokens = max_tokens
        self.price_1k_tokens_in = price_1k_tokens_in
        self.price_1k_tokens_out = price_1k_tokens_out

    def __str__(self):
        return self.string


class JobTokensExpense:
    """
    Tracks the number of tokens spent on a job and on which GPTModel.
    """

    def __init__(
        self,
        gpt_model: GPTModel,
        prompt_tokens=0,
        completion_tokens=0,
        total_tokens=0,
        rough_estimate=False,
    ):
        self.gpt_model = gpt_model
        self.prompt_tokens = prompt_tokens
        self.completion_tokens = completion_tokens
        self.total_tokens = total_tokens
        self.rough_estimate = rough_estimate

    @staticmethod
    def from_openai_usage_dictionary(
        gpt_model: GPTModel, dictionary: dict
    ) -> JobTokensExpense:
        return JobTokensExpense(
            gpt_model=gpt_model,
            prompt_tokens=dictionary["prompt_tokens"],
            completion_tokens=dictionary["completion_tokens"],
            total_tokens=dictionary["total_tokens"],
        )

    def spend(self, prompt_tokens, completion_tokens, total_tokens):
        self.prompt_tokens += prompt_tokens
        self.completion_tokens += completion_tokens
        self.total_tokens += total_tokens

    def add_from(self, other_expense: JobTokensExpense):
        self.prompt_tokens += other_expense.prompt_tokens
        self.completion_tokens += other_expense.completion_tokens
        self.total_tokens += other_expense.total_tokens
        if other_expense.rough_estimate:
            self.rough_estimate = True  # becomes rough if summed with something rough

    def get_cost(self):
        return (self.prompt_tokens / 1000) * self.gpt_model.price_1k_tokens_in + (
            self.completion_tokens / 1000
        ) * self.gpt_model.price_1k_tokens_out

    def __str__(self):
        string_repr = (
            f"GPT model: {self.gpt_model}\n"
            f"Prompt tokens: {self.prompt_tokens}\n"
            f"Completion tokens: {self.completion_tokens}\n"
            f"Total tokens: {self.total_tokens}\n"
            f"Cost: {round(self.get_cost(),4)}$"
        )

        if self.rough_estimate:
            string_repr += "\n(warning: rough estimate)"

        return string_repr

    def to_json(self):
        return {
            "model": self.gpt_model.string,
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "total_tokens": self.total_tokens,
            "cost": self.get_cost(),
            "rough_estimate": self.rough_estimate,
        }


def estimate_token_count(string: str, model: GPTModel) -> int:
    """Returns the number of tokens in a text string."""

    model_name = model.string
    model_name = model_name.replace("-0613", "")
    model_name = model_name.replace("-16k", "")

    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens



def get_openai_response(
    messages,
    model: GPTModel = GPTModel.GPT_3_5_TURBO,
    debug_stream=False,
    temperature=0.0,
    n=1,
    max_retries=25,
    delay=5,
    openai_api_key=None,
):

    openai_api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
            raise Exception("OPENAI_API_KEY environment variable not set and no key provided in parameters.")
    
    openai.api_key = openai_api_key

    retries = 0
    while retries < max_retries:
        try:
            response = openai.ChatCompletion.create(
                model=model.string,
                temperature=temperature,
                n=n,
                stream=debug_stream,
                messages=messages,
            )

            if debug_stream:
                full_response_text = ""
                for response_delta in response:
                    if len(response_delta["choices"]) > 0:
                        # check content exists
                        message_delta = response_delta["choices"][0]["delta"]

                        if (
                            "content" in message_delta
                            and message_delta["content"] is not None
                        ):
                            delta = response_delta["choices"][0]["delta"]["content"]
                            full_response_text += delta
                            print(
                                delta,
                                end="",
                                flush=True,
                            )

                print("\n\n")
                prompt_tokens = estimate_token_count(json.dumps(messages), model=model)
                completion_tokens = estimate_token_count(
                    full_response_text, model=model
                )
                total_tokens = prompt_tokens + completion_tokens
                rough_expense = JobTokensExpense(
                    gpt_model=model,
                    prompt_tokens=prompt_tokens,
                    completion_tokens=completion_tokens,
                    total_tokens=total_tokens,
                    rough_estimate=True,
                )

                return full_response_text, rough_expense

            else:
                usage = response["usage"]
                expense = JobTokensExpense.from_openai_usage_dictionary(model, usage)
                return response["choices"][0]["message"]["content"], expense

        except openai.OpenAIError as error:
            print(f"OpenAI API error code: {error.code}, message: {error}")

            # check if error contains the string "Rate limit"
            if "rate limit" in str(error).lower():
                print(f"OpenAI API error: {error}. Retrying in 15 seconds...")
                time.sleep(15)
            else:
                print(f"OpenAI API error: {error}. Retrying in {delay} seconds...")
                time.sleep(delay)
            retries += 1

    raise Exception(
        f"Max retries exceeded! OpenAI API call failed {max_retries} times."
    )
