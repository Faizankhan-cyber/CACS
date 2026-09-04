import streamlit as st
import time
from datetime import datetime


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Nova AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# DARK THEME + CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: #0b0f14;
        color: #f5f5f5;
    }

    /* Main content */
    .main .block-container {
        max-width: 1100px;
        padding-top: 35px;
        padding-bottom: 100px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #080b0f;
        border-right: 1px solid #20252d;
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 30px;
    }

    /* Header */
    .header {
        text-align: center;
        padding: 10px 0 30px 0;
    }

    .logo {
        font-size: 55px;
        margin-bottom: 5px;
    }

    .title {
        font-size: 42px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #8b949e;
        font-size: 16px;
    }

    /* Status */
    .status {
        display: inline-block;
        margin-top: 15px;
        padding: 6px 14px;
        border-radius: 20px;
        background: #102417;
        color: #4ade80;
        font-size: 13px;
        border: 1px solid #1d4d2b;
    }

    /* Welcome box */
    .welcome {
        background: #11161d;
        border: 1px solid #252c36;
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 25px;
        text-align: center;
    }

    .welcome h3 {
        color: #ffffff;
        margin-bottom: 8px;
    }

    .welcome p {
        color: #9ca3af;
        margin: 0;
    }

    /* Sidebar text */
    .side-title {
        color: #ffffff;
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 15px;
    }

    .side-text {
        color: #8b949e;
        font-size: 14px;
        line-height: 1.6;
    }

    /* Divider */
    .divider {
        height: 1px;
        background: #20252d;
        margin: 25px 0;
    }

    /* Chat messages */
    [data-testid="stChatMessage"] {
        background: #11161d;
        border: 1px solid #202630;
        border-radius: 14px;
        padding: 15px;
        margin-bottom: 12px;
    }

    /* Chat input */
    [data-testid="stChatInput"] {
        background: #11161d;
    }

    [data-testid="stChatInput"] textarea {
        background: #11161d !important;
        color: #ffffff !important;
        border: 1px solid #303743 !important;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: #6b7280 !important;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        background: #151a21;
        color: #d1d5db;
        border: 1px solid #2b323d;
        border-radius: 10px;
        padding: 10px;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background: #1c232d;
        border-color: #4b5563;
        color: #ffffff;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background: #11161d;
        border: 1px solid #242b35;
        padding: 12px;
        border-radius: 12px;
    }

    /* Caption */
    .stCaption {
        color: #6b7280 !important;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋 I'm Nova, your virtual assistant.\n\n"
                "Ask me about Python, AI, cybersecurity, "
                "cloud computing, Linux, Azure, or programming."
            ),
            "time": datetime.now().strftime("%I:%M %p")
        }
    ]


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="side-title">🤖 Nova AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="side-text">'
        'A simple chatbot built with Python and Streamlit.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown("### 📊 Chat Statistics")

    total_messages = len(st.session_state.messages)

    user_messages = sum(
        1 for message in st.session_state.messages
        if message["role"] == "user"
    )

    bot_messages = sum(
        1 for message in st.session_state.messages
        if message["role"] == "assistant"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("You", user_messages)

    with col2:
        st.metric("Nova", bot_messages)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown("### 💡 Topics")

    st.write("🐍 Python")
    st.write("🤖 Artificial Intelligence")
    st.write("🔐 Cybersecurity")
    st.write("☁️ Cloud Computing")
    st.write("🐧 Linux")
    st.write("🔷 Microsoft Azure")

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    if st.button("🗑️ Clear Conversation"):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Conversation cleared. 🧹\n\n"
                    "Hello again! How can I help you?"
                ),
                "time": datetime.now().strftime("%I:%M %p")
            }
        ]

        st.rerun()

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="side-text">'
        '🟢 Online<br>'
        'Version 1.0<br><br>'
        'Built with Python 🐍'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="header">

    <div class="logo">🤖</div>

    <div class="title">Nova AI</div>

    <div class="subtitle">
        Your simple Python-powered virtual assistant
    </div>

    <div class="status">
        ● Online
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# WELCOME MESSAGE
# =========================================================

if len(st.session_state.messages) == 1:

    st.markdown("""
    <div class="welcome">

        <h3>👋 Welcome to Nova AI</h3>

        <p>
        Ask a question below to start a conversation.
        </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# QUICK QUESTIONS
# =========================================================

if len(st.session_state.messages) == 1:

    st.markdown("### 💡 Try asking")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("🐍 What is Python?"):

            st.session_state.quick_question = "What is Python?"
            st.rerun()

    with col2:

        if st.button("🤖 What is AI?"):

            st.session_state.quick_question = "What is AI?"
            st.rerun()

    with col3:

        if st.button("🔐 What is Cybersecurity?"):

            st.session_state.quick_question = "What is cybersecurity?"
            st.rerun()


# =========================================================
# CHATBOT RESPONSE FUNCTION
# =========================================================

def get_response(message):

    message = message.lower().strip()


    # Greetings
    if any(word in message for word in
           ["hello", "hi", "hey", "hii", "helo"]):

        return (
            "Hello! 👋\n\n"
            "Nice to meet you! What would you like to learn about?"
        )


    # How are you
    elif "how are you" in message:

        return (
            "I'm doing great! 🤖\n\n"
            "I'm ready to answer your questions."
        )


    # Name
    elif "your name" in message or "who are you" in message:

        return (
            "I'm **Nova AI** 🤖.\n\n"
            "I'm a simple chatbot built using Python and Streamlit."
        )


    # Capabilities
    elif "what can you do" in message:

        return (
            "I can help with several basic topics:\n\n"
            "🐍 Python\n"
            "🤖 Artificial Intelligence\n"
            "🔐 Cybersecurity\n"
            "☁️ Cloud Computing\n"
            "🐧 Linux\n"
            "🔷 Microsoft Azure\n"
            "💻 Programming"
        )


    # Python
    elif "python" in message:

        return (
            "🐍 **Python** is a popular programming language "
            "that is simple to learn and very powerful.\n\n"
            "**Common uses:**\n"
            "• Web development\n"
            "• Automation\n"
            "• Data science\n"
            "• AI and machine learning\n"
            "• Cybersecurity\n"
            "• Scripting"
        )


    # Streamlit
    elif "streamlit" in message:

        return (
            "🎈 **Streamlit** is a Python framework used to create "
            "interactive web applications.\n\n"
            "It lets you build apps using Python without needing "
            "to write a full frontend from scratch."
        )


    # AI
    elif (
        "artificial intelligence" in message
        or "what is ai" in message
        or message == "ai"
    ):

        return (
            "🤖 **Artificial Intelligence (AI)** is technology that "
            "allows computers to perform tasks that normally require "
            "human intelligence.\n\n"
            "**Examples:**\n"
            "• Chatbots\n"
            "• Voice assistants\n"
            "• Image recognition\n"
            "• Recommendation systems\n"
            "• Generative AI"
        )


    # Cybersecurity
    elif (
        "cybersecurity" in message
        or "cyber security" in message
    ):

        return (
            "🔐 **Cybersecurity** is the practice of protecting "
            "computers, networks, applications, and data from "
            "cyber threats.\n\n"
            "**Common threats:**\n"
            "• Phishing\n"
            "• Malware\n"
            "• Ransomware\n"
            "• Password attacks\n"
            "• Social engineering"
        )


    # Cloud
    elif "cloud" in message:

        return (
            "☁️ **Cloud computing** means using computing resources "
            "such as servers, storage, and databases over the internet.\n\n"
            "**Popular cloud platforms:**\n"
            "• Microsoft Azure\n"
            "• Amazon Web Services\n"
            "• Google Cloud"
        )


    # Azure
    elif "azure" in message:

        return (
            "🔷 **Microsoft Azure** is Microsoft's cloud computing "
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


    # Linux
    elif "linux" in message:

        return (
            "🐧 **Linux** is an open-source operating system "
            "widely used for servers, cloud computing, development, "
            "and cybersecurity.\n\n"
            "Popular distributions include Ubuntu, Debian, Fedora, "
            "and Kali Linux."
        )


    # Programming
    elif "programming" in message or "coding" in message:

        return (
            "💻 **Programming** is the process of writing instructions "
            "that tell a computer what to do.\n\n"
            "Some popular programming languages are Python, Java, "
            "JavaScript, C, C++, and C#."
        )


    # Thanks
    elif "thank" in message:

        return (
            "You're welcome! 😊\n\n"
            "Happy to help."
        )


    # Goodbye
    elif message in ["bye", "goodbye", "see you", "see you later"]:

        return (
            "Goodbye! 👋\n\n"
            "Thanks for chatting with Nova AI!"
        )


    # Help
    elif message == "help":

        return (
            "Here are some things you can ask me:\n\n"
            "🐍 What is Python?\n"
            "🤖 What is AI?\n"
            "🔐 What is cybersecurity?\n"
            "☁️ What is cloud computing?\n"
            "🐧 What is Linux?\n"
            "🔷 What is Azure?\n"
            "💻 What is programming?"
        )


    # Default
    else:

        return (
            "🤔 I don't know the answer to that yet.\n\n"
            "Try asking me about **Python, AI, cybersecurity, "
            "cloud computing, Linux, Azure, or programming**."
        )


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        st.caption(message["time"])


# =========================================================
# HANDLE QUICK QUESTION
# =========================================================

if "quick_question" in st.session_state:

    user_input = st.session_state.quick_question

    del st.session_state.quick_question

else:

    user_input = st.chat_input(
        "💬 Message Nova AI..."
    )


# =========================================================
# PROCESS USER MESSAGE
# =========================================================

if user_input:

    current_time = datetime.now().strftime("%I:%M %p")


    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
            "time": current_time
        }
    )


    with st.chat_message("user"):

        st.markdown(user_input)
        st.caption(current_time)


    # Bot response
    response = get_response(user_input)


    with st.chat_message("assistant"):

        placeholder = st.empty()

        displayed_text = ""

        # Simple typing animation
        for word in response.split():

            displayed_text += word + " "

            placeholder.markdown(displayed_text)

            time.sleep(0.015)

        st.caption(current_time)


    # Save response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
            "time": current_time
        }
    )
