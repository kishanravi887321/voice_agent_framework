from voice_agent.voice_agent import VoiceAgent

import os
from dotenv import load_dotenv
load_dotenv()

agent = VoiceAgent(
    llm_type="gemini", 
    api_key=os.getenv("GOOGLE_API_KEY"), 
    model_name="gemini-1"
)

response = agent.run_llm("Write me a poem about the ocean.")
print(response)
