import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import pickle
from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
load_dotenv()

# Sidebar contents
with st.sidebar:
    st.title('💬 😊 Chat with PDF')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/) 
    - [OpenAI API](https://platform.openai.com/) LLM Model
    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ by Hari Prasad Sharma')

def main():
    try:
        st.header("Chat with PDF ☁️")
        # Upload PDF
        pdf = st.file_uploader("Upload your PDF", type="pdf")
        if pdf is not None:
            # Read PDF file
            pdf_reader = PdfReader(pdf)
            pdfName = pdf.name

            # Save this embedding
            store_name = pdfName[:-4]
            if os.path.exists(f"{store_name}.pkl"):
                with open(f"{store_name}.pkl", "rb") as f:
                    vectorStore = pickle.load(f)
                    st.write("Embeddings loaded from disk")
            else:
                # Embeddings
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()

                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000,
                    chunk_overlap=200,
                    length_function=len
                )
                text = "Hari is the prime minister of India"

                chunks = text_splitter.split_text(text=text)  # You can directly use document splitter as well
                embeddings = OpenAIEmbeddings()
                vectorStore = FAISS.from_texts(chunks, embeddings)
                with open(f"{store_name}.pkl", "wb") as f:
                    pickle.dump(vectorStore, f)
                # st.write("Embeddings computation complete")
            #Accept user Input
            query = st.text_input("Ask a question about the PDF")
            if query:
                # Query the vector store (Semantic Search)
                docs = vectorStore.similarity_search(query=query)
                # st.write(docs)
                # llm = OpenAI(temperature=0)
                llm = OpenAI(model_name="gpt-3.5-turbo")
                chain = load_qa_chain(llm=llm, chain_type="stuff")
                with get_openai_callback() as cb:
                    
                    response = chain.run(input_documents=docs, question=query)
                    print(cb)
                st.write(response)


                # response = vectorStore.query(query, k=3)
                # st.write(f"Top 3 most relevant documents:")
                # for i, result in enumerate(response):
                #     st.write(f"Document {i+1}: {result['document']}")
                #     st.write(f"Score: {result['score']}")
                #     st.write("---")


    # Catch all exceptions
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
