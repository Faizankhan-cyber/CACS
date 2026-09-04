import streamlit as st
import time
from datetime import datetime


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Bren's Jarvis",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# DARK THEME + CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* =========================
       MAIN APP
    ========================= */

    .stApp {
        background-color: #080b10;
        color: #ffffff;
    }

    .block-container {
        max-width: 1000px;
        padding-top: 35px;
        padding-bottom: 120px;
    }


    /* =========================
       SIDEBAR
    ========================= */

    section[data-testid="stSidebar"] {
        background-color: #0b0f15;
        border-right: 1px solid #1d2430;
    }

    section[data-testid="stSidebar"] * {
        color: #e5e7eb;
    }

    .sidebar-logo {
        text-align: center;
        padding: 10px 0 20px;
    }

    .sidebar-logo .icon {
        font-size: 45px;
    }

    .sidebar-logo h2 {
        margin: 5px 0;
        color: #ffffff;
    }

    .sidebar-logo p {
        color: #7d8795;
        font-size: 13px;
    }


    /* =========================
       HEADER
    ========================= */

    .hero {
        text-align: center;
        padding: 15px 0 30px;
    }

    .hero-icon {
        font-size: 55px;
        margin-bottom: 5px;
    }

    .hero-title {
        font-size: 44px;
        font-weight: 700;
        color: #ffffff;
        margin: 0;
    }

    .hero-subtitle {
        color: #8b95a3;
        font-size: 16px;
        margin-top: 8px;
    }


    /* =========================
       ONLINE STATUS
    ========================= */

    .status {
        display: inline-block;
        margin-top: 15px;
        padding: 6px 14px;
        border-radius: 20px;
        background-color: #0d2117;
        border: 1px solid #174d2d;
        color: #4ade80;
        font-size: 13px;
    }


    /* =========================
       WELCOME CARD
    ========================= */

    .welcome {
        background-color: #0f141b;
        border: 1px solid #202936;
        border-radius: 18px;
        padding: 30px;
        text-align: center;
        margin-bottom: 25px;
    }

    .welcome-icon {
        font-size: 38px;
    }

    .welcome h2 {
        color: #ffffff;
        margin: 10px 0;
    }

    .welcome p {
        color: #8993a1;
        margin: 0;
    }


    /* =========================
       CHAT MESSAGES
    ========================= */

    [data-testid="stChatMessage"] {
        background-color: #0f141b;
        border: 1px solid #202936;
        border-radius: 16px;
        padding: 16px;
        margin-bottom: 12px;
    }


    /* =========================
       CHAT INPUT
    ========================= */

    [data-testid="stChatInput"] {
        background-color: #080b10;
    }

    [data-testid="stChatInput"] textarea {
        background-color: #111720 !important;
        color: #ffffff !important;
        border: 1px solid #293342 !important;
        border-radius: 14px !important;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: #697586 !important;
    }


    /* =========================
       BUTTONS
    ========================= */

    .stButton > button {
        background-color: #10161e;
        color: #d8dee8;
        border: 1px solid #27303d;
        border-radius: 11px;
        min-height: 42px;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background-color: #171e28;
        color: #ffffff;
        border-color: #485466;
    }


    /* =========================
       METRICS
    ========================= */

    [data-testid="stMetric"] {
        background-color: #10161e;
        border: 1px solid #202936;
        border-radius: 12px;
        padding: 12px;
    }


    /* =========================
       DIVIDER
    ========================= */

    hr {
        border-color: #202630;
    }


    /* =========================
       FOOTER
    ========================= */

    .footer {
        text-align: center;
        color: #4f5967;
        font-size: 12px;
        margin-top: 40px;
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
                "Good to see you, sir. 👋\n\n"
                "I am **Bren's Jarvis**, your personal virtual assistant. "
                "I am ready to help you with Python, AI, cybersecurity, "
                "cloud computing, Linux, Azure and programming."
            ),
            "time": datetime.now().strftime("%I:%M %p")
        }
    ]


# =========================================================
# CHATBOT BRAIN
# =========================================================

def get_response(message):

    message = message.lower().strip()


    # -----------------------------------------------------
    # GREETINGS
    # -----------------------------------------------------

    if message in [
        "hello",
        "hi",
        "hey",
        "hii",
        "helo",
        "good morning",
        "good afternoon",
        "good evening"
    ]:

        return (
            "Good to see you, sir. 👋\n\n"
            "Bren's Jarvis is online and ready to assist you."
        )


    # -----------------------------------------------------
    # HOW ARE YOU
    # -----------------------------------------------------

    if "how are you" in message:

        return (
            "I'm functioning perfectly, sir. 🤖\n\n"
            "All systems are operational and I'm ready to help."
        )


    # -----------------------------------------------------
    # NAME
    # -----------------------------------------------------

    if (
        "your name" in message
        or "who are you" in message
        or "what are you" in message
    ):

        return (
            "I am **Bren's Jarvis** 🤖.\n\n"
            "I'm a simple virtual assistant built using "
            "**Python and Streamlit**."
        )


    # -----------------------------------------------------
    # CREATOR
    # -----------------------------------------------------

    if (
        "who made you" in message
        or "who created you" in message
        or "who built you" in message
    ):

        return (
            "I was built using Python and Streamlit. 💻\n\n"
            "My current version uses predefined responses "
            "rather than a real AI model."
        )


    # -----------------------------------------------------
    # CAPABILITIES
    # -----------------------------------------------------

    if (
        "what can you do" in message
        or "what do you do" in message
        or "your capabilities" in message
    ):

        return (
            "I can currently help you with:\n\n"
            "🐍 **Python**\n"
            "🤖 **Artificial Intelligence**\n"
            "🔐 **Cybersecurity**\n"
            "☁️ **Cloud Computing**\n"
            "🔷 **Microsoft Azure**\n"
            "🐧 **Linux**\n"
            "🗄️ **Databases**\n"
            "🌐 **Web Development**\n"
            "💻 **Programming**"
        )


    # -----------------------------------------------------
    # PYTHON
    # -----------------------------------------------------

    if "python" in message:

        return (
            "🐍 **Python** is a popular programming language "
            "known for its simple and readable syntax.\n\n"
            "**Python is commonly used for:**\n\n"
            "• Web development\n"
            "• Automation\n"
            "• Artificial Intelligence\n"
            "• Machine learning\n"
            "• Data science\n"
            "• Cybersecurity\n"
            "• Scripting"
        )


    # -----------------------------------------------------
    # STREAMLIT
    # -----------------------------------------------------

    if "streamlit" in message:

        return (
            "🎈 **Streamlit** is a Python framework used to "
            "create interactive web applications.\n\n"
            "It allows developers to build useful web apps "
            "using Python without having to manually create "
            "a complete frontend."
        )


    # -----------------------------------------------------
    # ARTIFICIAL INTELLIGENCE
    # -----------------------------------------------------

    if (
        "artificial intelligence" in message
        or "what is ai" in message
        or message == "ai"
    ):

        return (
            "🤖 **Artificial Intelligence (AI)** is technology "
            "that allows computers to perform tasks that normally "
            "require human intelligence.\n\n"
            "**Examples include:**\n\n"
            "• Chatbots\n"
            "• Voice assistants\n"
            "• Image recognition\n"
            "• Recommendation systems\n"
            "• Generative AI\n"
            "• Machine learning"
        )


    # -----------------------------------------------------
    # CYBERSECURITY
    # -----------------------------------------------------

    if (
        "cybersecurity" in message
        or "cyber security" in message
        or "cyber threat" in message
    ):

        return (
            "🔐 **Cybersecurity** is the practice of protecting "
            "computers, networks, applications and data from "
            "cyber threats.\n\n"
            "**Common threats include:**\n\n"
            "• Phishing\n"
            "• Malware\n"
            "• Ransomware\n"
            "• Password attacks\n"
            "• Social engineering\n"
            "• Data breaches"
        )


    # -----------------------------------------------------
    # CLOUD COMPUTING
    # -----------------------------------------------------

    if (
        "cloud computing" in message
        or "what is cloud" in message
        or message == "cloud"
    ):

        return (
            "☁️ **Cloud computing** means using computing "
            "resources over the internet instead of relying "
            "only on your own computer.\n\n"
            "**Examples:**\n\n"
            "• Virtual machines\n"
            "• Cloud storage\n"
            "• Databases\n"
            "• Networking\n"
            "• Cloud security\n"
            "• Cloud applications\n\n"
            "Popular platforms include **Microsoft Azure, "
            "AWS and Google Cloud**."
        )


    # -----------------------------------------------------
    # AZURE
    # -----------------------------------------------------

    if "azure" in message:

        return (
            "🔷 **Microsoft Azure** is Microsoft's cloud "
            "computing platform.\n\n"
            "Azure provides services for:\n\n"
            "• Virtual machines\n"
            "• Storage\n"
            "• Networking\n"
            "• Databases\n"
            "• Security\n"
            "• Artificial Intelligence\n"
            "• Monitoring"
        )


    # -----------------------------------------------------
    # LINUX
    # -----------------------------------------------------

    if "linux" in message:

        return (
            "🐧 **Linux** is an open-source operating system "
            "widely used in servers, cloud environments, "
            "software development and cybersecurity.\n\n"
            "Popular distributions include **Ubuntu, Debian, "
            "Fedora and Kali Linux**."
        )


    # -----------------------------------------------------
    # DATABASE
    # -----------------------------------------------------

    if (
        "database" in message
        or "dbms" in message
    ):

        return (
            "🗄️ A **database** is used to store and organize "
            "data so it can be easily accessed and managed.\n\n"
            "**Examples:**\n\n"
            "• MySQL\n"
            "• PostgreSQL\n"
            "• SQLite\n"
            "• Microsoft SQL Server"
        )


    # -----------------------------------------------------
    # WEB DEVELOPMENT
    # -----------------------------------------------------

    if (
        "web development" in message
        or "website" in message
        or "web development" in message
    ):

        return (
            "🌐 **Web development** is the process of creating "
            "websites and web applications.\n\n"
            "**Common technologies:**\n\n"
            "• HTML\n"
            "• CSS\n"
            "• JavaScript\n"
            "• Python\n"
            "• Flask\n"
            "• Django"
        )


    # -----------------------------------------------------
    # PROGRAMMING
    # -----------------------------------------------------

    if (
        "programming" in message
        or "coding" in message
    ):

        return (
            "💻 **Programming** is the process of writing "
            "instructions that tell a computer what to do.\n\n"
            "Popular programming languages include **Python, "
            "Java, JavaScript, C, C++ and C#**."
        )


    # -----------------------------------------------------
    # THANK YOU
    # -----------------------------------------------------

    if (
        "thank you" in message
        or "thanks" in message
        or "thank" in message
    ):

        return (
            "You're welcome, sir. 😊\n\n"
            "Always happy to assist."
        )


    # -----------------------------------------------------
    # HELP
    # -----------------------------------------------------

    if message == "help":

        return (
            "Certainly, sir. Here are some things you can ask me:\n\n"
            "🐍 What is Python?\n"
            "🤖 What is AI?\n"
            "🔐 What is cybersecurity?\n"
            "☁️ What is cloud computing?\n"
            "🔷 What is Azure?\n"
            "🐧 What is Linux?\n"
            "🗄️ What is a database?\n"
            "🌐 What is web development?"
        )


    # -----------------------------------------------------
    # GOODBYE
    # -----------------------------------------------------

    if message in [
        "bye",
        "goodbye",
        "see you",
        "see you later"
    ]:

        return (
            "Goodbye, sir. 👋\n\n"
            "Bren's Jarvis will be here when you return."
        )


    # -----------------------------------------------------
    # DEFAULT RESPONSE
    # -----------------------------------------------------

    return (
        "I'm afraid I don't have an answer for that yet, sir. 🤔\n\n"
        "You can ask me about **Python, AI, cybersecurity, "
        "cloud computing, Azure, Linux, databases, "
        "web development or programming**."
    )


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-logo">

        <div class="icon">🤖</div>

        <h2>Bren's Jarvis</h2>

        <p>Your personal virtual assistant</p>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### 📊 Conversation")

    user_count = sum(
        1
        for message in st.session_state.messages
        if message["role"] == "user"
    )

    bot_count = sum(
        1
        for message in st.session_state.messages
        if message["role"] == "assistant"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("You", user_count)

    with col2:
        st.metric("Jarvis", bot_count)

    st.divider()

    st.markdown("### 🧠 Knowledge")

    st.write("🐍 Python")
    st.write("🤖 Artificial Intelligence")
    st.write("🔐 Cybersecurity")
    st.write("☁️ Cloud Computing")
    st.write("🔷 Microsoft Azure")
    st.write("🐧 Linux")
    st.write("🗄️ Databases")
    st.write("🌐 Web Development")

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Conversation cleared, sir. 🧹\n\n"
                    "Bren's Jarvis is ready."
                ),
                "time": datetime.now().strftime("%I:%M %p")
            }
        ]

        st.rerun()

    st.divider()

    st.caption("🟢 JARVIS ONLINE")
    st.caption("Built with Python + Streamlit")


# =========================================================
# MAIN HEADER
# =========================================================

st.markdown("""
<div class="hero">

    <div class="hero-icon">
        🤖
    </div>

    <div class="hero-title">
        Bren's Jarvis
    </div>

    <div class="hero-subtitle">
        Just A Rather Very Intelligent System
    </div>

    <div class="status">
        ● Online
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# WELCOME SCREEN
# =========================================================

if len(st.session_state.messages) == 1:

    st.markdown("""
    <div class="welcome">

        <div class="welcome-icon">
            ⚡
        </div>

        <h2>
            Welcome, Sir.
        </h2>

        <p>
            Bren's Jarvis is online and ready to assist you.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 💡 Quick Questions")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        if st.button("🐍 Python"):

            st.session_state.quick_question = "What is Python?"
            st.rerun()

    with col2:

        if st.button("🤖 AI"):

            st.session_state.quick_question = "What is AI?"
            st.rerun()

    with col3:

        if st.button("🔐 Security"):

            st.session_state.quick_question = "What is cybersecurity?"
            st.rerun()

    with col4:

        if st.button("☁️ Cloud"):

            st.session_state.quick_question = "What is cloud computing?"
            st.rerun()


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        st.caption(message["time"])


# =========================================================
# GET USER INPUT
# =========================================================

if "quick_question" in st.session_state:

    user_input = st.session_state.quick_question

    del st.session_state.quick_question

else:

    user_input = st.chat_input(
        "Message Bren's Jarvis..."
    )


# =========================================================
# PROCESS USER MESSAGE
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


    # Generate response
    response = get_response(user_input)


    # Display Jarvis response
    with st.chat_message("assistant"):

        placeholder = st.empty()

        displayed_text = ""

        for word in response.split():

            displayed_text += word + " "

            placeholder.markdown(displayed_text)

            time.sleep(0.015)

        st.caption(current_time)


    # Save Jarvis response
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
    Bren's Jarvis • Python • Streamlit
</div>
""", unsafe_allow_html=True)
