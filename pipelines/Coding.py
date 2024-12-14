import random
from typing import Any, List, Dict, Optional

class BasePipeline:
    """
    Base pipeline for inheritance
    """

    def __init__(self, client: Any, model: str = "gpt-4o", temp_min: float = 0.4, 
                temp_max: float = 0.7, top_p: float = 0.8, token_length: int = 512):
        """
        Initializes the Pipeline with the provided parameters.

        Args:
            client (Any): The client object for interacting with the language model API.
            model (str): The model to use for generating responses (default: "gpt-4o").
            temp_min (float): Minimum temperature for randomness in response (default: 0.4).
            temp_max (float): Maximum temperature for randomness in response (default: 0.7).
            top_p (float): The top_p value for nucleus sampling (default: 0.8).
            token_length (int): The maximum token length for the generated responses (default: 512).
        """
        self.client = client
        self.model = model
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.top_p = top_p
        self.token_length = token_length


# class NameOfPipeline(BasePipeline):
#
#     def __call__(self, content: str) -> Optional[List[Dict[str, str]]]:
#
#         try:
#             pass
#         except Exception as e:
#             raise RuntimeError(f"An error occurred while processing the content: {e}")


class CodeExplanationPipeline(BasePipeline):

    def __call__(self, content: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate Code
            messages = [
                {"role": "system", "content": "You are an expert in various programming languages."},
                {"role": "user", "content": "Please provide an example of code that accomplishes any given task or functionality."},
                {"role": "user", "content": "Kindly ensure that your response contains only the code, without any supplementary explanations or commentary."}
            ]

            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )

            code = response.choices[0].message.content

            # Generate Answer
            messages = [
                {"role": "system", "content": "You are an expert in explaining code and clarifying programming concepts."},
                {"role": "user", "content": "Below is the code for which you need to generate an explanation:"},
                {"role": "user", "content": code},
                {"role": "user", "content": (
                    "Based on the provided code, generate a clear and detailed explanation of what the code does."
                    "The explanation should be easy to understand, with a focus on the purpose of the code, its key components, and any important logic or functions."
                    "Make sure to explain how the code works step-by-step, including any critical parts like loops, conditions, or function calls."
                    "Your response should be focused solely on the explanation, without additional information or comments."
                    )
                }
                ]

            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )

            answer = response.choices[0].message.content

            # Generate Instruction data
            instruct_data = [
                {"role": "system", "content": "You are a programming expert."},
                {"role": "user", "content": "Please explain about this given code"},
                {"role": "user", "content": f"{code}"},
                {"role": "assistant", "content": f"{answer}"},
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")