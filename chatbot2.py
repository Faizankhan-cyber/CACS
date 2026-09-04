import streamlit as st

# Page settings
st.set_page_config(
    page_title="My Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 My Chatbot")
st.write("Hello! I'm a simple chatbot. Ask me something below!")

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:

    # Display user's message
    st.chat_message("user").write(user_input)

    # Convert message to lowercase
    message = user_input.lower().strip()

    # Greetings
    if message in ["hello", "hi", "hey", "hii", "helo"]:
        response = "Hello! 👋 Nice to meet you. How can I help you today?"

    # How are you
    elif message in ["how are you", "how are you?"]:
        response = "I'm doing great! 🤖 Thanks for asking. How are you?"

    # Name
    elif message in ["what is your name?", "what's your name?", "your name?"]:
        response = "I'm My Chatbot 🤖, a chatbot built using Python and Streamlit."

    # Creator
    elif message in ["who created you?", "who made you?", "who is your creator?"]:
        response = "I was created by a developer using Python and Streamlit!"

    # Capabilities
    elif message in ["what can you do?", "what do you do?"]:
        response = (
            "I can have simple conversations, answer predefined questions, "
            "respond to greetings, and handle basic messages."
        )

    # Python
    elif "python" in message:
        response = (
            "Python is a popular programming language known for being "
            "simple, powerful, and beginner-friendly. 🐍"
        )

    # Streamlit
    elif "streamlit" in message:
        response = (
            "Streamlit is a Python framework that makes it easy to build "
            "interactive web apps without needing to learn HTML, CSS, or JavaScript."
        )

    # Programming
    elif "programming" in message or "coding" in message:
        response = (
            "Programming is the process of giving instructions to a computer "
            "so it can perform specific tasks. 💻"
        )

    # College
    elif "college" in message:
        response = (
            "College is a great place to learn, build projects, make friends, "
            "and occasionally wonder why assignments exist. 😄"
        )

    # Thanks
    elif "thank you" in message or "thanks" in message:
        response = "You're welcome! 😊 I'm happy to help."

    # Help
    elif message in ["help", "i need help", "can you help me?"]:
        response = (
            "Sure! 😊 Ask me about Python, Streamlit, programming, "
            "or just start a conversation."
        )

    # Goodbye
    elif message in ["bye", "goodbye", "see you", "see you later"]:
        response = "Goodbye! 👋 Have a great day!"

    # Default response
    else:
        response = (
            "Hmm, I don't have an answer for that yet. 🤔 "
            "Try asking me about Python, Streamlit, programming, "
            "or one of the things I know!"
        )

    # Display chatbot response
    st.chat_message("assistant").write(response)
