import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.document_loaders import csv_loader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

google_api_key = os.getenv("google_api_key")
file_path = "codebasics_faqs.csv"
main_placeholder = st.empty()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.9)
main_placeholder.text("Initializing LLM")

# Load data
file = csv_loader.CSVLoader(file_path, source_column="prompt")
data = file.load()
main_placeholder.text("Loading Data")

# Path for storing the embeddings and vector database
embeddings_file_path = "faiss_index"
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-mpnet-base-v2')

# Check if embeddings already exist
if os.path.exists(embeddings_file_path):
    # Load precomputed vector store
    vectordb = FAISS.load_local(embeddings_file_path, embeddings, allow_dangerous_deserialization=True)
    main_placeholder.text("Loaded existing embeddings")
else:
    # Build new embeddings and save to disk
    vectordb = FAISS.from_documents(data, embeddings)
    vectordb.save_local(embeddings_file_path)
    main_placeholder.text("Building and saving new embeddings")

# Define prompt template for question answering
prompt_template = """ Given the following context and a question, generate an answer based on this context similar to a human reply. If the answer is not found in the context, kindly state "I don't know". Dont try to make up an answer.

CONTEXT: {context}

QUESTION: {question}"""

prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

# Set up the retrieval chain for QA
chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectordb.as_retriever(),
    input_key="query",
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}
)

main_placeholder.text("Ready to answer")




