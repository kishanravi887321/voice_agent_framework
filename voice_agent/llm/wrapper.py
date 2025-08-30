from base  import BaseLLM
from gemini_llm import GeminiClient

class GeminiLLm(BaseLLM):
    def __init__(self, api_key: str):
        self.client = GeminiClient(api_key=api_key)

    def ask(self, question: str, context: str = "") -> str:
        if context:
            question = f"Context: {context}\n\nQuestion: {question}"
        response = self.client.ask(question)
        return response
    

