# from voice_agent.stt.speech_to_text import SpeechToText

# stt = SpeechToText(api_key="3294cac533734554b16271ce993b897c")
# output = stt.start()
import os
# from voice_agent.gather.vector_read import VectoRead
from dotenv import load_dotenv
load_dotenv()
# vectoread = VectoRead(
#     pinecone_api_key=os.getenv("PINECONE_API_KEY"),
#     index_name=os.getenv("PINECONE_INDEX_NAME"),
#     folder_path="./data_folder",
# )

# # Upsert all TXT files
# vectoread.upsert_folder_to_vectordb(email="ravi@example.com")

# # Query for relevant chunks
# chunks = vectoread.get_relevant_chunks("tell me about your functionality and why I choose to use you", email="ravi@example.com")
# print(chunks)




from voice_agent.llm.factory import LLMFactory

llm=LLMFactory.get_llm("gemini", api_key=os.getenv("GOOGLE_API_KEY")) 

print(llm.ask("Explain the theory of relativity in simple terms."))