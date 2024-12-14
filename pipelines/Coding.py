import random
from typing import Any, List, Dict, Optional

class BasePipeline:
    """
    Base pipeline for inheritance
    """

    def __init__(self, client: Any, model: str = "gpt-4o", temp_min: float = 0.3, 
                temp_max: float = 0.8, top_p: float = 0.5, token_length: int = 1024):
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


class CodeCompletionPipeline(BasePipeline):

    def __call__(self, content: str) -> Optional[List[Dict[str, str]]]:

        try:
            pass
        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class CodeGenerationPipeline(BasePipeline):

    def __call__(self, language: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate request for writing code
            messages = [
                {"role": "system", "content": "You are a seasoned expert in various programming languages."},
                {"role": "user", "content": (
                    f"Could you generate a request for code generation in {language}?"
                    " The request should include a comprehensive description of the desired functionality, expected behavior, and any specific requirements or constraints for the implementation."
                    " Please ensure that the request is clear, concise, easily understandable and in Task-oriented style."
                )},
                {"role": "user", "content": "Kindly respond with the request only, without any additional explanations or commentary."}
            ]

            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )

            request = response.choices[0].message.content

            # Generate code
            messages = [
                {"role": "system", "content": "You are an expert in various programming languages."},
                {"role": "user", "content": f"{request}"},
                {"role": "user", "content": "Please respond with the code only, without any additional explanations or comments."}
            ]

            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )

            code = response.choices[0].message.content

            # Generate Instruction data
            instruct_data = [
                {"role": "system", "content": "You are a programming expert."},
                {"role": "user", "content": request},
                {"role": "assistant", "content": code}
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class CodeDebuggingPipeline(BasePipeline):

    def __call__(self, language: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate Code need to fix
            messages = [
                {"role": "system", "content": "You are an expert in various programming languages."},
                {"role": "user", "content": f"Can you provide an example of code in {language} for any task or functionality that contains a bug or issue? The code should be incorrect or malfunctioning."},
                {"role": "user", "content": "Please respond with the code only, without any additional explanations or comments."}
            ]

            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )

            code = response.choices[0].message.content

            # Generate Answer solution
            messages = [
                {"role": "system", "content": "You are an expert in various programming languages."},
                {"role": "user", "content": ("Here is a code snippet that contains issues."
                                            "Could you please identify and fix the problems in the code?"
                                            "Ensure that the code functions correctly after the changes. Here is the code:")
                },
                {"role": "user", "content": code}
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
                {"role": "user", "content": ("Here is a code snippet that contains issues."
                                            "Could you please identify and fix the problems in the code?"
                                            "Ensure that the code functions correctly after the changes. Here is the code:")
                                            },
                {"role": "user", "content": f"{code}"},
                {"role": "assistant", "content": f"{answer}"}
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class CodeExplanationPipeline(BasePipeline):

    def __call__(self, language: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate Code need to explain
            messages = [
                {"role": "system", "content": "You are an expert in various programming languages."},
                {"role": "user", "content": f"Please provide an example of {language} code that accomplishes any given task or functionality."},
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

            # Generate Answer explain the code
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