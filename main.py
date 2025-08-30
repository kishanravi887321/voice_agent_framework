import os
from dotenv import load_dotenv
from voice_agent.voice_agent import VoiceAgent

load_dotenv()

agent = VoiceAgent(
    llm_type="gemini", 
    api_key=os.getenv("GEMINI_API_KEY"), 
    model_name="gemini-1"
)

response = agent.run_llm("Wrie about the mahtama gandhi ")
print(response)


# from voice_agent.voice_agent import TrainVoiceAgent

# # --- Insert training data ---
# trainer = TrainVoiceAgent(train=False, folder_path="./data_folder", email="ravi@example.com")
# # If you don't want to auto-train at init, use:
# # trainer = TrainVoiceAgent(train=False)
# # trainer.insert_data()

# # --- Query previously inserted data ---
# # chunks = trainer.retrieve_data("What are the applications of AI in healthcare?")
# # print("Relevant chunks:")
# # for c in chunks:
# #     print("-", c)
