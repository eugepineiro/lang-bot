import os, sys, warnings
import openai
from rag import *

warnings.simplefilter(action='ignore', category=FutureWarning)

openai.api_key = os.environ["OPENAI_API_KEY"]
USER_PROMPT = "is there a candidate specialized in artificial intelligence?"

if __name__ == '__main__':

    docs = get_docs()           # Load custom files
    chunks = split_text(docs)   # Split into chunks
    db = get_data_store(chunks) # Generate vectorstore

    #print(f"[LOG] {db.similarity_search(USER_PROMPT)}\n\n")

    print("Chatbot: Hi! I'm your Virtual Assistant. I can answer questions about HR Inc., what do you wanna know?\nChatbot: You can write 'bye' to end the conversation")

    user_input = ""
    while user_input != "bye":
        user_input = input("You: ")
        response = generate_response(db, user_input) # Get chatbot response to user prompt
        print(f"Chatbot: {response}")