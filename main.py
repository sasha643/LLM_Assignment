import streamlit as st
from langchain.llms import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

def main():
    # Set the title of the Streamlit app
    st.title("The 48 laws of Power")

    # Initialize Hugging Face Embeddings and FAISS Vector Store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.load_local("faiss_vector_db", embeddings=embeddings)

    # Configure Hugging Face Hub for model retrieval
    repo_id = "tiiuae/falcon-7b-instruct"
    llm = HuggingFaceHub(
        repo_id=repo_id,
        model_kwargs={
            "temperature": 0.1,
            "max_new_tokens": 85,
        },
        huggingfacehub_api_token='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'
    )

    # Create RetrievalQA object
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(),
        return_source_documents=True
    )

    # Define exit conditions for the application
    exit_conditions = (":q", "quit", "exit")

    # Create a form in the Streamlit app
    with st.form(key='my_form'):
        # Add a text input for user to type their question
        user_input = st.text_input("Type your question")

        # Use the form submission event to handle both button click and Enter key press
        submitted = st.form_submit_button(label='Submit')

        # Check if the form is submitted or if the user input is not an exit condition
        if submitted or (user_input and user_input not in exit_conditions):
            # Perform question answering using the RetrievalQA model
            result = qa(user_input)

            # Display a separator line
            st.write("-" * 60)

            # Display relevant information about the source documents
            for index, doc in enumerate(result["source_documents"], start=1):
                # Display relevant information about the documents
                # Add your logic for displaying information about source documents here
                ''
            # Display the result of the question answering
            st.write(result["result"])

if __name__ == "__main__":
    main()
