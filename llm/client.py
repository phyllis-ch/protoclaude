import ollama
from config import LLM_MODEL

class LLM:
    def __init__(self):
        self.model = LLM_MODEL

    def generate(self, messages, tools=None):
        return ollama.chat(
            model=self.model,
            messages=messages,
            tools=tools or [],
            think=False,
            stream=True,
            # options={
            #     "num_predict": 512,
            #     "num_ctx": 4096
            # }
        )
