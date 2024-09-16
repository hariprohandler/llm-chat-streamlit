# 💬 Chat with PDF using OpenAI and LangChain

This is a Streamlit-based application that allows users to upload a PDF file and interact with its content using a language model. The app uses the OpenAI API to provide answers to user queries about the content of the uploaded PDF.

## Features

- **Upload PDFs**: Easily upload a PDF file to extract its content.
- **Embeddings**: The content of the PDF is split into chunks and converted into vector embeddings using the OpenAI Embeddings API and FAISS for fast semantic search.
- **Question-Answering**: Ask questions about the PDF content, and the app will provide answers based on the uploaded document.
- **Persistent Embeddings**: Embeddings are saved to disk for future use, reducing the need for recomputation.

## Stack

- **Streamlit**: Frontend and user interface.
- **LangChain**: For handling LLM and chain operations.
- **OpenAI API**: Provides the LLM embeddings and question-answering capabilities.
- **FAISS**: Efficient similarity search and vector storage.
- **PyPDF2**: For PDF text extraction.

## Setup Instructions

### Requirements

- Python 3.8+
- Required packages listed in `requirements.txt`.

### Install Dependencies

To install the necessary dependencies, run the following:

```bash
pip install -r requirements.txt
```

### API Keys

You need an OpenAI API key to use the OpenAI embeddings and LLM features. Create a `.env` file in the root directory and add your API key as follows:

```bash
OPENAI_API_KEY=your_openai_api_key
```

### Running the Application

To start the Streamlit application, run the following command in your terminal:

```bash
streamlit run app.py
```

This will open the app in your browser.

## Usage

1. **Upload a PDF**: Upload a PDF by clicking on the "Upload your PDF" button.
2. **Ask Questions**: Once the PDF is processed, type in your questions about the document, and the app will return relevant responses based on the document content.
3. **Embeddings**: If the PDF has been uploaded before, embeddings are loaded from disk to save time.
4. **Query Results**: The app performs semantic search to return the best matching sections of the document in response to your query.

## Files

- **app.py**: The main application code.
- **requirements.txt**: The list of required Python libraries.
- **.env**: This file stores environment variables like API keys.
- **README.md**: This documentation file.

## Example

1. Run the application.
2. Upload a PDF with content related to any topic, e.g., "Sample PDF."
3. Ask a question: "What is the main idea of the first chapter?"
4. Receive a response from the language model based on the extracted text.

## Requirements

```
langchain==0.0.154
PyPDF2==3.0.1
python-dotenv==1.0.0
streamlit==1.18.1
faiss-cpu==1.7.4
altair==4.0.0
streamlit-extras
openai==1.45.0
tiktoken==0.7.0
```

## Contributing

Feel free to submit pull requests if you would like to contribute to this project. Please ensure that your changes include appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

