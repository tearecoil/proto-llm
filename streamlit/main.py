from openai import OpenAI
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
#from langchain_community.llms import OpenAI as llmopenai
#from langchain_openai import OpenAI as llmopenai
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain.chains import LLMChain, StuffDocumentsChain
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain.callbacks import get_openai_callback

import langchain
import pandas as pd
import streamlit as st 
import os
import getpass

# os.environ["OPENAI_API_KEY"] = getpass.getpass()
langchain.verbose = False

#load env variables
load_dotenv()
print(os.environ.get('OPENAI_API_KEY'))
#process text from PDF
def process_text(text):
    #split text into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size = 1500,
        chunk_overlap = 50,
        length_function = len
    )
    chunks = text_splitter.split_text(text)

    #convert chunks to embeddings
    embeddings = OpenAIEmbeddings(openai_api_key = os.environ.get('OPENAI_API_KEY'))
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    return knowledge_base

def main():
    st.title("OPENAI THEME - PROTOTYPE LLM")
    st.sidebar.title('Files Submitted')
    temperature = st.sidebar.slider("Temperature", min_value=0.0, 
                                    max_value=2.0, value=0.7, step=0.1)
    max_tokens = st.sidebar.slider("Max Tokens", min_value=1, 
                                    max_value=4096, value=256)
    pdf = st.sidebar.file_uploader("UPLOAD YOUR PDF FILE", type="pdf")
    if pdf:
        pdf_reader = PdfReader(pdf)
        #store the pdf text in a var
        text = ""

        for page in pdf_reader.pages:
            text += page.extract_text()
            #create knowledge base object
            knowledgeBase = process_text(text)

        query = st.text_input("Ask question to PDF...")
        cancel_button = st.button("Cancel")
        if cancel_button:
            st.stop()
        if query: 
            docs = knowledgeBase.similarity_search(query)
            llm = ChatOpenAI(os.getenv("OPENAI_API_KEY"), model = 'gpt-4o-mini')
            #llm = llmopenai(openai_api_key=os.getenv('OPENAI_API_KEY'))
            chain = load_qa_chain(llm, chain_type="stuff")

            with get_openai_callback() as cost:
                response = chain.invoke(input={"question": query, 
                                               "input_documents": docs})
                print(cost)
                st.write(response["output_text"])
                                    
if __name__ == "__main__":
    main()