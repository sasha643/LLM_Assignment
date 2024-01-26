# LangChain Vector Database

LangChain Vector Database is a tool for creating a vector database from textual documents and performing retrieval-based question answering using Streamlit. This repository consists of two main scripts: `upload.py` for creating the vector database, and `main.py` for running a Streamlit app to perform question answering.

## Requirements
- Python 3.6 or later
- [Streamlit](https://streamlit.io/)
- [LangChain](https://github.com/langchain/langchain)
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

### 1. Creating the Vector Database

Run the `upload.py` script to create the vector database:

```bash
python upload.py
