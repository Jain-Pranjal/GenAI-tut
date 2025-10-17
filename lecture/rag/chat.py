# this is the retrieval phase

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from openai import OpenAI
import os


load_dotenv()

# basically using the open ai syntax but all the requests will go to google gemini endpoint
openai_client=OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

embeddings_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")


# now we need to search the user query in the vector db so for that we will use the from_existing_collection method
vector_db=QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="resume",
    embedding=embeddings_model
)


# taking the user query
user_query=input(">> Enter your query : ")

search_results=vector_db.similarity_search(query=user_query, k=3) # k is the number of similar documents to be retrieved

# it will automatically convert the user query into embedding and then search for the similar embeddings in the vector db and return the top k similar documents

# these search results will give the relevant chunks from the document which we will use to give the context to the llm along with the user query

context=[]

for result in search_results:
    context.append(result.page_content)

SYSTEM_PROMPT=f"""
You are a helpful assistant that helps the user based on the context given from the document. If you don't know the answer based on the context, just say that you don't know. Do not try to make up an answer.

context : {context}

"""

# chatting with the llm to get the response

response=openai_client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]
)

print(f"$$ {response.choices[0].message.content}")