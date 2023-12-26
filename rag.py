from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI, HuggingFaceHub
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# ------------- Retrieval-Augmented Generation  ------------- #

def get_docs():
    """
    Loads each file into one document, like knowledge base
    :return: docs
    """

    loader = DirectoryLoader("data", "*.txt", loader_cls=TextLoader)  # Reads custom data from local files

    docs = loader.load()
    return docs

def split_text(docs):
    """
    Get chunks from docs. Our loaded doc may be too long for most models, and even if it fits is can struggle to find relevant context. So we generate chunks
    :param docs: docs to be split
    :return: chunks
    """

    text_splitter = RecursiveCharacterTextSplitter( # recommended splitter for generic text
        chunk_size=2000,
        chunk_overlap=200,
        add_start_index=True
    )
    chunks = text_splitter.split_documents(docs)
    print(f"[LOG] Split {len(docs)} documents into {len(chunks)} chunks.")
    return chunks

def get_data_store(chunks):
    """
    Store chunks into a db. ChromaDB uses vector embeddings as the key, creates a new DB from the documents
    :param docs:
    :param chunks:
    :return: database
    """
    embeddings = HuggingFaceEmbeddings( #  embedding=OpenAIEmbeddings() rate limit
        model_name='sentence-transformers/all-MiniLM-L6-v2',
        model_kwargs={'device': 'cpu'}
    )

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )
    return db

def generate_response(db, prompt):
    """
    Generate a response with a LLM based on previous custom context
    :return: chatbot response
    """

    #openai_llm = ChatOpenAI(model_name="gpt-3.5-turbo") has very low rate limit
    hf_llm = HuggingFaceHub( # Generate LLM
        repo_id="HuggingFaceH4/zephyr-7b-beta",
        task="text-generation",
        model_kwargs={
            "max_new_tokens": 512,
            "top_k": 30,
            "temperature": 0.1,
            "repetition_penalty": 1.03,
        },
    )

    chain = RetrievalQA.from_chain_type( # Generate chat model based on previous llm
        llm=hf_llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_type="similarity", search_kwargs={"k": 6}),
        verbose=False
    )

    response = chain.run(prompt)
    return response
