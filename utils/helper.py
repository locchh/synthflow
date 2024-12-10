import os
import tiktoken
from openai import OpenAI
from openai import AzureOpenAI
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


def create_azure_openai_client(config_path: str = "path/to/your/config.yaml"):
    """
    Creates and returns an Azure OpenAI client using configuration from a YAML file.

    Args:
        config_path (str): Path to the YAML configuration file (default: path/to/your/config.yaml).
    
    Returns:
        AzureOpenAI: An instance of the AzureOpenAI client.

    Raises:
        FileNotFoundError: If the YAML config file is not found.
        KeyError: If a required key is missing in the YAML file.
    """
    
    # Load the configuration from the YAML file
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found at {config_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing the YAML file: {e}")

    # Extract the necessary configuration values with fallback to default values if keys are missing
    try:
        azure_config = config.get('gpt-4o-mini', {})
        azure_endpoint = azure_config.get('API_BASE')
        api_key = azure_config.get('API_KEY')
        api_version = azure_config.get('API_VERSION')

        if not all([azure_endpoint, api_key, api_version]):
            raise KeyError("Missing required configuration keys: API_BASE, API_KEY, or API_VERSION")
    except KeyError as e:
        raise KeyError(f"Missing key in configuration: {e}")

    # Initialize the AzureOpenAI client
    client = AzureOpenAI(
        azure_endpoint=azure_endpoint,
        api_key=api_key,
        api_version=api_version,
        http_client=httpx.Client(verify=False)  # Disable SSL verification, change if needed
    )

    return client


def test_azure_openai_api(config_path: str = "path/to/your/config.yaml"):
    """
    Tests the Azure OpenAI API by sending a simple chat request.

    Args:
        config_path (str): Path to the YAML configuration file (default: path/to/your/config.yaml).
    
    Returns:
        None
    """
    
    # Load the configuration from the YAML file
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found at {config_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing the YAML file: {e}")

    # Extract required values from the config
    try:
        azure_config = config.get('gpt-4o-mini', {})
        azure_endpoint = azure_config.get('API_BASE')
        api_key = azure_config.get('API_KEY')
        api_version = azure_config.get('API_VERSION')

        if not all([azure_endpoint, api_key, api_version]):
            raise KeyError("Missing required configuration keys: API_BASE, API_KEY, or API_VERSION")
    except KeyError as e:
        raise KeyError(f"Missing required key in configuration: {e}")

    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint=azure_endpoint,
        api_key=api_key,
        api_version=api_version,
        http_client=httpx.Client(verify=False)
    )

    # Define the test messages
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello assistant, I need your help"}
    ]

    # Send the chat completion request
    try:
        response = client.chat.completions.create(
            messages=messages,
            model='gpt-4o-mini'
        )
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Error during API request: {e}")