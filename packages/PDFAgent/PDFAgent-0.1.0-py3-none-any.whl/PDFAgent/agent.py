"""Main Agent for reading PDFs
"""
from blitzchain import Client

class PDFAgent:
    def __init__(
            self, 
            name: str,
            api_key: str, 
            base_url: str=None
        ):
        self.api_key = api_key
        self.base_url = base_url if base_url else "https://app.twilix.io/api/v1"
        self.client: Client = Client(api_key)
        self.name = name
        self.collection = self.client.Collection(name)

    def insert_pdf(self, url: str):
        """Inserting a PDF via URL.
        """
        result = self.collection.insert_pdf(url)
        print("Inserting PDF... Please wait 30-60 seconds for this to finish indexing.")
        return result
    
    def ask(self, question: str, conversation_id: str=None):
        """Ask your PDF a question
        """
        return self.collection.generative_qa(
            prompt=question,
            prompt_fields=None,
            conversation_id=conversation_id
        )

    def template(self, prompt: str, conversation_id: str=None):
        """Use a template to analyze how your PDF
        """
        return self.collection.template(
            prompt=prompt,
            prompt_fields=["autoGen_content"],
            conversation_id=conversation_id
        )

    def copilot(self, prompt: str, conversation_id: str=None):
        """The endpoint for advanced analysis
        """
        return self.collection.copilot(
            prompt=prompt,
            prompt_fields=["autoGen_content"],
            conversation_id=conversation_id,
            include_rerank=True,
            minimum_rerank_score=0.05
        )
