import os
from dotenv import load_dotenv

from voice_agent.gather.vector_read import VectoRead
from voice_agent.llm.gemini_llm import GeminiLLm
from voice_agent.llm.openai_llm import OpenAILLM
from voice_agent.llm.ollma_llm import OllamaLLM
from voice_agent.llm.openrouter_service_llm import OpenRouterLLM
from voice_agent.llm.claude_llm import ClaudeLLM
from voice_agent.llm.custom_llm import CustomLLm

load_dotenv()


class VoiceAgent:
    """
    Unified class for:
    1. Training / querying a vector database.
    2. Selecting and using different LLMs via direct SDK interface.
    """

    def __init__(self, 
                 llm_type: str = "openai", 
                 folder_path: str = "./data_folder", 
                 email: str = "user@example.com", 
                 train: bool = False, 
                 **kwargs):
        """
        Args:
            llm_type (str): Type of LLM (gemini, openai, ollama, openrouter, claude, custom)
            folder_path (str): Path to TXT files for vector DB
            email (str): Namespace key for vector DB entries
            train (bool): Whether to trigger vector DB training at init
            **kwargs: Extra args passed to LLM constructors (e.g. api_key, model_name)
        """
        self.folder_path = folder_path
        self.email = email
        self.train = train

        # Initialize vector handler
        self.vectoread = VectoRead(
            pinecone_api_key=os.getenv("PINECONE_API_KEY"),
            index_name=os.getenv("PINECONE_INDEX_NAME"),
            folder_path=self.folder_path
        )
        if self.train:
            self.train_vector_db()

        # Initialize LLM
        self.llm = self._get_llm(llm_type, **kwargs)

    # -------------------------
    # Vector DB Functions
    # -------------------------
    def train_vector_db(self):
        """Upsert all files from the folder to the vector DB."""
        print("[INFO] Training vector DB with files from:", self.folder_path)
        self.vectoread.upsert_folder_to_vectordb(email=self.email)
        print("[INFO] Training completed.")

    def query_vector_db(self, query_text):
        """Fetch relevant chunks from the vector DB."""
        print("[INFO] Querying vector DB for:", query_text)
        chunks = self.vectoread.get_relevant_chunks(query_text, email=self.email)
        return chunks

    # -------------------------
    # LLM Functions
    # -------------------------
    def _get_llm(self, llm_type: str, **kwargs):
        llm_type = llm_type.lower()
        if llm_type == "gemini":
            return GeminiLLm(api_key=kwargs.get("api_key"))
        elif llm_type == "openai":
            return OpenAILLM(api_key=kwargs.get("api_key"), 
                             model_name=kwargs.get("model_name", "gpt-4"))
        elif llm_type == "ollama":
            return OllamaLLM(model_name=kwargs.get("model_name", "gemma3"), 
                             api_key=kwargs.get("api_key"))
        elif llm_type == "openrouter":
            return OpenRouterLLM(api_key=kwargs.get("api_key"), 
                                 model_name=kwargs.get("model_name", "openrouter-model"))
        elif llm_type == "claude":
            return ClaudeLLM(api_key=kwargs.get("api_key"), 
                             model_name=kwargs.get("model_name", "claude-3"))
        elif llm_type == "custom":
            return CustomLLm(api_key=kwargs.get("api_key"), 
                             model_url=kwargs.get("model_url"))
        else:
            raise ValueError(f"Unsupported LLM type: {llm_type}")

    def run_llm(self, prompt: str, **kwargs):
        """Run the selected LLM on a given prompt."""
        if not self.llm:
            raise RuntimeError("No LLM initialized.")
        print(f"[INFO] Running prompt on {self.llm.__class__.__name__}")
        return self.llm.ask(prompt, **kwargs)
