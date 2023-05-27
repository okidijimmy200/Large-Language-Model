import os
from langchain.document_loaders import ReadTheDocsLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from consts import INDEX_NAME
import pinecone

'''initialize pinecone client'''
pinecone.init(
    api_key=os.environ.get("PINE_CONE_API_KEY"),
    environment=os.environ.get("PINE_CONE_ENVIRONMENT"),
)

'''read document, embedd it and push to pincone vector database'''
def ingest_docs():
    '''read document from docs folder'''
    loader = ReadTheDocsLoader(
        path="docs/langchain-docs/python.langchain.com/en/latest"
    )
    raw_documents = loader.load()
    # print(f'loaded {len(raw_documents)} documents')
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=100, separators=["\n\n", "\n", " ", ""]
    )

    # split langchain docs into chunks
    documents = text_splitter.split_documents(documents=raw_documents)

    '''iterate though documents, retrieving the source key replacing the prefix of it between langchain docs to http'''
    for doc in documents:
        old_path = doc.metadata["source"]
        new_url = old_path.replace("langchain-docs", "https:/")
        doc.metadata.update({"source": new_url})

    print(f"Going to insert {len(documents)} to Pinecone")
    '''embed documents'''
    embeddings = OpenAIEmbeddings()
    '''upload embedded vectors into pincone'''
    Pinecone.from_documents(
        documents=documents, embedding=embeddings, index_name=INDEX_NAME
    )
    print("************** Added to Pinecone VectorStore*******************")


if __name__ == "__main__":
    ingest_docs()
