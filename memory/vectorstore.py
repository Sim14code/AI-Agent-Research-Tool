
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def get_vectorstore():
    embedding = OpenAIEmbeddings()
    return FAISS.load_local("faiss_index", embedding)
