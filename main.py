# from voice_agent.stt.speech_to_text import SpeechToText

# stt = SpeechToText(api_key="3294cac533734554b16271ce993b897c")
# output = stt.start()


from voice_agent.gather.llama_read import LlamaRead

reader=LlamaRead(api_key="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",
                 folder_path="data_folder")

