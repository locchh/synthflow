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

class TroubleshootingPipeline(BasePipeline):

    def __call__(self, content: str) -> Optional[List[Dict[str, str]]]:
        pass

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
                {"role": "user", "content": f"{answer}"},
            ]

            return instruct_data
        
        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the content: {e}")