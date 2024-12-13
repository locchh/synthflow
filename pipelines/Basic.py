import random
from typing import Any, List, Dict, Optional

class SimpleQAPipeline:
    """
    A class that generates a question and its corresponding answer based on the provided content
    using a language model API. It performs the task in three steps: first, generating a question
    from the content, second, generating an answer based on the question, and finally, combining
    the question and answer into an instruction data format.

    Attributes:
        client (Any): The client object that communicates with the language model API.
        model (str): The model to use for generating responses (default: "gpt-4o").
        temp_min (float): The minimum temperature value for randomness in response (default: 0.4).
        temp_max (float): The maximum temperature value for randomness in response (default: 0.7).
        top_p (float): The probability value used for nucleus sampling (default: 0.8).
        token_length (int): The maximum number of tokens to generate in each response (default: 512).
    """

    def __init__(self, client: Any, model: str = "gpt-4o", temp_min: float = 0.4, 
                 temp_max: float = 0.7, top_p: float = 0.8, token_length: int = 512):
        """
        Initializes the SimpleQAPipeline with the provided parameters.

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

    def __call__(self, content: str) -> Optional[List[Dict[str, str]]]:
        """
        Generates a question and its corresponding answer based on the provided content. 
        The process includes generating a question, an answer to the question, and
        the corresponding instruction data.

        Args:
            content (str): The content from which a question and answer are to be generated.

        Returns:
            Optional[List[Dict[str, str]]]: A list of dictionaries containing the question, answer, 
            and instruction data for further processing, or None if an error occurs.
        
        Raises:
            RuntimeError: If any error occurs during the interaction with the client or language model API.
        """
        try:
            # Generate Question
            messages = [
                {"role": "system", "content": "You are an expert in training large language models."},
                {"role": "user", "content": "Below is the content for generating a question:"},
                {"role": "user", "content": content},
                {"role": "user", "content": (
                    "Based on the above content, generate a clear and detailed question that would allow someone to answer it without referring back to the content."
                    " The question should contain enough information and context for answering."
                    " If the question is based on an example code, make sure the question retains that example code in the question itself."
                    " Your response should only be the question, without any extra information or explanation."
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
                {"role": "system", "content": "You are a programming expert."},
                {"role": "user", "content": "Please answer the following question."},
                {"role": "user", "content": f"{question}"},
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
