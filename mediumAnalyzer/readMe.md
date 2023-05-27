Here we will be building a medium analyzing application using Langchain.

Check out this blog post that dives deep into the analyzing a document using langchain
>> https://medium.com/@okidijimmy/building-llm-powered-applications-a-beginners-guide-to-large-language-models-with-langchain-c2760b5872f5

We will be using pinecone, medium blog post copied into a blog.txt file in the root folder.

For document analyzer using pinecone in the main.py file
1. We upload .txt into the document using TextLoader.
2. We then perform text splitting using the TextSplitter from Langchain to break the document into smaller managable chunks
3. We then embedd the document converting it to vectors
4. Push and save the vectors to pinecone vectorstore. This is stored in the index in pinecone which is like a table to store our vectors
VectorDBQA chain takes the prompt, embeds as vector, then plots it to vector db which db returns closest vectors. 


In the index.py file, we do analyze .pdf file similar to how we do with the .txt file in main.py.
The difference here being we use the FAISS as our vector database.


