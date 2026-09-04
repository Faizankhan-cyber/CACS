import streamlit as st
from datetime import datetime

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# App Title
# -----------------------------

st.title("🤖 AI Chatbot")
st.caption("A simple chatbot built with Python and Streamlit")

# -----------------------------
# Chat History
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:
    st.header("⚙️ Settings")

    st.write("### About")
    st.write(
        "This is a simple rule-based chatbot "
        "created using Python and Streamlit."
    )

    st.write("### Features")
    st.write("• Chat interface")
    st.write("• Chat history")
    st.write("• Multiple responses")
    st.write("• Clear chat option")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -----------------------------
# Display Previous Messages
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

        if "time" in message:
            st.caption(message["time"])

# -----------------------------
# Chat Input
# -----------------------------

user_input = st.chat_input("💬 Type your message...")

if user_input:

    # Current time
    current_time = datetime.now().strftime("%I:%M %p")

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
        st.caption(current_time)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "time": current_time
    })

    # Convert message to lowercase
    message = user_input.lower().strip()

    # -----------------------------
    # Chatbot Responses
    # -----------------------------

    if message in ["hello", "hi", "hey", "hii", "helo"]:
        response = (
            "Hello! 👋 Nice to meet you! "
            "How can I help you today?"
        )

    elif "how are you" in message:
        response = (
            "I'm doing great! 🤖 "
            "Thanks for asking. How are you doing?"
        )

    elif "your name" in message:
        response = (
            "I'm AI Chatbot 🤖. "
            "I was built using Python and Streamlit."
        )

    elif "who are you" in message:
        response = (
            "I'm a simple rule-based chatbot. "
            "I can understand certain messages and respond to them."
        )

    elif "who created you" in message or "who made you" in message:
        response = (
            "I was created by a developer using "
            "Python and Streamlit. 💻"
        )

    elif "what can you do" in message:
        response = (
            "I can have simple conversations, answer basic questions, "
            "talk about Python and Streamlit, and respond to common messages."
        )

    elif "python" in message:
        response = (
            "Python 🐍 is a popular programming language. "
            "It is easy to learn and is used for web development, "
            "automation, data science, AI, and many other things."
        )

    elif "streamlit" in message:
        response = (
            "Streamlit is a Python framework that lets you "
            "quickly create interactive web applications."
        )

    elif "coding" in message or "programming" in message:
        response = (
            "Programming means writing instructions that tell "
            "a computer what to do. 💻"
        )

    elif "ai" in message or "artificial intelligence" in message:
        response = (
            "Artificial Intelligence, or AI, allows computers "
            "to perform tasks that normally require human intelligence."
        )

    elif "cloud" in message:
        response = (
            "Cloud computing allows you to use computing resources "
            "such as servers, storage, and databases over the internet. ☁️"
        )

    elif "cybersecurity" in message or "cyber security" in message:
        response = (
            "Cybersecurity is the practice of protecting computers, "
            "networks, applications, and data from cyber threats. 🔐"
        )

    elif "thank you" in message or "thanks" in message:
        response = (
            "You're welcome! 😊 "
            "I'm always happy to help."
        )

    elif "help" in message:
        response = (
            "Sure! 😊 You can ask me about Python, Streamlit, "
            "AI, cloud computing, cybersecurity, or programming."
        )

    elif message in ["bye", "goodbye", "see you"]:
        response = (
            "Goodbye! 👋 "
            "Thanks for chatting with me. Have a great day!"
        )

    else:
        response = (
            "I'm still learning! 🤔 "
            "I don't understand that question yet. "
            "Try asking me about Python, Streamlit, AI, "
            "cloud computing, or cybersecurity."
        )

    # -----------------------------
    # Display Bot Response
    # -----------------------------

    with st.chat_message("assistant"):
        st.write(response)
        st.caption(current_time)

    # Save bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "time": current_time
    })
