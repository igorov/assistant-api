from langchain_community.vectorstores import Chroma
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

class ChromaDB:
    def __init__(self):
        embedder = NVIDIAEmbeddings(model="NV-Embed-QA")
        self.db = Chroma(persist_directory="./chroma_db", embedding_function=embedder)

    def get_context(self, query):
        docs = self.db.similarity_search(query)
        
        return [doc.page_content for doc in docs]