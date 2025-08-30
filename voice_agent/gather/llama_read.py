import os
import openai
from llama_index import LLMPredictor, ServiceContext
from llama_index.llms import OpenAI as LlamaOpenAI
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

class LlamaRead:
    def __init__(self, api_key: str, folder_path: str, model: str = "gpt-3.5-turbo"):
        """
        Initialize LlamaRead with OpenRouter/OpenAI API key and folder path.
        :param api_key: OpenRouter or OpenAI API key
        :param folder_path: Path to folder containing text documents
        :param model: Model to use (default gpt-3.5-turbo)
        """
        self.api_key = api_key
        self.folder_path = folder_path
        self.model = model
        self.index_file = "document_index.json"
        self.index = None

        # Configure OpenRouter/OpenAI
        openai.api_key = self.api_key
        openai.api_base = "https://openrouter.ai/api/v1"

        # Load documents and create/load index
        self._load_or_create_index()

    def _load_or_create_index(self):
        # Load documents
        documents = SimpleDirectoryReader(self.folder_path).load_data()

        # Create LLM predictor
        llm_predictor = LLMPredictor(
            llm=LlamaOpenAI(
                model=self.model,
            )
        )
        service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

        # Check if index exists
        if os.path.exists(self.index_file):
            self.index = GPTSimpleVectorIndex.load_from_disk(self.index_file)
        else:
            self.index = GPTSimpleVectorIndex(documents, service_context=service_context)
            self.index.save_to_disk(self.index_file)

    def ask(self, question: str) -> str:
        """
        Ask a question to the document index
        :param question: The question string
        :return: Answer from documents
        """
        if not self.index:
            raise ValueError("Index not initialized")
        response = self.index.query(question)
        return str(response)
