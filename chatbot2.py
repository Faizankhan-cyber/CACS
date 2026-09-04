import streamlit as st
import time
from datetime import datetime


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Bren's Jarvis",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* =========================
       GLOBAL
    ========================= */

    .stApp {
        background: #080b10;
        color: #ffffff;
    }

    .main .block-container {
        max-width: 950px;
        padding-top: 35px;
        padding-bottom: 120px;
    }


    /* =========================
       SIDEBAR
    ========================= */

    section[data-testid="stSidebar"] {
        background: #0b0f15;
        border-right: 1px solid #202630;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #ffffff;
    }


    /* =========================
       MAIN TITLE
    ========================= */

    .main-title {
        text-align: center;
        font-size: 44px;
        font-weight: 700;
        color: #ffffff;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .main-subtitle {
        text-align: center;
        color: #8b95a3;
        font-size: 16px;
        margin-bottom: 15px;
    }

    .online-text {
        text-align: center;
        color: #4ade80;
        font-size: 14px;
        margin-bottom: 30px;
    }


    /* =========================
       WELCOME BOX
    ========================= */

    .welcome-box {
        background: #10161e;
        border: 1px solid #242d39;
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        margin-bottom: 25px;
    }

    .welcome-box h2 {
        color: #ffffff;
        margin-bottom: 8px;
    }

    .welcome-box p {
        color: #8b95a3;
        margin: 0;
    }


    /* =========================
       CHAT MESSAGES
    ========================= */

    [data-testid="stChatMessage"] {
        background: #10161e;
        border: 1px solid #222b37;
        border-radius: 15px;
        margin-bottom: 12px;
    }


    /* =========================
       CHAT INPUT
    ========================= */

    [data-testid="stChatInput"] {
        background: #080b10;
    }

    [data-testid="stChatInput"] textarea {
        background-color: #111821 !important;
        color: white !important;
        border: 1px solid #303b49 !important;
        border-radius: 14px !important;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: #6b7583 !important;
    }


    /* =========================
       BUTTONS
    ========================= */

    .stButton button {
        background: #10161e;
        color: #d8dee8;
        border: 1px solid #293442;
        border-radius: 10px;
        min-height: 42px;
    }

    .stButton button:hover {
        background: #171e27;
        color: white;
        border-color: #4a5666;
    }


    /* =========================
       METRICS
    ========================= */

    [data-testid="stMetric"] {
        background: #10161e;
        border: 1px solid #242d39;
        border-radius: 12px;
        padding: 12px;
    }


    /* =========================
       DIVIDERS
    ========================= */

    hr {
        border-color: #202630;
    }


    /* =========================
       FOOTER
    ========================= */

    .footer {
        text-align: center;
        color: #505a68;
        font-size: 12px;
        margin-top: 35px;
        padding-bottom: 20px;
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
                "I am **Bren's Jarvis**, your personal virtual "
                "assistant. I am ready to assist you."
            ),
            "time": datetime.now().strftime("%I:%M %p")
        }
    ]


# =========================================================
# JARVIS RESPONSE SYSTEM
# =========================================================

def get_response(message):

    message = message.lower().strip()


    # Greetings
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
            "Bren's Jarvis is online and ready to assist."
        )


    # How are you
    if "how are you" in message:

        return (
            "I'm functioning perfectly, sir. 🤖\n\n"
            "All systems are operational."
        )


    # Name
    if (
        "your name" in message
        or "who are you" in message
        or "what are you" in message
    ):

        return (
            "I am **Bren's Jarvis** 🤖.\n\n"
            "I'm a virtual assistant built using "
            "**Python and Streamlit**."
        )


    # Creator
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


    # Capabilities
    if (
        "what can you do" in message
        or "what do you do" in message
        or "capabilities" in message
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


    # Python
    if "python" in message:

        return (
            "🐍 **Python** is a popular programming language "
            "known for its simple and readable syntax.\n\n"
            "**Python is used for:**\n\n"
            "• Web development\n"
            "• Automation\n"
            "• Artificial Intelligence\n"
            "• Machine learning\n"
            "• Data science\n"
            "• Cybersecurity\n"
            "• Scripting"
        )


    # Streamlit
    if "streamlit" in message:

        return (
            "🎈 **Streamlit** is a Python framework for building "
            "interactive web applications.\n\n"
            "It allows you to create web apps using Python "
            "without manually building an entire frontend."
        )


    # AI
    if (
        "artificial intelligence" in message
        or "what is ai" in message
        or message == "ai"
    ):

        return (
            "🤖 **Artificial Intelligence (AI)** is technology "
            "that allows computers to perform tasks that normally "
            "require human intelligence.\n\n"
            "**Examples:**\n\n"
            "• Chatbots\n"
            "• Voice assistants\n"
            "• Image recognition\n"
            "• Recommendation systems\n"
            "• Generative AI"
        )


    # Cybersecurity
    if (
        "cybersecurity" in message
        or "cyber security" in message
    ):

        return (
            "🔐 **Cybersecurity** is the practice of protecting "
            "systems, networks, applications and data from "
            "cyber threats.\n\n"
            "**Common threats:**\n\n"
            "• Phishing\n"
            "• Malware\n"
            "• Ransomware\n"
            "• Password attacks\n"
            "• Social engineering"
        )


    # Cloud
    if (
        "cloud computing" in message
        or "what is cloud" in message
        or message == "cloud"
    ):

        return (
            "☁️ **Cloud computing** means using computing "
            "resources over the internet.\n\n"
            "**Examples:**\n\n"
            "• Virtual machines\n"
            "• Cloud storage\n"
            "• Databases\n"
            "• Networking\n"
            "• Security\n\n"
            "Popular platforms include Azure, AWS and "
            "Google Cloud."
        )


    # Azure
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


    # Linux
    if "linux" in message:

        return (
            "🐧 **Linux** is an open-source operating system "
            "widely used in servers, cloud computing, software "
            "development and cybersecurity.\n\n"
            "Popular distributions include Ubuntu, Debian, "
            "Fedora and Kali Linux."
        )


    # Database
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


    # Web development
    if (
        "web development" in message
        or "website" in message
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


    # Programming
    if (
        "programming" in message
        or "coding" in message
    ):

        return (
            "💻 **Programming** is the process of writing "
            "instructions that tell a computer what to do.\n\n"
            "Popular languages include Python, Java, "
            "JavaScript, C, C++ and C#."
        )


    # Thanks
    if (
        "thank you" in message
        or "thanks" in message
        or "thank" in message
    ):

        return (
            "You're welcome, sir. 😊\n\n"
            "Always happy to assist."
        )


    # Help
    if message == "help":

        return (
            "Certainly, sir. Here are some things you can ask:\n\n"
            "🐍 What is Python?\n"
            "🤖 What is AI?\n"
            "🔐 What is cybersecurity?\n"
            "☁️ What is cloud computing?\n"
            "🔷 What is Azure?\n"
            "🐧 What is Linux?\n"
            "🗄️ What is a database?"
        )


    # Goodbye
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


    # Default
    return (
        "I'm afraid I don't have an answer for that yet, sir. 🤔\n\n"
        "Try asking me about **Python, AI, cybersecurity, "
        "cloud computing, Azure, Linux, databases or programming**."
    )


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🤖 Bren's Jarvis")

    st.caption("Your personal virtual assistant")

    st.divider()

    st.subheader("📊 Conversation")

    user_count = sum(
        1
        for message in st.session_state.messages
        if message["role"] == "user"
    )

    jarvis_count = sum(
        1
        for message in st.session_state.messages
        if message["role"] == "assistant"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("You", user_count)

    with col2:
        st.metric("Jarvis", jarvis_count)

    st.divider()

    st.subheader("🧠 Knowledge")

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

    st.success("JARVIS ONLINE")

    st.caption("Built with Python + Streamlit")


# =========================================================
# MAIN HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🤖 Bren\'s Jarvis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'Just A Rather Very Intelligent System'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="online-text">● Online and ready to assist</div>',
    unsafe_allow_html=True
)


# =========================================================
# WELCOME SCREEN
# =========================================================

if len(st.session_state.messages) == 1:

    st.markdown("""
    <div class="welcome-box">

        <h2>⚡ Welcome, Sir.</h2>

        <p>
            Bren's Jarvis is online and ready to assist you.
            Ask a question below to begin.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.subheader("💡 Quick Questions")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        if st.button(
            "🐍 Python",
            use_container_width=True
        ):

            st.session_state.quick_question = "What is Python?"
            st.rerun()

    with col2:

        if st.button(
            "🤖 AI",
            use_container_width=True
        ):

            st.session_state.quick_question = "What is AI?"
            st.rerun()

    with col3:

        if st.button(
            "🔐 Security",
            use_container_width=True
        ):

            st.session_state.quick_question = "What is cybersecurity?"
            st.rerun()

    with col4:

        if st.button(
            "☁️ Cloud",
            use_container_width=True
        ):

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
# INPUT
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


    # Display response

    with st.chat_message("assistant"):

        placeholder = st.empty()

        displayed_text = ""

        for word in response.split():

            displayed_text += word + " "

            placeholder.markdown(displayed_text)

            time.sleep(0.015)

        st.caption(current_time)


    # Save response

    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "time": current_time
    })


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer">'
    'Bren\'s Jarvis • Python • Streamlit'
    '</div>',
    unsafe_allow_html=True
)
