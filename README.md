# LangChain Vector Database

LangChain Vector Database is a tool for creating a vector database from textual documents and performing retrieval-based question answering using Streamlit. This repository consists of two main scripts: `upload.py` for creating the vector database, and `main.py` for running a Streamlit app to perform question answering.

## Requirements
- Python 3.6 or later
- [Streamlit](https://streamlit.io/)
- [langchain](https://www.langchain.com/)
- [sentence_transformers](https://www.sbert.net/)
- [faiss-cpu](https://pypi.org/project/faiss-cpu/)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/sasha643/LLM_Assignment.git
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Download the LangChain library** from [https://github.com/langchain/langchain](https://github.com/langchain/langchain) and follow the installation instructions.

## Usage

### 1. Arranging documents

Put all you documents from which you need to create the knowledge base in the ./doc folder.

### 2. Creating the Vector Database

Run the `upload.py` script to create the vector database:

```bash
python upload.py
```
This script loads documents from the specified directory, splits them into chunks, and creates embeddings using the Hugging Face model. It then builds a FAISS vector store from the document chunks and saves it locally.

#### 3. Running the Streamlit App

Run the main.py script to launch the Streamlit app:

```bash
streamlit run main.py
```

This script initializes Hugging Face Embeddings, loads the FAISS vector store created in the previous step, and configures Hugging Face Hub for model retrieval. It then creates a Streamlit form for users to input questions and displays relevant information about source documents.

#### Configuration

- In upload.py, you can customize the directory path, chunk size, and overlap parameters for loading and splitting documents.

- In main.py, configure the model name, repository ID, and model parameters for Hugging Face embeddings and Hugging Face Hub retrieval.
