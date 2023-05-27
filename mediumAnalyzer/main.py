import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain import VectorDBQA, OpenAI
import pinecone

pinecone.init(
    api_key="f3dd05f7-d7bd-4964-9d1a-4a826e63088a",
    environment="asia-southeast1-gcp-free",
)

if __name__ == "__main__":
    print("Hello world")
    loader = TextLoader("/home/jimmy/LLM/mediumAnalyzer/blog.txt")
    # convert text file to document
    document = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(len(texts))

    # embeddings -- convert text into vectors
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    doc_search = Pinecone.from_documents(texts, embeddings, index_name="blogs-index")

    # VectorDBQA chain takes the prompt, embeds as vector, then plots it to vector db which db returns closest vectors
    qa = VectorDBQA.from_chain_type(
        llm=OpenAI(),
        chain_type="stuff",
        vectorstore=doc_search,
        return_source_document=True,
    )

    query = "What is a vector DB? Give me a 15 word answer for a begineer"
    result = qa({"query": query})
    print(result)
