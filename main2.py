from voice_agent.voice_agent2 import SpeechToText
import  os 

stt = SpeechToText(api_key=os.getenv("3294cac533734554b16271ce993b897c"), llm_type="gemini", vector_mode=False)
stt.start()   # speak → transcription → LLM → spoken answer
