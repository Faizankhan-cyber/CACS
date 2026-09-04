import streamlit as st
from datetime import datetime


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Bren's Jarvis",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# WHITE UI STYLING
# =========================================================

st.markdown(
    """
<style>

/* ================================
   MAIN PAGE
================================ */

.stApp {
    background-color: #ffffff !important;
    color: #111111 !important;
}

.main {
    background-color: #ffffff !important;
}

.block-container {
    max-width: 1200px;
    padding-top: 35px !important;
    padding-bottom: 100px !important;
}


/* ================================
   HIDE STREAMLIT DEFAULT UI
================================ */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: #ffffff !important;
}


/* ================================
   SIDEBAR
================================ */

section[data-testid="stSidebar"] {
    background-color: #ffffff !important;
    border-right: 1px solid #e5e7eb !important;
}

section[data-testid="stSidebar"] > div {
    background-color: #ffffff !important;
}


/* Sidebar text */

section[data-testid="stSidebar"] label {
    color: #222222 !important;
}

section[data-testid="stSidebar"] p {
    color: #555555 !important;
}


/* ================================
   HEADINGS
================================ */

h1, h2, h3, h4 {
    color: #111111 !important;
}

p {
    color: #444444;
}


/* ================================
   INPUTS
================================ */

input,
textarea {
    background-color: #ffffff !important;
    color: #111111 !important;
    border: 1px solid #d1d5db !important;
    border-radius: 10px !important;
}

input::placeholder,
textarea::placeholder {
    color: #8a8a8a !important;
}


/* Select boxes */

div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #111111 !important;
    border: 1px solid #d1d5db !important;
    border-radius: 10px !important;
}

div[data-baseweb="select"] span {
    color: #222222 !important;
}


/* ================================
   BUTTONS
================================ */

.stButton > button {
    width: 100%;
    background-color: #ffffff !important;
    color: #222222 !important;
    border: 1px solid #d1d5db !important;
    border-radius: 10px !important;
    min-height: 45px !important;
    font-weight: 500 !important;
}

.stButton > button:hover {
    background-color: #f5f5f5 !important;
    border-color: #999999 !important;
    color: #111111 !important;
}


/* ================================
   HERO
================================ */

.hero-box {
    text-align: center;
    padding: 10px 10px 30px 10px;
}

.hero-title {
    font-size: 42px;
    font-weight: 700;
    color: #111111;
}

.hero-subtitle {
    font-size: 16px;
    color: #666666;
    margin-top: 8px;
}

.online {
    display: inline-block;
    margin-top: 12px;
    padding: 7px 14px;
    border: 1px solid #d1d5db;
    border-radius: 20px;
    background: #ffffff;
    color: #333333;
    font-size: 13px;
}


/* ================================
   WELCOME CARD
================================ */

.welcome-box {
    background: #ffffff;
    border: 1px solid #dcdcdc;
    border-radius: 18px;
    padding: 35px 25px;
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

.welcome-title {
    font-size: 28px;
    font-weight: 700;
    color: #111111;
}

.welcome-text {
    font-size: 15px;
    color: #666666;
    margin-top: 12px;
    line-height: 1.6;
}


/* ================================
   ACTION CARDS
================================ */

.action-box {
    background: #ffffff;
    border: 1px solid #dedede;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    margin-bottom: 10px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.04);
}

.action-icon {
    font-size: 28px;
}

.action-title {
    font-size: 15px;
    font-weight: 600;
    color: #222222;
    margin-top: 7px;
}

.action-text {
    font-size: 12px;
    color: #777777;
    margin-top: 5px;
}


/* ================================
   CHAT AREA
================================ */

.chat-heading {
    font-size: 23px;
    font-weight: 700;
    color: #111111;
    margin-top: 35px;
    margin-bottom: 5px;
}

.chat-description {
    color: #777777;
    font-size: 13px;
    margin-bottom: 15px;
}


/* Chat messages */

[data-testid="stChatMessage"] {
    background-color: #ffffff !important;
    border: 1px solid #e1e1e1 !important;
    border-radius: 14px !important;
    padding: 12px 15px !important;
    margin-bottom: 10px !important;
}


/* Chat message text */

[data-testid="stChatMessage"] p {
    color: #222222 !important;
}


/* ================================
   CHAT INPUT
================================ */

[data-testid="stChatInput"] {
    background-color: #ffffff !important;
}

[data-testid="stChatInput"] > div {
    background-color: #ffffff !important;
    border: 1px solid #cccccc !important;
    border-radius: 14px !important;
}

[data-testid="stChatInput"] textarea {
    background-color: #ffffff !important;
    color: #111111 !important;
}


/* ================================
   METRICS
================================ */

[data-testid="stMetric"] {
    background-color: #ffffff !important;
    border: 1px solid #dddddd !important;
    border-radius: 12px !important;
    padding: 12px !important;
}

[data-testid="stMetricLabel"] {
    color: #666666 !important;
}

[data-testid="stMetricValue"] {
    color: #111111 !important;
}


/* ================================
   DIVIDERS
================================ */

hr {
    border-color: #e5e5e5 !important;
}


/* ================================
   MOBILE
================================ */

@media (max-width: 768px) {

    .block-container {
        padding-left: 18px !important;
        padding-right: 18px !important;
        padding-top: 20px !important;
    }

    .hero-title {
        font-size: 32px;
    }

    .hero-subtitle {
        font-size: 14px;
    }

    .welcome-box {
        padding: 28px 18px;
    }

    .welcome-title {
        font-size: 24px;
    }

    .welcome-text {
        font-size: 14px;
    }

    .chat-heading {
        font-size: 21px;
    }
}


/* ================================
   SMALL PHONES
================================ */

@media (max-width: 450px) {

    .hero-title {
        font-size: 28px;
    }

    .hero-subtitle {
        font-size: 13px;
    }

    .welcome-title {
        font-size: 22px;
    }

}

</style>
""",
    unsafe_allow_html=True
)


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
                "I can help you find courses, explore electives, "
                "check prerequisites, and plan your registration."
            ),
            "time": datetime.now().strftime("%I:%M %p")
        }
    ]


if "selected_courses" not in st.session_state:
    st.session_state.selected_courses = []


# =========================================================
# FUNCTIONS
# =========================================================

def find_course(message):

    message = message.lower()

    for code, course in courses.items():

        if code.lower() in message:
            return code, course

        if course["name"].lower() in message:
            return code, course

    return None, None


def course_list():

    text = "### 📚 Available Courses\n\n"

    for code, course in courses.items():

        text += (
            f"**{code} · {course['name']}**\n\n"
            f"🎓 {course['type']}  |  "
            f"📊 {course['credits']} credits  |  "
            f"🕐 {course['day']} {course['time']}\n\n"
        )

    return text


def elective_list():

    text = "### 🎯 Available Electives\n\n"

    for code, course in courses.items():

        if course["type"] == "Elective":

            text += (
                f"**{code} · {course['name']}**\n\n"
                f"📊 {course['credits']} credits  |  "
                f"Prerequisite: **{course['prerequisite']}**\n\n"
            )

    return text


def jarvis_response(message):

    text = message.lower().strip()


    if text in ["hello", "hi", "hey", "hii"]:

        return (
            "Hello! 👋\n\n"
            "Bren's Jarvis is online and ready to help "
            "with your course registration."
        )


    if "your name" in text or "who are you" in text:

        return (
            "I'm **Bren's Jarvis** 🎓.\n\n"
            "I'm your course registration assistant. "
            "I can help you explore courses, electives, "
            "prerequisites and registration information."
        )


    if "what can you do" in text:

        return (
            "I can help you with:\n\n"
            "📚 Find courses\n\n"
            "🎯 Explore electives\n\n"
            "✅ Check prerequisites\n\n"
            "📊 Check course credits\n\n"
            "🕐 Check course schedules\n\n"
            "💡 Get course recommendations\n\n"
            "📋 Understand registration steps"
        )


    if (
        "available courses" in text
        or "show courses" in text
        or "list courses" in text
    ):

        return course_list()


    if "elective" in text:

        return elective_list()


    if "prerequisite" in text:

        code, course = find_course(text)

        if course:

            return (
                f"### ✅ Prerequisite\n\n"
                f"**{course['name']} ({code})**\n\n"
                f"Prerequisite: **{course['prerequisite']}**"
            )

        return (
            "Please mention the course code.\n\n"
            "Example:\n\n"
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
            "Tell me which course you want information about.\n\n"
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
            courses[code]["credits"]
            for code in st.session_state.selected_courses
        )

        return f"You currently have **{total} credits** selected."


    if (
        "how to register" in text
        or "registration process" in text
        or "registration steps" in text
    ):

        return (
            "### 📋 Registration Guide\n\n"
            "**1. Check available courses**\n\n"
            "**2. Check prerequisites**\n\n"
            "**3. Check your timetable**\n\n"
            "**4. Select your core courses**\n\n"
            "**5. Choose your electives**\n\n"
            "**6. Check your total credits**\n\n"
            "**7. Submit your registration**"
        )


    if "cyber" in text or "security" in text:

        return (
            "🔐 **Cybersecurity Fundamentals** would be "
            "a good choice if you're interested in cybersecurity.\n\n"
            "It is a 3-credit elective with no prerequisite."
        )


    if "cloud" in text or "azure" in text:

        return (
            "☁️ **Cloud Computing** would be a good choice "
            "if you're interested in cloud technologies.\n\n"
            "It carries 3 credits and requires Computer Networks."
        )


    if "ai" in text or "artificial intelligence" in text:

        return (
            "🤖 **Artificial Intelligence** is a 3-credit elective.\n\n"
            "The prerequisite is Python Programming."
        )


    if "thank" in text:

        return "You're welcome! 😊"


    if text in ["bye", "goodbye"]:

        return (
            "Goodbye! 👋\n\n"
            "Good luck with your registration."
        )


    return (
        "I'm not sure about that yet. 🤔\n\n"
        "Try asking:\n\n"
        "• **Show available courses**\n"
        "• **Show electives**\n"
        "• **Tell me about BCS305**\n"
        "• **What is the prerequisite for BCS306?**\n"
        "• **How many credits is BCS301?**\n"
        "• **Recommend a cybersecurity course**"
    )


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🎓 Bren's Jarvis")

    st.caption("Course Registration Assistant")

    st.divider()

    st.subheader("👨‍🎓 Student")

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

    st.subheader("📚 Course Planner")

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

    st.divider()

    st.subheader("⚡ Quick Actions")

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
# MAIN HEADER
# =========================================================

st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">🎓 Bren's Jarvis</div>
        <div class="hero-subtitle">
            Your Course Registration Assistant
        </div>
        <div class="online">
            ● Registration Assistant Online
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# WELCOME
# =========================================================

name = student_name if student_name else "Student"

st.markdown(
    f"""
    <div class="welcome-box">
        <div class="welcome-title">
            👋 Welcome, {name}
        </div>

        <div class="welcome-text">
            I'm Bren's Jarvis. I can help you plan your
            <strong>{semester}</strong> course registration,
            explore electives, check prerequisites,
            and understand your course options.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# QUICK ACTIONS
# =========================================================

st.subheader("💡 What would you like to do?")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(
        """
        <div class="action-box">
            <div class="action-icon">📚</div>
            <div class="action-title">Courses</div>
            <div class="action-text">
                Browse available courses
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "View Courses",
        key="main_courses",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "Show available courses"
        )
        st.rerun()


with col2:

    st.markdown(
        """
        <div class="action-box">
            <div class="action-icon">🎯</div>
            <div class="action-title">Electives</div>
            <div class="action-text">
                Explore elective subjects
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "View Electives",
        key="main_electives",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "Show electives"
        )
        st.rerun()


with col3:

    st.markdown(
        """
        <div class="action-box">
            <div class="action-icon">📋</div>
            <div class="action-title">Registration</div>
            <div class="action-text">
                Learn registration steps
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "Registration Guide",
        key="main_registration",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "How do I register for a course?"
        )
        st.rerun()


with col4:

    st.markdown(
        """
        <div class="action-box">
            <div class="action-icon">💡</div>
            <div class="action-title">Recommendations</div>
            <div class="action-text">
                Get course recommendations
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "Get Recommendation",
        key="main_recommend",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "Recommend a course"
        )
        st.rerun()


# =========================================================
# CHAT
# =========================================================

st.markdown(
    '<div class="chat-heading">💬 Chat with Jarvis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="chat-description">'
    'Ask anything about your course registration.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        st.caption(message["time"])


# =========================================================
# CHAT INPUT
# =========================================================

if "quick_question" in st.session_state:

    user_input = st.session_state.quick_question

    del st.session_state.quick_question

else:

    user_input = st.chat_input(
        "Ask Bren's Jarvis about course registration..."
    )


# =========================================================
# PROCESS USER MESSAGE
# =========================================================

if user_input:

    current_time = datetime.now().strftime("%I:%M %p")

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


    response = jarvis_response(user_input)

    with st.chat_message("assistant"):

        st.markdown(response)

        st.caption(current_time)


    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
            "time": current_time
        }
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Bren's Jarvis · Course Registration Assistant · "
    "Built with Python & Streamlit"
)
