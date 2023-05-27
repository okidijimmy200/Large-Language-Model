Here we will be implementing a documentation chat helper. We are going to create a tool that assists with querying documentation. With this tool, users will be able to query using LLM (Language Model) questions about the documentation, such as how to use the documentaion and for examples of its usage.

We will build this end-to-end, meaning we will set up the entire workflow to achieve the desired result. This includes running the necessary processes and writing the frontend. For the frontend, we will utilize Streamlit, a user-friendly framework, to create an elegant and convenient user interaction experience.

We will cover
-- vector databses
-- retreival
-- similarity search
-- memory
-- insider chat
-- streamlit

The first part is to find a documentation.
We will be using the langchain documentation as an example, download it, turn it into vectors ie take every page in documentation, chunk it up, embeddd it, turn it to vector, store in a vector store, then we use it to write a chain.

--Download the langchain documentation into the root folder of your project using either of these commands (this will take a while)
wget -r -A.html -P langchain-docs https://python.langchain.com/en/latest/
!wget -r -A.html -P langchain-docs https://python.langchain.com/en/latest/
wget -r --no-parent --html-extension -P langchain-docs https://python.langchain.com/en/latest/

--Create an index in pinecone to store vector embeddings of documentations of langchain

--The docs.py file performs reading documentation, embedding it and pushing to pinecone vector database.

In backend, we create a core.py which implements chain to retrieve from the vectorstore

RetrievalQA -- Here the model we are querying is not trained in langchain, it doesnot know it even exists since langchain is a new tech of 2022 yet OpenAi is trained from 2021.
The RetrievalQA chain is going to take our prompt and query and embedd it to vector, put it in vectorstore. This then runs a similarity search and give us a couple of vectors closest to original vector.

2. We will write a chain that will use the vector database to find the correct chunks we need to answer the correct question.

3. We use streamlit as our frontend. we
to run streamlit 
>>streamlit run main.py

4. we will intergrate memory in our chat so that it has memory ability to reference things we asked it in the past