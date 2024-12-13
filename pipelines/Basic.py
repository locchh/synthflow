import random

class SimpleQAPipeline:

    def __init__(self, client,model="gpt-4o", temp_min=0.1, temp_max=0.7, top_p=0.8, token_length=512):
        self.client = client
        self.model = model
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.top_p = top_p
        self.token_length = token_length

    def __call__(self, content: str):  # Added self here
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
