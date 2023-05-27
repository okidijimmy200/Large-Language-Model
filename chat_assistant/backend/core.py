import os
from typing import Any, Dict, List

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Pinecone
import pinecone


pinecone.init(
    api_key=os.environ["PINE_CONE_API_KEY"],
    environment=os.environ["PINE_CONE_ENVIRONMENT"],
)

INDEX_NAME = "langchain-doc-index"

'''Implements chain to retrieve vectors from vectorstore'''
def run_llm(query: str, chat_history: List[Dict[str, Any]] = []):
    # create embedings model
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
    '''retrieve vectors from pincone'''
    docsearch = Pinecone.from_existing_index(
        embedding=embeddings,
        index_name=INDEX_NAME,
    )
    '''initialize chat api'''
    chat = ChatOpenAI(
        verbose=True,
        temperature=0,
    )

    '''ConversationalRetrievalChain this allows us pass chat history'''
    qa = ConversationalRetrievalChain.from_llm(
        # chat
        llm=chat, 
        # retriever is a wrapper around vectorstore to help in similarity search
        retriever=docsearch.as_retriever(), 
        # helps us determine which vectors to get answers for
        return_source_documents=True
    )

    return qa({"question": query, "chat_history": chat_history})