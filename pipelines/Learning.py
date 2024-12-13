import random

class DefinitionPipeline:

    def __init__(self, client,model="gpt-4o", temp_min=0.4, temp_max=0.7, top_p=0.8, token_length=512):
        self.client = client
        self.model = model
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.top_p = top_p
        self.token_length = token_length

    def __call__(self, content: str):
        pass
