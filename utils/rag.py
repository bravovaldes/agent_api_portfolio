from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json

def load_docs(json_path: str):
    with open(json_path, "r") as f:
        data = json.load(f)
    docs = []
    for k, v in data.items():
        text = json.dumps(v, indent=2, ensure_ascii=False)
        docs.append(Document(page_content=f"{k.upper()}:\n{text}"))
    return docs

def load_vectorstore():
    docs = load_docs("data/valdes.json")
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(docs)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=OpenAIEmbeddings(),
        persist_directory="db"
    )
    vectordb.persist()
    return vectordb
