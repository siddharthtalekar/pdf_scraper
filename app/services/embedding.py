import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyDXaEq7rvGLJLfpF8usnxB4nrD3uUdCjjI"

from langchain.vectorstores import Qdrant
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.schema import Document
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

COLLECTION_NAME = "pdf_collection"
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def embed_and_store(text: str, source: str):
    docs = [Document(page_content=text, metadata={"source": source})]


    Qdrant.from_documents(
        documents=docs,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        location="http://localhost:6333"
    )
  
