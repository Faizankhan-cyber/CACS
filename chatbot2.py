import streamlit as st
from datetime import datetime


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Bren's Jarvis",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
   GLOBAL
   ========================================================= */

* {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    padding: 0;
}

.stApp {
    background: #070a0f;
    color: #f5f7fa;
}

.block-container {
    max-width: 1180px;
    padding-top: 25px !important;
    padding-bottom: 100px !important;
}


/* =========================================================
   HIDE STREAMLIT BRANDING
   ========================================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {
    background: #0b0f15 !important;
    border-right: 1px solid #1d2631;
}

section[data-testid="stSidebar"] > div {
    padding-top: 25px;
}

.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 4px;
}

.sidebar-logo-icon {
    font-size: 28px;
}

.sidebar-title {
    font-size: 21px;
    font-weight: 700;
    color: #ffffff;
}

.sidebar-subtitle {
    color: #7f8997;
    font-size: 13px;
    margin-bottom: 25px;
}

.sidebar-section {
    color: #f1f5f9;
    font-size: 15px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 12px;
}


/* =========================================================
   MAIN HEADER
   ========================================================= */

.hero {
    text-align: center;
    padding: 10px 10px 25px;
}

.hero-icon {
    font-size: 44px;
    margin-bottom: 2px;
}

.hero-title {
    font-size: 42px;
    font-weight: 750;
    letter-spacing: -1px;
    color: #ffffff;
    line-height: 1.15;
}

.hero-subtitle {
    color: #8b96a5;
    font-size: 15px;
    margin-top: 9px;
}

.online-status {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    margin-top: 13px;
    padding: 6px 12px;
    border-radius: 30px;
    background: #0c2117;
    border: 1px solid #164b2d;
    color: #4ade80;
    font-size: 12px;
}


/* =========================================================
   WELCOME CARD
   ========================================================= */

.welcome-card {
    background: linear-gradient(
        145deg,
        #111821,
        #0d131a
    );

    border: 1px solid #25303d;
    border-radius: 20px;
    padding: 34px 30px;
    text-align: center;
    margin-bottom: 28px;
}

.welcome-icon {
    font-size: 38px;
    margin-bottom: 8px;
}

.welcome-title {
    font-size: 27px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 10px;
}

.welcome-text {
    color: #8c97a6;
    font-size: 15px;
    line-height: 1.6;
}

.welcome-text strong {
    color: #dce3ec;
}


/* =========================================================
   QUICK ACTIONS
   ========================================================= */

.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 14px;
}

.action-card {
    background: #0f151d;
    border: 1px solid #242e3a;
    border-radius: 15px;
    padding: 18px;
    text-align: center;
    min-height: 115px;
}

.action-icon {
    font-size: 27px;
    margin-bottom: 7px;
}

.action-title {
    color: #f1f5f9;
    font-size: 14px;
    font-weight: 600;
}

.action-description {
    color: #727e8d;
    font-size: 11px;
    margin-top: 5px;
}


/* =========================================================
   BUTTONS
   ========================================================= */

.stButton > button {
    width: 100%;
    background: #101720 !important;
    color: #e5eaf0 !important;
    border: 1px solid #273341 !important;
    border-radius: 11px !important;
    min-height: 44px !important;
    font-size: 13px !important;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: #18212c !important;
    border-color: #435264 !important;
    color: #ffffff !important;
}


/* =========================================================
   CHAT
   ========================================================= */

.chat-container {
    margin-top: 30px;
}

.chat-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 13px;
}

.chat-title {
    font-size: 22px;
    font-weight: 700;
    color: #ffffff;
}

.chat-subtitle {
    color: #697586;
    font-size: 12px;
}


/* Chat messages */

[data-testid="stChatMessage"] {
    background: #10161e !important;
    border: 1px solid #222d39 !important;
    border-radius: 15px !important;
    margin-bottom: 10px !important;
    padding: 12px 15px !important;
}


/* User messages */

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-user"]
) {
    background: #111923 !important;
}


/* =========================================================
   CHAT INPUT
   ========================================================= */

[data-testid="stChatInput"] {
    background: transparent !important;
    border-top: none !important;
}

[data-testid="stChatInput"] > div {
    background: #0f151d !important;
    border: 1px solid #2a3542 !important;
    border-radius: 16px !important;
}

[data-testid="stChatInput"] textarea {
    background: transparent !important;
    color: #ffffff !important;
    font-size: 14px !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #667384 !important;
}


/* =========================================================
   SIDEBAR INPUTS
   ========================================================= */

section[data-testid="stSidebar"] input {
    background: #111821 !important;
    color: #ffffff !important;
    border: 1px solid #293542 !important;
}

section[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background: #111821 !important;
    border-color: #293542 !important;
}


/* =========================================================
   METRIC
   ========================================================= */

[data-testid="stMetric"] {
    background: #111821 !important;
    border: 1px solid #25303d !important;
    border-radius: 12px !important;
    padding: 10px !important;
}

[data-testid="stMetricLabel"] {
    color: #7d8998 !important;
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;
}


/* =========================================================
   DIVIDERS
   ========================================================= */

hr {
    border-color: #1d2631 !important;
}


/* =========================================================
   FOOTER
   ========================================================= */

.app-footer {
    text-align: center;
    color: #46515f;
    font-size: 11px;
    margin-top: 45px;
    padding-top: 20px;
    border-top: 1px solid #151c25;
}


/* =========================================================
   TABLET
   ========================================================= */

@media (max-width: 900px) {

    .block-container {
        padding-left: 24px !important;
        padding-right: 24px !important;
    }

    .hero-title {
        font-size: 36px;
    }

}


/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 640px) {

    .block-container {
        padding-top: 15px !important;
        padding-left: 14px !important;
        padding-right: 14px !important;
        padding-bottom: 90px !important;
    }


    /* Header */

    .hero {
        padding-top: 8px;
        padding-bottom: 20px;
    }

    .hero-icon {
        font-size: 34px;
    }

    .hero-title {
        font-size: 30px;
        letter-spacing: -0.5px;
    }

    .hero-subtitle {
        font-size: 13px;
    }

    .online-status {
        font-size: 11px;
        padding: 5px 10px;
    }


    /* Welcome */

    .welcome-card {
        padding: 27px 17px;
        border-radius: 17px;
    }

    .welcome-icon {
        font-size: 32px;
    }

    .welcome-title {
        font-size: 23px;
        line-height: 1.25;
    }

    .welcome-text {
        font-size: 13px;
    }


    /* Sections */

    .section-title {
        font-size: 20px;
    }


    /* Buttons */

    .stButton > button {
        min-height: 47px !important;
        font-size: 13px !important;
    }


    /* Chat */

    .chat-title {
        font-size: 20px;
    }

    .chat-subtitle {
        display: none;
    }

    [data-testid="stChatMessage"] {
        border-radius: 13px !important;
        padding: 10px 12px !important;
    }

}


/* =========================================================
   SMALL PHONES
   ========================================================= */

@media (max-width: 380px) {

    .hero-title {
        font-size: 27px;
    }

    .hero-subtitle {
        font-size: 12px;
    }

    .welcome-title {
        font-size: 21px;
    }

    .welcome-text {
        font-size: 12px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# COURSE DATA
# =========================================================

courses = {
    "BCS301": {
        "name": "Database Management Systems",
        "credits": 4,
        "type": "Core",
        "prerequisite": "None",
        "day": "Monday",
        "time": "09:00 - 10:00"
    },

    "BCS302": {
        "name": "Computer Networks",
        "credits": 4,
        "type": "Core",
        "prerequisite": "None",
        "day": "Tuesday",
        "time": "10:00 - 11:00"
    },

    "BCS303": {
        "name": "Python Programming",
        "credits": 4,
        "type": "Core",
        "prerequisite": "Basic Programming",
        "day": "Wednesday",
        "time": "09:00 - 10:00"
    },

    "BCS304": {
        "name": "Cybersecurity Fundamentals",
        "credits": 3,
        "type": "Elective",
        "prerequisite": "None",
        "day": "Tuesday",
        "time": "11:00 - 12:00"
    },

    "BCS305": {
        "name": "Cloud Computing",
        "credits": 3,
        "type": "Elective",
        "prerequisite": "Computer Networks",
        "day": "Thursday",
        "time": "10:00 - 11:00"
    },

    "BCS306": {
        "name": "Artificial Intelligence",
        "credits": 3,
        "type": "Elective",
        "prerequisite": "Python Programming",
        "day": "Friday",
        "time": "11:00 - 12:00"
    },

    "BCS307": {
        "name": "Web Development",
        "credits": 3,
        "type": "Elective",
        "prerequisite": "Basic Programming",
        "day": "Thursday",
        "time": "11:00 - 12:00"
    }
}


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋\n\n"
                "I'm **Bren's Jarvis**, your course registration "
                "assistant.\n\n"
                "I can help you find courses, understand "
                "prerequisites, choose electives and plan "
                "your registration."
            ),
            "time": datetime.now().strftime("%I:%M %p")
        }
    ]


if "selected_courses" not in st.session_state:
    st.session_state.selected_courses = []


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def find_course(message):

    message = message.lower()

    for code, course in courses.items():

        if code.lower() in message:
            return code, course

        if course["name"].lower() in message:
            return code, course

    return None, None


def get_course_list():

    result = "### 📚 Available Courses\n\n"

    for code, course in courses.items():

        result += (
            f"**{code} · {course['name']}**\n\n"
            f"🎓 {course['type']}  •  "
            f"📊 {course['credits']} credits  •  "
            f"🕐 {course['day']} {course['time']}\n\n"
        )

    return result


def get_electives():

    result = "### 🎯 Available Electives\n\n"

    for code, course in courses.items():

        if course["type"] == "Elective":

            result += (
                f"**{code} · {course['name']}**\n\n"
                f"📊 {course['credits']} credits  •  "
                f"Prerequisite: **{course['prerequisite']}**\n\n"
            )

    return result


# =========================================================
# JARVIS BRAIN
# =========================================================

def get_response(message):

    text = message.lower().strip()


    if text in ["hi", "hello", "hey", "hii"]:

        return (
            "Hello! 👋\n\n"
            "Bren's Jarvis is online and ready to help "
            "with your course registration."
        )


    if "your name" in text or "who are you" in text:

        return (
            "I'm **Bren's Jarvis** 🤖.\n\n"
            "I'm a course registration assistant designed "
            "to help students explore and plan their courses."
        )


    if "what can you do" in text:

        return (
            "I can help you with:\n\n"
            "📚 **Find courses**\n"
            "🎯 **Explore electives**\n"
            "✅ **Check prerequisites**\n"
            "📊 **Check credits**\n"
            "🕐 **Check schedules**\n"
            "💡 **Get course recommendations**\n"
            "📋 **Understand registration steps**"
        )


    if (
        "available courses" in text
        or "show courses" in text
        or "list courses" in text
    ):

        return get_course_list()


    if "elective" in text:

        return get_electives()


    if "prerequisite" in text:

        code, course = find_course(text)

        if course:

            return (
                f"### ✅ Prerequisite\n\n"
                f"**{course['name']} ({code})**\n\n"
                f"The prerequisite is **{course['prerequisite']}**."
            )

        return (
            "Please include the course code.\n\n"
            "For example:\n"
            "**What is the prerequisite for BCS305?**"
        )


    if (
        "details" in text
        or "tell me about" in text
        or "information about" in text
    ):

        code, course = find_course(text)

        if course:

            return (
                f"### 📘 {course['name']}\n\n"
                f"**Course Code:** {code}\n\n"
                f"**Type:** {course['type']}\n\n"
                f"**Credits:** {course['credits']}\n\n"
                f"**Prerequisite:** {course['prerequisite']}\n\n"
                f"**Schedule:** {course['day']} · {course['time']}"
            )

        return (
            "Tell me which course you want to know about.\n\n"
            "Example: **Tell me about BCS305**"
        )


    if "credit" in text:

        code, course = find_course(text)

        if course:

            return (
                f"📊 **{course['name']}** has "
                f"**{course['credits']} credits**."
            )

        total = sum(
            courses[c]["credits"]
            for c in st.session_state.selected_courses
        )

        return (
            f"You currently have **{total} credits** selected."
        )


    if (
        "how to register" in text
        or "registration process" in text
        or "registration steps" in text
    ):

        return (
            "### 📋 Course Registration\n\n"
            "**1.** Check the courses available.\n\n"
            "**2.** Check prerequisites.\n\n"
            "**3.** Check timetable conflicts.\n\n"
            "**4.** Select your core courses.\n\n"
            "**5.** Choose your electives.\n\n"
            "**6.** Check your total credits.\n\n"
            "**7.** Submit your registration.\n\n"
            "Always follow your institution's official "
            "registration rules and deadlines."
        )


    if "cyber" in text or "security" in text:

        return (
            "🔐 If you're interested in cybersecurity, "
            "I'd recommend **Cybersecurity Fundamentals**.\n\n"
            "It is a **3-credit elective** with no prerequisite."
        )


    if "cloud" in text or "azure" in text:

        return (
            "☁️ If you're interested in cloud computing, "
            "I'd recommend **Cloud Computing**.\n\n"
            "It carries **3 credits** and requires "
            "Computer Networks."
        )


    if "ai" in text or "artificial intelligence" in text:

        return (
            "🤖 If you're interested in AI, "
            "I'd recommend **Artificial Intelligence**.\n\n"
            "The prerequisite is **Python Programming**."
        )


    if "thank" in text:

        return "You're welcome! 😊"


    if text in ["bye", "goodbye"]:

        return (
            "Goodbye! 👋\n\n"
            "Good luck with your course registration."
        )


    return (
        "I'm not sure about that yet. 🤔\n\n"
        "Try asking me:\n\n"
        "• 📚 **Show available courses**\n"
        "• 🎯 **Show electives**\n"
        "• 📘 **Tell me about BCS305**\n"
        "• ✅ **What is the prerequisite for BCS306?**\n"
        "• 📊 **How many credits is BCS301?**\n"
        "• 💡 **Recommend a cybersecurity course**"
    )


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-logo">
        <div class="sidebar-logo-icon">🎓</div>
        <div class="sidebar-title">Bren's Jarvis</div>
    </div>

    <div class="sidebar-subtitle">
        Course Registration Assistant
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown(
        '<div class="sidebar-section">👨‍🎓 Student</div>',
        unsafe_allow_html=True
    )

    student_name = st.text_input(
        "Student Name",
        placeholder="Enter your name"
    )

    semester = st.selectbox(
        "Semester",
        [
            "Semester 1",
            "Semester 2",
            "Semester 3",
            "Semester 4",
            "Semester 5",
            "Semester 6"
        ],
        index=2
    )

    st.divider()

    st.markdown(
        '<div class="sidebar-section">📚 Course Planner</div>',
        unsafe_allow_html=True
    )

    selected = st.multiselect(
        "Select courses",
        list(courses.keys()),
        format_func=lambda code:
            f"{code} · {courses[code]['name']}"
    )

    st.session_state.selected_courses = selected

    total_credits = sum(
        courses[code]["credits"]
        for code in selected
    )

    st.metric(
        "Selected Credits",
        total_credits
    )

    if selected:

        st.caption(
            f"{len(selected)} course(s) selected"
        )

    st.divider()

    st.markdown(
        '<div class="sidebar-section">⚡ Quick Actions</div>',
        unsafe_allow_html=True
    )

    if st.button(
        "📚 View Courses",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "Show available courses"
        )
        st.rerun()


    if st.button(
        "🎯 View Electives",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "Show electives"
        )
        st.rerun()


    if st.button(
        "📋 Registration Guide",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "How do I register for a course?"
        )
        st.rerun()


    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Conversation cleared. 🧹\n\n"
                    "Bren's Jarvis is ready."
                ),
                "time": datetime.now().strftime("%I:%M %p")
            }
        ]

        st.rerun()


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

    <div class="hero-icon">🎓</div>

    <div class="hero-title">
        Bren's Jarvis
    </div>

    <div class="hero-subtitle">
        Your Course Registration Assistant
    </div>

    <div class="online-status">
        <span>●</span>
        Registration Assistant Online
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# WELCOME
# =========================================================

name = student_name if student_name else "Student"

st.markdown(
    f"""
    <div class="welcome-card">

        <div class="welcome-icon">👋</div>

        <div class="welcome-title">
            Welcome, {name}
        </div>

        <div class="welcome-text">
            I'm Bren's Jarvis. I can help you plan your
            <strong>{semester}</strong> course registration,
            explore electives and check course requirements.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# QUICK ACTIONS
# =========================================================

st.markdown(
    '<div class="section-title">💡 What would you like to do?</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown("""
    <div class="action-card">

        <div class="action-icon">📚</div>

        <div class="action-title">
            Courses
        </div>

        <div class="action-description">
            Browse available courses
        </div>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "View Courses",
        key="courses_btn",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "Show available courses"
        )

        st.rerun()


with col2:

    st.markdown("""
    <div class="action-card">

        <div class="action-icon">🎯</div>

        <div class="action-title">
            Electives
        </div>

        <div class="action-description">
            Explore elective subjects
        </div>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "View Electives",
        key="electives_btn",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "Show electives"
        )

        st.rerun()


with col3:

    st.markdown("""
    <div class="action-card">

        <div class="action-icon">📋</div>

        <div class="action-title">
            Registration
        </div>

        <div class="action-description">
            Learn registration steps
        </div>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Registration Guide",
        key="registration_btn",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "How do I register for a course?"
        )

        st.rerun()


with col4:

    st.markdown("""
    <div class="action-card">

        <div class="action-icon">💡</div>

        <div class="action-title">
            Recommendations
        </div>

        <div class="action-description">
            Find courses for your goals
        </div>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Get Recommendation",
        key="recommend_btn",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "Recommend a course"
        )

        st.rerun()


# =========================================================
# CHAT HEADER
# =========================================================

st.markdown("""
<div class="chat-container">

    <div class="chat-header">

        <div class="chat-title">
            💬 Chat with Jarvis
        </div>

        <div class="chat-subtitle">
            Ask anything about course registration
        </div>

    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# CHAT HISTORY
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
        "Ask Bren's Jarvis about course registration..."
    )


# =========================================================
# PROCESS MESSAGE
# =========================================================

if user_input:

    current_time = datetime.now().strftime("%I:%M %p")

    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "time": current_time
    })

    with st.chat_message("user"):

        st.markdown(user_input)

        st.caption(current_time)


    response = get_response(user_input)

    with st.chat_message("assistant"):

        st.markdown(response)

        st.caption(current_time)


    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "time": current_time
    })


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="app-footer">
    Bren's Jarvis · Course Registration Assistant
    · Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)
