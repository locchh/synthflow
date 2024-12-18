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


class ErrorAnalysisPipeline(BasePipeline):

    def __call__(self, content: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate Question
            messages = [
                {"role": "system", "content": "You are an expert in creating clear and insightful questions specifically about error analysis in system administration."},
                {"role": "user", "content": "Below is the content for generating a question:"},
                {"role": "user", "content": content},
                {"role": "user", "content": (
                    "Based on the above content, generate a question that focuses specifically on understanding and troubleshooting error messages within a system administration context."
                    " The question should be clear, concise, and focused on testing the ability to identify and resolve common errors based on the given details."
                    " The question should provide enough context for someone to answer it without needing to refer back to the content."
                    " Please provide only the question in your response, without any extra information or explanation."
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

            # Generate Answer
            messages = [
                {"role": "system", "content": "You are an expert who answers questions clearly and in a natural, conversational style."},
                {"role": "user", "content": "Please provide a thoughtful and detailed response to the following error analysis question:"},
                {"role": "user", "content": f"{question}"}
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
                {"role": "user", "content": "Please answer the following question."},
                {"role": "user", "content": f"{question}"},
                {"role": "assistant", "content": f"{answer}"},
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class IntegrationPipeline(BasePipeline):

    def __call__(self, content: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate Question about System Integration
            messages = [
                {"role": "system", "content": "You are an expert in creating clear and insightful questions specifically about system integration."},
                {"role": "user", "content": "Below is the content for generating a question:"},
                {"role": "user", "content": content},
                {"role": "user", "content": (
                    "Based on the above content, generate a question that focuses specifically on system integration, including connecting legacy systems to modern technologies or platforms."
                    " The question should be clear, concise, and focused on testing the ability to identify key integration techniques and tools."
                    " The question should provide enough context for someone to answer it without needing to refer back to the content."
                    " Please provide only the question in your response, without any extra information or explanation."
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

            # Generate Answer about System Integration
            messages = [
                {"role": "system", "content": "You are an expert who answers questions clearly and in a natural, conversational style."},
                {"role": "user", "content": "Please provide a thoughtful and detailed response to the following system integration question:"},
                {"role": "user", "content": f"{question}"}
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
                {"role": "user", "content": "Please answer the following question."},
                {"role": "user", "content": f"{question}"},
                {"role": "assistant", "content": f"{answer}"},
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class PerformanceOptimizationPipeline(BasePipeline):

    def __call__(self, content: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate Performance Optimization Question
            messages = [
                {"role": "system", "content": "You are an expert in creating clear and insightful questions specifically about performance optimization techniques."},
                {"role": "user", "content": "Below is the content for generating a question:"},
                {"role": "user", "content": content},
                {"role": "user", "content": (
                    "Based on the above content, generate a question that focuses specifically on performance optimization strategies."
                    " The question should be clear, concise, and focused on testing the ability to identify and apply optimization techniques based on system requirements."
                    " The question should provide enough context for someone to answer it without needing to refer back to the content."
                    " Please provide only the question in your response, without any extra information or explanation."
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

            # Generate Performance Optimization Answer
            messages = [
                {"role": "system", "content": "You are an expert who answers questions clearly and in a natural, conversational style."},
                {"role": "user", "content": "Please provide a thoughtful and detailed response to the following performance optimization question:"},
                {"role": "user", "content": f"{question}"}
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
                {"role": "user", "content": "Please answer the following question."},
                {"role": "user", "content": f"{question}"},
                {"role": "assistant", "content": f"{answer}"},
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class MigrationPipeline(BasePipeline):

    def __call__(self, content: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate System Migration Question
            messages = [
                {"role": "system", "content": "You are an expert in creating clear and insightful questions specifically about system migration tasks."},
                {"role": "user", "content": "Below is the content for generating a question:"},
                {"role": "user", "content": content},
                {"role": "user", "content": (
                    "Based on the above content, generate a question that focuses specifically on the steps and considerations involved in system migration."
                    " The question should be clear, concise, and focused on testing the ability to understand and apply the concepts related to migrating a system from one environment to another."
                    " The question should provide enough context for someone to answer it without needing to refer back to the content."
                    " Please provide only the question in your response, without any extra information or explanation."
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

            # Generate System Migration Answer
            messages = [
                {"role": "system", "content": "You are an expert in providing thoughtful, clear, and detailed responses to system migration-related questions."},
                {"role": "user", "content": "Please provide a thoughtful and detailed response to the following system migration question:"},
                {"role": "user", "content": f"{question}"}
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
                {"role": "user", "content": "Please answer the following question."},
                {"role": "user", "content": f"{question}"},
                {"role": "assistant", "content": f"{answer}"},
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class SystemConfigurationPipeline(BasePipeline):

    def __call__(self, content: str) -> Optional[List[Dict[str, str]]]:

        try:
            
            # Generate System Configuration Question
            messages = [
                {"role": "system", "content": "You are an expert in creating clear and insightful questions specifically about system configuration tasks and best practices."},
                {"role": "user", "content": "Below is the content for generating a question:"},
                {"role": "user", "content": content},
                {"role": "user", "content": (
                    "Based on the above content, generate a question that focuses specifically on system configuration and related tasks."
                    " The question should be clear, concise, and focused on testing the ability to apply proper configuration techniques based on system requirements."
                    " The question should provide enough context for someone to answer it without needing to refer back to the content."
                    " Please provide only the question in your response, without any extra information or explanation."
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

            # Generate System Configuration Answer
            messages = [
                {"role": "system", "content": "You are an expert in providing clear, detailed, and thoughtful responses to system configuration questions."},
                {"role": "user", "content": "Please provide a thoughtful and detailed response to the following system configuration question:"},
                {"role": "user", "content": f"{question}"}
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
                {"role": "user", "content": "Please answer the following question."},
                {"role": "user", "content": f"{question}"},
                {"role": "assistant", "content": f"{answer}"},
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class ProgrammingPipeline(BasePipeline):

    def __call__(self, content: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate Programming Code Question
            messages = [
                {"role": "system", "content": "You are an expert in creating clear and insightful questions specifically about writing programming code in various programming languages."},
                {"role": "user", "content": "Below is the content for generating a question:"},
                {"role": "user", "content": content},
                {"role": "user", "content": (
                    "Based on the above content, generate a question that focuses specifically on writing programming code to solve a particular problem."
                    " The question should be clear, concise, and focused on testing the ability to write correct and efficient code based on the provided requirements."
                    " The question should provide enough context for someone to write a relevant code solution without needing to refer back to the content."
                    " Please provide only the question in your response, without any extra information or explanation."
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

            # Generate Programming Code Answer
            messages = [
                {"role": "system", "content": "You are an expert in writing clear and efficient programming code in various languages."},
                {"role": "user", "content": "Please provide a thoughtful and detailed response to the following programming code question:"},
                {"role": "user", "content": f"{question}"}
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
                {"role": "user", "content": "Please answer the following question."},
                {"role": "user", "content": f"{question}"},
                {"role": "assistant", "content": f"{answer}"},
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class SystemOperationPipeline(BasePipeline):

    def __call__(self, content: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate Question about System Operations
            messages = [
                {"role": "system", "content": "You are an expert in creating clear and insightful questions specifically about system operations and related tasks."},
                {"role": "user", "content": "Below is the content for generating a question:"},
                {"role": "user", "content": content},
                {"role": "user", "content": (
                    "Based on the above content, generate a question that focuses specifically on system operations tasks."
                    " The question should be clear, concise, and focused on testing the ability to understand and apply key system operation principles."
                    " The question should provide enough context for someone to answer it without needing to refer back to the content."
                    " Please provide only the question in your response, without any extra information or explanation."
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

            # Generate Answer about System Operations
            messages = [
                {"role": "system", "content": "You are an expert who answers questions clearly and in a natural, conversational style."},
                {"role": "user", "content": "Please provide a thoughtful and detailed response to the following system operations question:"},
                {"role": "user", "content": f"{question}"}
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
                {"role": "user", "content": "Please answer the following question."},
                {"role": "user", "content": f"{question}"},
                {"role": "assistant", "content": f"{answer}"},
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class CommandReferencePipeline(BasePipeline):

    def __call__(self, content: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate Question
            messages = [
                {"role": "system", "content": "You are an expert in creating clear and insightful questions specifically about command references for system administration."},
                {"role": "user", "content": "Below is the content for generating a question:"},
                {"role": "user", "content": content},
                {"role": "user", "content": (
                    "Based on the above content, generate a question that focuses specifically on referencing the correct command for a system administration task."
                    " The question should be clear, concise, and focused on testing the ability to identify and apply the correct command based on system requirements."
                    " The question should provide enough context for someone to answer it without needing to refer back to the content."
                    " Please provide only the question in your response, without any extra information or explanation."
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

            # Generate answer
            messages = [
                {"role": "system", "content": "You are an expert who answers questions clearly and in a natural, conversational style."},
                {"role": "user", "content": "Please provide a thoughtful and detailed response to the following command reference question:"},
                {"role": "user", "content": f"{question}"}
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
                {"role": "user", "content": "Please answer the following question."},
                {"role": "user", "content": f"{question}"},
                {"role": "assistant", "content": f"{answer}"},
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class TroubleshootingPipeline(BasePipeline):

    def __call__(self, content: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate Question
            messages = [
                {"role": "system", "content": "You are an expert in creating clear and insightful questions specifically about troubleshooting technical issues."},
                {"role": "user", "content": "Below is the content for generating a question:"},
                {"role": "user", "content": content},
                {"role": "user", "content": (
                    "Based on the above content, generate a question that focuses specifically on troubleshooting the issue described."
                    " The question should be clear, concise, and focused on testing the ability to apply troubleshooting methods and techniques."
                    " The question should provide enough context for someone to answer it without needing to refer back to the content."
                    " Please provide only the question in your response, without any extra information or explanation."
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

            # Generate Answer
            messages = [
                {"role": "system", "content": "You are an expert who answers questions clearly and in a natural, conversational style."},
                {"role": "user", "content": "Please provide a thoughtful and detailed response to the following troubleshooting question:"},
                {"role": "user", "content": f"{question}"}
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
                {"role": "user", "content": "Please answer the following question."},
                {"role": "user", "content": f"{question}"},
                {"role": "assistant", "content": f"{answer}"},
            ]

            return instruct_data

        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")


class DefinitionPipeline(BasePipeline):

    def __call__(self, content: str) -> Optional[List[Dict[str, str]]]:

        try:
            # Generate Question
            messages = [
                {"role": "system", "content": "You are an expert in creating clear and insightful questions specifically about definitions or terminology."},
                {"role": "user", "content": "Below is the content for generating a question:"},
                {"role": "user", "content": content},
                {"role": "user", "content": (
                    "Based on the above content, generate a question that focuses specifically on the definitions or terminology presented."
                    " The question should be clear, concise, and focused on testing the understanding of the defined terms or concepts."
                    " The question should provide enough context for someone to answer it without needing to refer back to the content."
                    " Please provide only the question in your response, without any extra information or explanation."
                )}
            ]

            # messages = [
            #     {"role": "system", "content": "You are an expert in creating clear and insightful questions based on given content."},
            #     {"role": "user", "content": "Below is the content for generating a question:"},
            #     {"role": "user", "content": content},
            #     {"role": "user", "content": (
            #         "Based on the above content, generate a question that focuses on testing the understanding of the definition or concept presented."
            #         " The question should be clear, concise, and detailed enough for someone to answer without needing to refer back to the content."
            #         " Please provide only the question in your response, without any extra information or explanation."
            #     )}
            # ]

            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=random.uniform(self.temp_min, self.temp_max),
                max_tokens=self.token_length,
                top_p=self.top_p
            )

            question = response.choices[0].message.content

            # Generate Answer
            messages = [
                {"role": "system", "content": "You are an expert who answers questions clearly and in a natural, conversational style."},
                {"role": "user", "content": "Please provide a thoughtful and natural response to the following question:"},
                {"role": "user", "content": f"{question}"}
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
                {"role": "user", "content": "Please answer the following question."},
                {"role": "user", "content": f"{question}"},
                {"role": "assistant", "content": f"{answer}"},
            ]

            return instruct_data
        
        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")