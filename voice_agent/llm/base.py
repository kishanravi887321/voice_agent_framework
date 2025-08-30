
from gemini_llm import GeminiClient

client = GeminiClient(api_key="AIzaSyAxH3aGTKQ3qDAUL87DP_djqE8RO8PaNo0")

# Ask a question
context = "Python is a high-level programming language used for web development, AI, and more."
query = "Explain Python in simple terms."
answer = client.ask(query, context)

print("Gemini says:", answer)