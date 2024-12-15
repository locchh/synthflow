import random
from typing import Any, List, Dict, Optional

class BasePipeline:
    """
    Base pipeline for inheritance
    """

    def __init__(self, client: Any, model: str = "gpt-4o", temp_min: float = 0.3, 
                temp_max: float = 0.7, top_p: float = 0.4, token_length: int = 1024):
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


class SQLQueryPipeline(BasePipeline):

    def __call__(self,) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate question
            messages = [
                {"role": "system", "content": "You are an expert in SQL query design."},
                {"role": "user", 
                "content": (
                    "Please generate a well-defined SQL query question for any task or functionality that requires retrieving or manipulating data from a database."
                    "Please respond with the question only, no extra explanations."
                )}
            ]

            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )

            question = response.choices[0].message.content

            # Generate query
            messages = [
                {"role": "system", "content": "You are an expert in SQL"},
                {
                "role": "user",
                "content": f"{question}\nPlease respond with the SQL query only, without any additional explanations or comments."
                }
            ]

            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )

            query = response.choices[0].message.content
            
            # Generate instruction data
            instruct_data = [
                {"role": "system", "content": "You are a programming expert."},
                {"role": "user", "content": question},
                {"role": "assistant", "content": query}
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class CodeDocumentationPipeline(BasePipeline):

    def __call__(self, language: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate task
            messages  = [{"role": "system", "content": "You are an expert in multiple programming languages."},
                        {"role": "user", 
                        "content": (
                            f"Generate a concise coding task in {language} that is formatted as a programming exercise."
                            "The task should be clear, well-structured, and easily understandable. Keep the description short and to the point."
                            "Please respond with the task only, no extra explanations."
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

            task_request = response.choices[0].message.content

            # Generate code
            messages = [
                {"role": "system", "content": "You are an expert in multiple programming languages."},
                {
                "role": "user",
                "content": f"{task_request}\nPlease respond with the code only, without any additional explanations or comments."
                }
            ]

            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )

            code = response.choices[0].message.content

            # Generate documentation
            messages = [
                {"role": "system", "content": "You are an expert in generating clear and comprehensive documentation for code."},
                {"role": "user", 
                "content": (
                    "Please generate detailed documentation for the following code. The documentation should include:\n"
                    "1. A brief overview of the purpose of the code.\n"
                    "2. Descriptions of key functions, methods, and classes, including their inputs, outputs, and behavior.\n"
                    "3. Any important details or assumptions made in the code.\n"
                    "4. A section on how to use or run the code, if applicable.\n"
                    "5. Any potential limitations or areas for improvement.\n\n"
                    f"Here is the code to document:\n\n{code}"
                )}
            ]

            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )

            document = response.choices[0].message.content

            # Generate instruction data
            instruct_data = [
                {"role": "system", "content": "You are a programming expert."},
                {"role": "user", "content": f"Please document the following code"},
                {"role": "user", "content": code},
                {"role": "assistant", "content": document}
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class ErrorExplanationPipeline(BasePipeline):

    def __call__(self, language: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate 
            messages = [
                {"role": "system", "content": "You are an expert in debugging and explaining programming errors."},
                {"role": "user", 
                "content": (
                    f"Generate a realistic coding error message that might occur in a programming language {language}."
                    "Please respond with the coding error message only, no extra explanations."
                )}
            ]

            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )

            error = response.choices[0].message.content

            # Generate explain
            messages = [
                {"role": "system", "content": "You are an expert in debugging and providing detailed explanations for programming errors."},
                {"role": "user", 
                "content": (
                    f"Please review the following error message generated in the {language} programming language:\n\n{error}\n\n"
                    "Provide a comprehensive explanation of the cause of this error and recommend steps to resolve or debug it. "
                    "Ensure your explanation is clear, concise, and suitable for someone looking to understand and fix the issue."
                )}
            ]

            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )

            explain = response.choices[0].message.content

            # Generate instruction data
            instruct_data = [
                {"role": "system", "content": "You are a programming expert."},
                {"role": "user", 
                "content": (
                    f"Please review the following error message generated in the {language} programming language:\n\n{error}\n\n"
                )},
                {"role": "assistant", "content": explain}
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class CodeReviewPipeline(BasePipeline):

    def __call__(self, language: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate task
            messages  = [{"role": "system", "content": "You are an expert in multiple programming languages."},
                        {"role": "user", 
                        "content": (
                            f"Generate a concise coding task in {language} that is formatted as a programming exercise."
                            "The task should be clear, well-structured, and easily understandable. Keep the description short and to the point."
                            "Please respond with the task only, no extra explanations."
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

            task_request = response.choices[0].message.content

            # Generate code
            messages = [
                {"role": "system", "content": "You are an expert in multiple programming languages."},
                {
                "role": "user",
                "content": f"{task_request}\nPlease respond with the code only, without any additional explanations or comments."
                }
            ]

            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )

            code = response.choices[0].message.content

            # Review code
            messages = [
                        {"role": "system", "content": "You are an expert code reviewer skilled in multiple programming languages."},
                        {"role": "user", 
                        "content": (
                            "Please review the following code thoroughly and provide detailed feedback. Focus on the following aspects:\n"
                            "1. **Readability and Style**: Is the code well-structured, commented, and easy to read? Are variable and function names descriptive?\n"
                            "2. **Functionality**: Does the code perform as intended? Identify any potential issues, bugs, or edge cases that may not be handled.\n"
                            "3. **Efficiency**: Could the code be optimized for better performance? Highlight any redundant or inefficient sections.\n"
                            "4. **Best Practices**: Does the code adhere to best practices for the language or framework? Are there opportunities to improve maintainability or scalability?\n"
                            "5. **Security**: Point out any potential security vulnerabilities and suggest mitigations.\n"
                            "6. **Suggestions for Improvement**: Provide actionable recommendations to improve the overall quality of the code.\n\n"
                            f"Here is the code to review:\n\n{code}"
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

            review = response.choices[0].message.content

            # Generate instruction data
            instruct_data = [
                {"role": "system", "content": "You are a programming expert."},
                {"role": "user", "content": f"Review the following {language} code and provide feedback:"},
                {"role": "user", "content": code},
                {"role": "assistant", "content": review}
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class CodeOptimizationPipeline(BasePipeline):

    def __call__(self, language: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Common system message for all requests
            system_message = {"role": "system", "content": "You are an expert in multiple programming languages."}
            
            # Generate a clear and concise coding task request
            task_request_message = {
                "role": "user", 
                "content": (
                    f"Generate a concise coding task in {language} that is formatted as a programming exercise. "
                    "The task should be clear, well-structured, and easily understandable. Keep the description short and to the point."
                    " Please respond with the task only, no extra explanations."
                )
            }
            
            response = self.client.chat.completions.create(
                messages=[system_message, task_request_message],
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )
            task_request = response.choices[0].message.content
 
            # Generate code based on the task request
            code_request_message = {
                "role": "user",
                "content": f"{task_request}\nPlease respond with the code only, without any additional explanations or comments."
            }

            response = self.client.chat.completions.create(
                messages=[system_message, code_request_message],
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )
            code_ = response.choices[0].message.content

            # Generate optimize version of code
            optimization_request_message = {
                "role": "user", 
                "content": (
                    f"Here is my {language} code:\n{code_}\n"
                    "Please optimize the following code for better performance, readability, and maintainability, without changing its original functionality."
                    "Focus on reducing redundancy, improving efficiency, and ensuring clear, concise code."
                    "Respond with the completed code only, without any extra commentary."
                )
            }

            response = self.client.chat.completions.create(
                messages=[system_message, optimization_request_message],
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )
            code = response.choices[0].message.content

            # Generate instruction data
            instruct_data = [
                {"role": "system", "content": "You are a programming expert."},
                {"role": "user", "content": (
                    f"Here is my {language} code:\n{code_}\n"
                    "Please optimize the following code for better performance, readability, and maintainability, without changing its original functionality."
                    "Focus on reducing redundancy, improving efficiency, and ensuring clear, concise code."
                    "Respond with the completed code only, without any extra commentary."
                    )
                },
                {"role": "assistant", "content": code}
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class CodeTranslationPipeline(BasePipeline):

    def __call__(self, from_language: str, to_language: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Common system message for all requests
            system_message = {"role": "system", "content": "You are an expert in multiple programming languages."}
            
            # Generate a clear and concise coding task request
            task_request_message = {
                "role": "user", 
                "content": (
                    f"Generate a concise coding task in {from_language} that is formatted as a programming exercise. "
                    "The task should be clear, well-structured, and easily understandable. Keep the description short and to the point."
                    " Please respond with the task only, no extra explanations."
                )
            }
            
            response = self.client.chat.completions.create(
                messages=[system_message, task_request_message],
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )
            task_request = response.choices[0].message.content

            # Generate code based on the task request
            code_request_message = {
                "role": "user",
                "content": f"{task_request}\nPlease respond with the code only, without any additional explanations or comments."
            }

            response = self.client.chat.completions.create(
                messages=[system_message, code_request_message],
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )
            code_ = response.choices[0].message.content

            # Generate translated code
            translation_request_message = {
                "role": "user", 
                "content": (
                    f"Here is my {from_language} code:\n{code_}\n"
                    f"Please translate the following code to {to_language}. "
                    "Ensure that the functionality of the code does not change during the translation and the logic of the program remains exactly the same."
                    " Respond with the completed code only, without any extra commentary."
                )
            }

            response = self.client.chat.completions.create(
                messages=[system_message, translation_request_message],
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )
            code = response.choices[0].message.content

            # Generate instruction data
            instruct_data = [
                {"role": "system", "content": "You are a programming expert."},
                {"role": "user", "content": f"Convert this {from_language} code to {to_language}:"},
                {"role": "user", "content": code_},
                {"role": "assistant", "content": code}
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class CodeCompletionPipeline(BasePipeline):

    def __call__(self, language: str) -> Optional[List[Dict[str, str]]]:
        try:
            # Step 1: Generate a clear and concise coding task request
            messages = [
                {"role": "system", "content": "You are an expert in multiple programming languages."},
                {"role": "user", "content": (
                    f"Generate a concise coding task in {language} that is formatted as a programming exercise. "
                    "The task should be clear, well-structured, and easily understandable."
                    " Keep the description short and to the point."
                )},
                {"role": "user", "content": "Please respond with the task only, no extra explanations."}
            ]
            
            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )
            task_request = response.choices[0].message.content

            # Step 2: Generate an incomplete code version
            incomplete_code_prompt = [
                {"role": "system", "content": "You are an expert in various programming languages."},
                {"role": "user", "content": "Please generate an incomplete version of the following request."},
                {"role": "user", "content": task_request},
                {"role": "user", "content": (
                    "The code should contain the basic structure, but key parts like logic or functionality should be missing."
                    " Leave placeholders for these missing parts so I can complete them."
                    " Please provide only the code without any additional comments or explanations."
                )}
            ]
            
            response = self.client.chat.completions.create(
                messages=incomplete_code_prompt,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )
            incomplete_code = response.choices[0].message.content

            # Step 3: Complete the code based on the incomplete version
            complete_code_prompt = [
                {"role": "system", "content": "You are an expert in various programming languages."},
                {"role": "user", "content": "Here is my incomplete code:"},
                {"role": "user", "content": incomplete_code},
                {"role": "user", "content": "Based on the following request:"},
                {"role": "user", "content": task_request},
                {"role": "user", "content": (
                    "Please complete the code by filling in the missing logic and functionality."
                    " Ensure the solution aligns with the task description provided above."
                    " Respond with the completed code only, without any extra commentary."
                )}
            ]
            
            response = self.client.chat.completions.create(
                messages=complete_code_prompt,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )
            complete_code = response.choices[0].message.content

            # Step 4: Return instruction data
            instruct_data = [
                {"role": "system", "content": "You are a programming expert."},
                {"role": "user", "content": "Here is the task you need to complete:"},
                {"role": "user", "content": task_request},
                {"role": "user", "content": "Below is the incomplete code:"},
                {"role": "user", "content": incomplete_code},
                {"role": "assistant", "content": complete_code}
            ]

            return instruct_data

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