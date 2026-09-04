import streamlit as st
import time
from datetime import datetime


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Smart Chatbot",
    page_icon="🤖",
    layout="centered"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }

    .welcome {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
    }

    .stChatMessage {
        border-radius: 12px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">🤖 Smart Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your simple Python-powered virtual assistant</div>',
    unsafe_allow_html=True
)


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋 I'm your Smart Chatbot.\n\n"
                "You can ask me about Python, AI, cloud computing, "
                "cybersecurity, programming, or just have a conversation!"
            ),
            "time": datetime.now().strftime("%I:%M %p")
        }
    ]


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("⚙️ Chatbot")

    st.write("### 📌 Features")

    st.write("💬 Interactive chat")
    st.write("🧠 Smart keyword matching")
    st.write("🕒 Message timestamps")
    st.write("⚡ Fast responses")
    st.write("🗑️ Clear conversation")

    st.divider()

    # Statistics
    st.write("### 📊 Chat Statistics")

    total_messages = len(st.session_state.messages)

    user_messages = sum(
        1 for message in st.session_state.messages
        if message["role"] == "user"
    )

    bot_messages = sum(
        1 for message in st.session_state.messages
        if message["role"] == "assistant"
    )

    st.metric("Total Messages", total_messages)
    st.metric("Your Messages", user_messages)
    st.metric("Bot Messages", bot_messages)

    st.divider()

    # Clear chat
    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Chat cleared! 🧹\n\n"
                    "Hello again! How can I help you?"
                ),
                "time": datetime.now().strftime("%I:%M %p")
            }
        ]

        st.rerun()


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

        st.caption(message["time"])


# =========================================================
# CHATBOT FUNCTION
# =========================================================

def get_response(message):

    message = message.lower().strip()


    # Greetings
    if any(word in message for word in
           ["hello", "hi", "hey", "hii", "helo"]):

        return (
            "Hello! 👋\n\n"
            "Nice to meet you! What would you like to talk about?"
        )


    # How are you
    elif "how are you" in message:

        return (
            "I'm doing great! 🤖\n\n"
            "Thanks for asking. I'm ready to help you with "
            "whatever you're working on."
        )


    # Name
    elif "your name" in message or "who are you" in message:

        return (
            "I'm **Smart Chatbot** 🤖.\n\n"
            "I'm a simple chatbot created using **Python and Streamlit**."
        )


    # Creator
    elif "who made you" in message or "who created you" in message:

        return (
            "I was created using Python and Streamlit. 💻\n\n"
            "My responses are currently based on predefined rules."
        )


    # Capabilities
    elif "what can you do" in message or "your features" in message:

        return (
            "I can currently:\n\n"
            "• 💬 Have simple conversations\n"
            "• 🐍 Explain basic Python concepts\n"
            "• 🤖 Explain AI concepts\n"
            "• ☁️ Talk about cloud computing\n"
            "• 🔐 Explain cybersecurity topics\n"
            "• 💻 Answer basic programming questions\n\n"
            "I'm still a simple chatbot, though. I haven't achieved "
            "world domination yet."
        )


    # Python
    elif "python" in message:

        return (
            "🐍 **Python** is a high-level programming language "
            "known for being simple and easy to learn.\n\n"
            "It is commonly used for:\n"
            "• Web development\n"
            "• Automation\n"
            "• Data science\n"
            "• Artificial Intelligence\n"
            "• Cybersecurity\n"
            "• Machine learning"
        )


    # Streamlit
    elif "streamlit" in message:

        return (
            "🎈 **Streamlit** is a Python framework used to create "
            "interactive web applications quickly.\n\n"
            "You can build apps using mostly Python without having "
            "to manually create a complete frontend."
        )


    # AI
    elif (
        "artificial intelligence" in message
        or "what is ai" in message
        or message == "ai"
        or " ai " in f" {message} "
    ):

        return (
            "🤖 **Artificial Intelligence (AI)** is technology that "
            "allows computers to perform tasks that normally require "
            "human intelligence.\n\n"
            "Examples include:\n"
            "• Chatbots\n"
            "• Image recognition\n"
            "• Voice assistants\n"
            "• Recommendation systems\n"
            "• Generative AI"
        )


    # Cybersecurity
    elif (
        "cybersecurity" in message
        or "cyber security" in message
        or "cyber threat" in message
    ):

        return (
            "🔐 **Cybersecurity** is the practice of protecting "
            "systems, networks, applications, and data from "
            "unauthorized access and cyber attacks.\n\n"
            "Common threats include:\n"
            "• Phishing\n"
            "• Malware\n"
            "• Ransomware\n"
            "• Password attacks\n"
            "• Social engineering"
        )


    # Cloud
    elif (
        "cloud computing" in message
        or "cloud" in message
    ):

        return (
            "☁️ **Cloud computing** means using computing resources "
            "over the internet instead of relying only on your own computer.\n\n"
            "Examples include:\n"
            "• Virtual machines\n"
            "• Cloud storage\n"
            "• Databases\n"
            "• Networking\n"
            "• Cloud security\n\n"
            "Popular cloud platforms include AWS, Microsoft Azure, "
            "and Google Cloud."
        )


    # Programming
    elif (
        "programming" in message
        or "coding" in message
    ):

        return (
            "💻 **Programming** means writing instructions that tell "
            "a computer what to do.\n\n"
            "Popular programming languages include Python, Java, "
            "JavaScript, C, C++, and C#."
        )


    # Linux
    elif "linux" in message:

        return (
            "🐧 **Linux** is an open-source operating system widely "
            "used on servers, cloud systems, cybersecurity labs, "
            "and development environments.\n\n"
            "Popular distributions include Ubuntu, Debian, Fedora, "
            "and Kali Linux."
        )


    # Azure
    elif "azure" in message:

        return (
            "☁️ **Microsoft Azure** is Microsoft's cloud computing "
            "platform.\n\n"
            "It provides services for:\n"
            "• Virtual machines\n"
            "• Storage\n"
            "• Networking\n"
            "• Databases\n"
            "• Security\n"
            "• AI\n"
            "• Monitoring"
        )


    # Thanks
    elif (
        "thank you" in message
        or "thanks" in message
    ):

        return (
            "You're welcome! 😊\n\n"
            "Happy to help."
        )


    # Help
    elif "help" in message:

        return (
            "Sure! 😊 Try asking me something like:\n\n"
            "• What is Python?\n"
            "• What is AI?\n"
            "• What is cybersecurity?\n"
            "• What is cloud computing?\n"
            "• What is Linux?\n"
            "• What is Azure?\n"
            "• What can you do?"
        )


    # Goodbye
    elif message in [
        "bye",
        "goodbye",
        "see you",
        "see you later"
    ]:

        return (
            "Goodbye! 👋\n\n"
            "Thanks for chatting with me. Have a great day!"
        )


    # Unknown question
    else:

        return (
            "🤔 I'm not sure how to answer that yet.\n\n"
            "Try asking me about **Python, AI, cybersecurity, "
            "cloud computing, Linux, Azure, programming**, "
            "or type **help** to see what I can do."
        )


# =========================================================
# USER INPUT
# =========================================================

user_input = st.chat_input(
    "💬 Ask me anything..."
)


if user_input:

    current_time = datetime.now().strftime("%I:%M %p")


    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
            "time": current_time
        }
    )


    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
        st.caption(current_time)


    # Generate response
    response = get_response(user_input)


    # Typing effect
    with st.chat_message("assistant"):

        message_placeholder = st.empty()

        displayed_text = ""

        for word in response.split():

            displayed_text += word + " "

            message_placeholder.markdown(displayed_text)

            time.sleep(0.02)

        st.caption(current_time)


    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
            "time": current_time
        }
    )
