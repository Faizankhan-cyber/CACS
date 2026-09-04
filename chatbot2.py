import streamlit as st
from datetime import datetime
import time


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Nova AI",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)


# =========================================================
# DARK THEME CSS
# =========================================================

st.markdown("""
<style>

/* ================================
   MAIN APP
================================ */

.stApp {
    background-color: #0b0f14;
    color: #ffffff;
}

.main .block-container {
    max-width: 900px;
    padding-top: 40px;
    padding-bottom: 120px;
}


/* ================================
   SIDEBAR
================================ */

section[data-testid="stSidebar"] {
    background-color: #080b10;
    border-right: 1px solid #202630;
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb;
}


/* ================================
   TITLE
================================ */

.title-container {
    text-align: center;
    padding: 20px 0 30px 0;
}

.title-container h1 {
    font-size: 42px;
    margin: 0;
    color: #ffffff;
    font-weight: 700;
}

.title-container p {
    color: #8b949e;
    font-size: 16px;
    margin-top: 8px;
}


/* ================================
   ONLINE STATUS
================================ */

.online {
    display: inline-block;
    margin-top: 12px;
    padding: 6px 14px;
    border-radius: 20px;
    background-color: #102217;
    border: 1px solid #1d4d2b;
    color: #4ade80;
    font-size: 13px;
}


/* ================================
   WELCOME CARD
================================ */

.welcome-card {
    background-color: #11161d;
    border: 1px solid #242b35;
    border-radius: 16px;
    padding: 25px;
    text-align: center;
    margin-bottom: 25px;
}

.welcome-card h3 {
    margin: 0 0 8px 0;
    color: #ffffff;
}

.welcome-card p {
    margin: 0;
    color: #8b949e;
}


/* ================================
   CHAT MESSAGES
================================ */

[data-testid="stChatMessage"] {
    background-color: #11161d;
    border: 1px solid #242b35;
    border-radius: 14px;
    margin-bottom: 10px;
}


/* ================================
   CHAT INPUT
================================ */

[data-testid="stChatInput"] {
    background-color: #0b0f14;
}

[data-testid="stChatInput"] textarea {
    background-color: #11161d !important;
    color: #ffffff !important;
    border: 1px solid #303743 !important;
    border-radius: 12px !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #6b7280 !important;
}


/* ================================
   BUTTONS
================================ */

.stButton > button {
    width: 100%;
    background-color: #11161d;
    color: #d1d5db;
    border: 1px solid #2b323d;
    border-radius: 10px;
}

.stButton > button:hover {
    background-color: #1a2029;
    color: #ffffff;
    border-color: #4b5563;
}


/* ================================
   DIVIDER
================================ */

hr {
    border-color: #202630;
}


/* ================================
   METRICS
================================ */

[data-testid="stMetric"] {
    background-color: #11161d;
    border: 1px solid #242b35;
    border-radius: 12px;
}


/* ================================
   FOOTER
================================ */

.footer {
    text-align: center;
    color: #555e6b;
    font-size: 13px;
    margin-top: 30px;
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
                "Hello! 👋 I'm Nova AI.\n\n"
                "I can answer questions about Python, AI, "
                "cybersecurity, cloud computing, Linux, Azure "
                "and programming."
            ),
            "time": datetime.now().strftime("%I:%M %p")
        }
    ]


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🤖 Nova AI")

    st.caption("Simple Python-powered chatbot")

    st.divider()

    st.markdown("### 📊 Chat Statistics")

    user_count = sum(
        1 for message in st.session_state.messages
        if message["role"] == "user"
    )

    bot_count = sum(
        1 for message in st.session_state.messages
        if message["role"] == "assistant"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("You", user_count)

    with col2:
        st.metric("Nova", bot_count)

    st.divider()

    st.markdown("### 💡 Topics")

    st.write("🐍 Python")
    st.write("🤖 Artificial Intelligence")
    st.write("🔐 Cybersecurity")
    st.write("☁️ Cloud Computing")
    st.write("🐧 Linux")
    st.write("🔷 Microsoft Azure")

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Chat cleared! 🧹\n\n"
                    "How can I help you?"
                ),
                "time": datetime.now().strftime("%I:%M %p")
            }
        ]

        st.rerun()

    st.divider()

    st.caption("🟢 Online")
    st.caption("Built with Python + Streamlit")


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="title-container">

    <h1>🤖 Nova AI</h1>

    <p>
        Your simple Python-powered virtual assistant
    </p>

    <div class="online">
        ● Online
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# WELCOME CARD
# =========================================================

if len(st.session_state.messages) == 1:

    st.markdown("""
    <div class="welcome-card">

        <h3>👋 Welcome to Nova AI</h3>

        <p>
            Ask me something to start a conversation.
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
    if message in ["hello", "hi", "hey", "hii", "helo"]:

        return (
            "Hello! 👋\n\n"
            "Nice to meet you! How can I help you today?"
        )


    # How are you
    elif "how are you" in message:

        return (
            "I'm doing great! 🤖\n\n"
            "I'm ready to help you."
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
            "I can help you with:\n\n"
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
            "**Uses of Python:**\n"
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
            "🎈 **Streamlit** is a Python framework used to "
            "build interactive web applications.\n\n"
            "It allows you to create web apps using Python "
            "without building the entire frontend manually."
        )


    # AI
    elif (
        "artificial intelligence" in message
        or "what is ai" in message
        or message == "ai"
    ):

        return (
            "🤖 **Artificial Intelligence (AI)** is technology "
            "that allows computers to perform tasks that normally "
            "require human intelligence.\n\n"
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
            "systems, networks, applications and data from "
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
            "☁️ **Cloud computing** means using computing "
            "resources over the internet.\n\n"
            "Examples include:\n"
            "• Virtual machines\n"
            "• Cloud storage\n"
            "• Databases\n"
            "• Networking\n"
            "• Cloud security\n\n"
            "Popular platforms include Azure, AWS and Google Cloud."
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
            "widely used for servers, cloud computing, software "
            "development and cybersecurity."
        )


    # Programming
    elif "programming" in message or "coding" in message:

        return (
            "💻 **Programming** means writing instructions "
            "that tell a computer what to do.\n\n"
            "Popular languages include Python, Java, JavaScript, "
            "C, C++ and C#."
        )


    # Thanks
    elif "thank" in message:

        return (
            "You're welcome! 😊\n\n"
            "Happy to help."
        )


    # Goodbye
    elif message in ["bye", "goodbye", "see you"]:

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
            "cloud computing, Linux, Azure or programming**."
        )


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        st.caption(message["time"])


# =========================================================
# INPUT
# =========================================================

if "quick_question" in st.session_state:

    user_input = st.session_state.quick_question

    del st.session_state.quick_question

else:

    user_input = st.chat_input(
        "Message Nova AI..."
    )


# =========================================================
# PROCESS MESSAGE
# =========================================================

if user_input:

    current_time = datetime.now().strftime("%I:%M %p")


    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "time": current_time
    })


    # Display user message
    with st.chat_message("user"):

        st.markdown(user_input)
        st.caption(current_time)


    # Get response
    response = get_response(user_input)


    # Display bot response
    with st.chat_message("assistant"):

        placeholder = st.empty()

        displayed_text = ""

        for word in response.split():

            displayed_text += word + " "

            placeholder.markdown(displayed_text)

            time.sleep(0.015)

        st.caption(current_time)


    # Save bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "time": current_time
    })


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    Nova AI • Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)
