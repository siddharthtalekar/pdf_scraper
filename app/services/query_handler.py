import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyDXaEq7rvGLJLfpF8usnxB4nrD3uUdCjjI"

from langchain.vectorstores import Qdrant
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
from qdrant_client import QdrantClient
from langchain.chains.question_answering import load_qa_chain

qdrant = QdrantClient(host="localhost", port=6333)
COLLECTION_NAME = "pdf_collection"

def answer_query(question: str) -> str:
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    db = Qdrant(
        client=qdrant,
        collection_name=COLLECTION_NAME,
        embeddings=embeddings
    )

    retriever = db.as_retriever(search_type="mmr")
    docs = retriever.get_relevant_documents(question)

    llm = GoogleGenerativeAI(model="gemini-1.5-flash")

    chain = load_qa_chain(llm, chain_type="stuff")
    return chain.run(input_documents=docs, question=question)

