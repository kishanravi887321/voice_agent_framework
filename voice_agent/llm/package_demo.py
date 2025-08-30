"""
Alternative demo using proper package imports
"""
import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from voice_agent.llm.gemini_llm import GeminiClient

def main():
    """Demo using package-style imports"""
    try:
        # Initialize client
        client = GeminiClient(api_key="AIzaSyAxH3aGTKQ3qDAUL87DP_djqE8RO8PaNo0")
        
        print("🤖 Gemini Chatbot Ready!")
        print("Type 'quit' to exit")
        print("-" * 40)
        
        while True:
            user_input = input("\n👤 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not user_input:
                continue
            
            # Get response from Gemini
            print("🤖 Gemini: ", end="")
            response = client.ask(user_input)
            print(response)
    
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
