import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def load_and_split_documents(chunk_size, chunk_overlap):
    # Load documents from the specified directory
    print("Loading documents...")
    loader = DirectoryLoader(
        path='./docs',
        glob="**/*",
        show_progress=False,
    )
    print("Documents loaded")

    # Create chunks from the loaded documents
    print("Creating chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    # Load and split the documents into chunks using the specified text splitter
    chunks = loader.load_and_split(
        text_splitter=text_splitter
    )
    print("Created", len(chunks), "chunks of data")
    return chunks

def main():
    # Set chunk size and overlap parameters
    chunk_size = 100
    chunk_overlap = 0

    # Load and split documents into chunks
    chunks = load_and_split_documents(chunk_size, chunk_overlap)

    # Create embeddings using HuggingFace model
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create a FAISS vector store from the document chunks and save it locally
    vectorstore = FAISS.from_documents(documents=chunks, embedding=embeddings)
    vectorstore.save_local("faiss_vector_db")
    print("Success! Vector Store has been created!")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()