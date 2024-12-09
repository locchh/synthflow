import os
import tiktoken
from openai import OpenAI
from typing import List, Dict

def count_tiktoken_length(messages: List[Dict[str, str]], model_name: str = "gpt-3.5-turbo") -> int:
    """
    Counts the total number of tokens in a list of messages using tiktoken.

    Args:
        messages (List[Dict[str, str]]): List of messages, where each message is a dictionary
                                         with keys like "role" and "content".
        model_name (str): The name of the model for which the tokenization should be done.
                          Default is "gpt-3.5-turbo".

    Returns:
        int: Total number of tokens across all messages.
    """
    try:
        # Load the tokenizer for the specified model
        encoding = tiktoken.encoding_for_model(model_name)
        
        total_tokens = 0
        
        for message in messages:
            for key, value in message.items():
                # Count tokens for each value in the message dictionary
                total_tokens += len(encoding.encode(value))
        
        return total_tokens
    except Exception as e:
        raise RuntimeError(f"Error in calculating token length: {e}")
        

def set_openai_key(path_to_key: str = "/home/loc/Documents/keys/OPENAI_API_KEY.txt") -> None:
    """
    Sets the OpenAI API key from a file to an environment variable.

    Args:
        path_to_key (str): Path to the file containing the OpenAI API key.
                           Default is '/home/loc/Documents/keys/OPENAI_API_KEY.txt'.
    """
    # Check if the path exists
    if os.path.exists(path_to_key):
        with open(path_to_key, "r") as f:
            api_key = f.read().strip()  # Read and strip any extra whitespace/newlines
        os.environ["OPENAI_API_KEY"] = api_key  # Set the environment variable
        print(f"API key set successfully.")
    else:
        raise FileNotFoundError(f"{path_to_key} does not exist!")  # Use a proper exception


def test_openai_api(model: str = "gpt-4") -> None:
    """
    Tests the OpenAI API by generating a chat completion with a simple prompt.

    Args:
        model (str): The name of the model to use. Default is 'gpt-4'.
    """
    try:
        client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
        )

        
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model="gpt-4o",
        )

        # Access the assistant's response content
        response_content = response.choices[0].message.content
        print(response_content)
        
    except Exception as e:
        print(f"An error occurred: {e}")


def create_openai_client() -> OpenAI | None:
    """
    Creates an instance of the OpenAI client using the API key from the environment variable.

    Returns:
        OpenAI | None: The OpenAI client instance if successful, otherwise None.
    """
    try:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
        
        client = OpenAI(api_key=api_key)
        return client
    except Exception as e:
        print(f"Failed to create OpenAI client: {e}")
        return None