import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

os.environ.get('OPENAI_API_KEY')

if __name__ == '__main__':
    pdf_path = '/home/jimmy/LLM/mediumAnalyzer/2210.03629.pdf'
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator='\n')
    docs = text_splitter.split_documents(documents=documents)

    # fiass converts text/pdf to perform similarity context to feed to LLM
    embeddings = OpenAIEmbeddings()
    # Faiss --vector
    vector_store = FAISS.from_documents(docs, embeddings)
    vector_store.save_local('faiss_index_react')

    new_vector_store = FAISS.load_local('faiss_index_react', embeddings)
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type='stuff', retriever = new_vector_store.as_retriever())
    res = qa.run('Give me the gist of React in 3 minutes')
    print(res)