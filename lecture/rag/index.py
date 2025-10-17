# This file will be used to indexing the pdf 
# THIS IS THE INDEXING PHASE

from dotenv import load_dotenv

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings



load_dotenv()

pdf_path = Path(__file__).parent / "Pranjal_Resume.pdf"

# Load the PDF
loader = PyPDFLoader(file_path=pdf_path)
docs=loader.load() # page by page reading of the pdf

# spliitting the doc into smaller chunks
text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20, # 20 char will be overlapped in the next chunk
    )

chunks=text_splitter.split_documents(documents=docs)


# now we will create the embeddings of the chunks
embeddings_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
# using the google gemini embedding model


# now we will store the embeddings in the vector db
vector_store=QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings_model,
    url="http://localhost:6333", # url of docker container
    collection_name="resume" )

print("Indexing completed successfully!!")


# go to /dashboard and check the collection is created or not