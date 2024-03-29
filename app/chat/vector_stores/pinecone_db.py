import os
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore

from app.chat.embeddings.openai_embeddings import embeddings
from dotenv import load_dotenv

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index("docs")

vector_store = PineconeVectorStore.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"), embeddings
)


def build_retriever(chat_args, k):
    try:
        search_kwargs = {"filter": {"pdf_id": chat_args.pdf_id, k: k}}
        return vector_store.as_retriever(search_kwargs=search_kwargs)
    except Exception as e:
        print(e, "err")
