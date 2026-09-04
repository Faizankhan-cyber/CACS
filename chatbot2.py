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
# RESPONSIVE DARK THEME
# =========================================================

st.markdown("""
<style>

/* ========================================================
   GLOBAL
   ======================================================== */

html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}

.stApp {
    background: #080b10;
    color: #ffffff;
}

.main .block-container {
    max-width: 1050px;
    padding-top: 32px;
    padding-left: 35px;
    padding-right: 35px;
    padding-bottom: 120px;
}


/* ========================================================
   SIDEBAR
   ======================================================== */

section[data-testid="stSidebar"] {
    background-color: #0b0f15;
    border-right: 1px solid #202630;
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb;
}


/* ========================================================
   MAIN HEADER
   ======================================================== */

.main-title {
    text-align: center;
    font-size: 40px;
    line-height: 1.2;
    font-weight: 700;
    color: #ffffff;
    margin: 0;
    padding: 0;
}

.main-subtitle {
    text-align: center;
    color: #8b95a3;
    font-size: 16px;
    margin-top: 8px;
}

.status {
    text-align: center;
    color: #4ade80;
    font-size: 14px;
    margin-top: 10px;
    margin-bottom: 32px;
}


/* ========================================================
   WELCOME CARD
   ======================================================== */

.welcome-box {
    background: #10161e;
    border: 1px solid #26313e;
    border-radius: 18px;
    padding: 30px 25px;
    text-align: center;
    margin-bottom: 28px;
}

.welcome-box h2 {
    color: #ffffff;
    font-size: 28px;
    line-height: 1.3;
    margin: 0 0 12px 0;
}

.welcome-box p {
    color: #8f99a8;
    font-size: 16px;
    line-height: 1.6;
    margin: 0;
}


/* ========================================================
   SECTION HEADINGS
   ======================================================== */

h1, h2, h3 {
    color: #ffffff !important;
}


/* ========================================================
   QUICK ACTION BUTTONS
   ======================================================== */

.stButton > button {
    width: 100%;
    min-height: 44px;
    background-color: #10161e;
    color: #dce2ea;
    border: 1px solid #2a3542;
    border-radius: 10px;
    font-size: 14px;
    transition: 0.2s;
}

.stButton > button:hover {
    background-color: #171f29;
    color: #ffffff;
    border-color: #4b5868;
}


/* ========================================================
   CHAT MESSAGES
   ======================================================== */

[data-testid="stChatMessage"] {
    background-color: #10161e;
    border: 1px solid #222c38;
    border-radius: 14px;
    padding: 12px 16px;
    margin-bottom: 10px;
}


/* ========================================================
   CHAT INPUT
   ======================================================== */

[data-testid="stChatInput"] {
    background-color: #080b10 !important;
}

[data-testid="stChatInput"] textarea {
    background-color: #111821 !important;
    color: #ffffff !important;
    border: 1px solid #303b49 !important;
    border-radius: 14px !important;
    font-size: 15px !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #697586 !important;
}


/* ========================================================
   METRICS
   ======================================================== */

[data-testid="stMetric"] {
    background-color: #10161e;
    border: 1px solid #242d39;
    border-radius: 12px;
    padding: 12px;
}


/* ========================================================
   COURSE CARD
   ======================================================== */

.course-card {
    background-color: #10161e;
    border: 1px solid #242d39;
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 12px;
}


/* ========================================================
   FOOTER
   ======================================================== */

.footer {
    text-align: center;
    color: #505a68;
    font-size: 12px;
    margin-top: 40px;
    padding-bottom: 20px;
}


/* ========================================================
   TABLET
   ======================================================== */

@media (max-width: 900px) {

    .main .block-container {
        max-width: 900px;
        padding-left: 25px;
        padding-right: 25px;
    }

    .main-title {
        font-size: 36px;
    }

    .welcome-box {
        padding: 25px 20px;
    }

}


/* ========================================================
   MOBILE
   ======================================================== */

@media (max-width: 640px) {

    /* Main page */

    .main .block-container {
        width: 100%;
        max-width: 100%;
        padding-top: 22px;
        padding-left: 15px;
        padding-right: 15px;
        padding-bottom: 100px;
    }


    /* Header */

    .main-title {
        font-size: 30px;
        line-height: 1.2;
        white-space: normal;
    }

    .main-subtitle {
        font-size: 14px;
        margin-top: 8px;
        line-height: 1.4;
    }

    .status {
        font-size: 13px;
        margin-top: 8px;
        margin-bottom: 24px;
    }


    /* Welcome */

    .welcome-box {
        padding: 25px 16px;
        border-radius: 16px;
        margin-bottom: 24px;
    }

    .welcome-box h2 {
        font-size: 25px;
        line-height: 1.25;
    }

    .welcome-box p {
        font-size: 14px;
        line-height: 1.6;
    }


    /* Section heading */

    .main .block-container h2 {
        font-size: 25px !important;
    }

    .main .block-container h3 {
        font-size: 21px !important;
    }


    /* Quick buttons */

    .stButton > button {
        min-height: 48px;
        font-size: 14px;
    }


    /* Chat */

    [data-testid="stChatMessage"] {
        border-radius: 12px;
        padding: 10px 12px;
    }

    [data-testid="stChatInput"] textarea {
        font-size: 14px !important;
    }


    /* Metrics */

    [data-testid="stMetric"] {
        padding: 9px;
    }


    /* Footer */

    .footer {
        font-size: 11px;
        margin-top: 25px;
    }

}


/* ========================================================
   VERY SMALL PHONES
   ======================================================== */

@media (max-width: 380px) {

    .main .block-container {
        padding-left: 12px;
        padding-right: 12px;
    }

    .main-title {
        font-size: 27px;
    }

    .main-subtitle {
        font-size: 13px;
    }

    .welcome-box h2 {
        font-size: 22px;
    }

    .welcome-box p {
        font-size: 13px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SAMPLE COURSE DATABASE
# =========================================================

courses = {

    "BCS301": {
        "name": "Database Management Systems",
        "credits": 4,
        "type": "Core",
        "semester": 3,
        "department": "Computer Applications",
        "prerequisite": "None",
        "day": "Monday",
        "time": "09:00 - 10:00"
    },

    "BCS302": {
        "name": "Computer Networks",
        "credits": 4,
        "type": "Core",
        "semester": 3,
        "department": "Computer Applications",
        "prerequisite": "None",
        "day": "Tuesday",
        "time": "10:00 - 11:00"
    },

    "BCS303": {
        "name": "Python Programming",
        "credits": 4,
        "type": "Core",
        "semester": 3,
        "department": "Computer Applications",
        "prerequisite": "Basic Programming",
        "day": "Wednesday",
        "time": "09:00 - 10:00"
    },

    "BCS304": {
        "name": "Cybersecurity Fundamentals",
        "credits": 3,
        "type": "Elective",
        "semester": 3,
        "department": "Computer Applications",
        "prerequisite": "None",
        "day": "Tuesday",
        "time": "11:00 - 12:00"
    },

    "BCS305": {
        "name": "Cloud Computing",
        "credits": 3,
        "type": "Elective",
        "semester": 3,
        "department": "Computer Applications",
        "prerequisite": "Computer Networks",
        "day": "Thursday",
        "time": "10:00 - 11:00"
    },

    "BCS306": {
        "name": "Artificial Intelligence",
        "credits": 3,
        "type": "Elective",
        "semester": 3,
        "department": "Computer Applications",
        "prerequisite": "Python Programming",
        "day": "Friday",
        "time": "11:00 - 12:00"
    },

    "BCS307": {
        "name": "Web Development",
        "credits": 3,
        "type": "Elective",
        "semester": 3,
        "department": "Computer Applications",
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
                "Hello, student! 👋\n\n"
                "I'm **Bren's Jarvis**, your Course Registration "
                "Assistant. 🎓\n\n"
                "I can help you explore courses, check "
                "prerequisites, compare electives and plan "
                "your registration."
            ),
            "time": datetime.now().strftime("%I:%M %p")
        }
    ]


if "selected_courses" not in st.session_state:
    st.session_state.selected_courses = []


# =========================================================
# COURSE FUNCTIONS
# =========================================================

def course_list():

    text = "📚 **Available Courses**\n\n"

    for code, course in courses.items():

        text += (
            f"**{code} - {course['name']}**\n"
            f"Credits: {course['credits']} | "
            f"Type: {course['type']} | "
            f"Schedule: {course['day']}, {course['time']}\n\n"
        )

    return text


def elective_list():

    text = "🎯 **Available Electives**\n\n"

    for code, course in courses.items():

        if course["type"] == "Elective":

            text += (
                f"**{code} - {course['name']}**\n"
                f"Credits: {course['credits']} | "
                f"Prerequisite: {course['prerequisite']}\n\n"
            )

    return text


def find_course(message):

    for code, course in courses.items():

        if code.lower() in message:
            return code, course

        if course["name"].lower() in message:
            return code, course

    return None, None


# =========================================================
# JARVIS RESPONSE
# =========================================================

def get_response(message):

    message = message.lower().strip()


    if message in ["hello", "hi", "hey", "hii", "helo"]:

        return (
            "Hello! 👋\n\n"
            "Bren's Jarvis is online and ready to help "
            "with your course registration."
        )


    if "your name" in message or "who are you" in message:

        return (
            "I'm **Bren's Jarvis** 🤖🎓.\n\n"
            "I'm your Course Registration Assistant."
        )


    if "what can you do" in message:

        return (
            "I can help you with:\n\n"
            "📚 Find available courses\n"
            "🎯 Find electives\n"
            "✅ Check prerequisites\n"
            "📊 Calculate credits\n"
            "🕐 Check course timings\n"
            "📋 Explain registration steps\n"
            "💡 Suggest courses based on your interests"
        )


    if (
        "available courses" in message
        or "courses available" in message
        or "list courses" in message
        or "show courses" in message
    ):

        return course_list()


    if "elective" in message:

        return elective_list()


    if "prerequisite" in message or "requirement" in message:

        code, course = find_course(message)

        if course:

            return (
                f"📘 **{course['name']} ({code})**\n\n"
                f"Prerequisite: **{course['prerequisite']}**"
            )

        return (
            "Please mention the course code or name.\n\n"
            "Example: **What is the prerequisite for BCS305?**"
        )


    if (
        "details" in message
        or "information about" in message
        or "tell me about" in message
    ):

        code, course = find_course(message)

        if course:

            return (
                f"📘 **{course['name']} ({code})**\n\n"
                f"**Credits:** {course['credits']}\n\n"
                f"**Type:** {course['type']}\n\n"
                f"**Semester:** {course['semester']}\n\n"
                f"**Prerequisite:** {course['prerequisite']}\n\n"
                f"**Schedule:** {course['day']}, {course['time']}"
            )

        return (
            "Please provide a course code.\n\n"
            "Example: **Tell me about BCS305**"
        )


    if "credit" in message:

        code, course = find_course(message)

        if course:

            return (
                f"📊 **{course['name']}** carries "
                f"**{course['credits']} credits**."
            )

        total = sum(
            courses[c]["credits"]
            for c in st.session_state.selected_courses
        )

        return (
            f"Your selected courses currently carry "
            f"**{total} credits**."
        )


    if "how to register" in message or "registration process" in message:

        return (
            "📋 **Course Registration Steps**\n\n"
            "**1.** Check available courses.\n\n"
            "**2.** Check prerequisites.\n\n"
            "**3.** Check your timetable.\n\n"
            "**4.** Select your core courses.\n\n"
            "**5.** Select your electives.\n\n"
            "**6.** Check your total credits.\n\n"
            "**7.** Submit your registration.\n\n"
            "Always follow your college's official registration "
            "rules and deadlines."
        )


    if "cyber" in message or "security" in message:

        return (
            "🔐 If you're interested in cybersecurity, "
            "I'd recommend **Cybersecurity Fundamentals**.\n\n"
            "It is a 3-credit elective with no prerequisite."
        )


    if "cloud" in message or "azure" in message:

        return (
            "☁️ If you're interested in cloud computing, "
            "I'd recommend **Cloud Computing**.\n\n"
            "It carries 3 credits and requires "
            "Computer Networks."
        )


    if "ai" in message:

        return (
            "🤖 If you're interested in AI, "
            "I'd recommend **Artificial Intelligence**.\n\n"
            "Python Programming is the prerequisite."
        )


    if "thank" in message:

        return (
            "You're welcome! 😊\n\n"
            "Happy to help with your registration."
        )


    if message in ["bye", "goodbye"]:

        return (
            "Goodbye! 👋\n\n"
            "Good luck with your course registration."
        )


    return (
        "I'm not sure about that yet. 🤔\n\n"
        "Try asking:\n\n"
        "📚 **Show available courses**\n"
        "🎯 **Show electives**\n"
        "📘 **Tell me about BCS305**\n"
        "✅ **What is the prerequisite for BCS306?**\n"
        "💡 **Recommend a cybersecurity course**\n"
        "📋 **How do I register for a course?**"
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
        f"{code} - {courses[code]['name']}"
    )

    st.session_state.selected_courses = selected

    total_credits = sum(
        courses[code]["credits"]
        for code in selected
    )

    st.metric(
        "Total Credits",
        total_credits
    )

    if total_credits > 24:

        st.warning("⚠️ High credit load")

    elif total_credits > 0:

        st.success("✅ Credit load calculated")

    st.divider()

    st.subheader("🔎 Quick Tools")

    if st.button(
        "📚 View All Courses",
        use_container_width=True
    ):

        st.session_state.quick_question = "Show available courses"
        st.rerun()


    if st.button(
        "🎯 View Electives",
        use_container_width=True
    ):

        st.session_state.quick_question = "Show electives"
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
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Chat cleared. 🧹\n\n"
                    "Bren's Jarvis is ready to help "
                    "with your registration."
                ),
                "time": datetime.now().strftime("%I:%M %p")
            }
        ]

        st.rerun()

    st.divider()

    st.success("● JARVIS ONLINE")

    st.caption("Python + Streamlit")


# =========================================================
# MAIN HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🎓 Bren\'s Jarvis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'Your Course Registration Assistant'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="status">'
    '● Registration Assistant Online'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# WELCOME SECTION
# =========================================================

if len(st.session_state.messages) == 1:

    name = student_name if student_name else "Student"

    st.markdown(
        f"""
        <div class="welcome-box">

            <h2>👋 Welcome, {name}</h2>

            <p>
            I'm Bren's Jarvis. I can help you plan your
            <b>{semester}</b> course registration.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("💡 What would you like to do?")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        if st.button(
            "📚 Courses",
            use_container_width=True
        ):

            st.session_state.quick_question = (
                "Show available courses"
            )

            st.rerun()

    with col2:

        if st.button(
            "🎯 Electives",
            use_container_width=True
        ):

            st.session_state.quick_question = (
                "Show electives"
            )

            st.rerun()

    with col3:

        if st.button(
            "📋 Registration",
            use_container_width=True
        ):

            st.session_state.quick_question = (
                "How do I register for a course?"
            )

            st.rerun()

    with col4:

        if st.button(
            "💡 Recommendations",
            use_container_width=True
        ):

            st.session_state.quick_question = (
                "Recommend a course"
            )

            st.rerun()


# =========================================================
# CHAT HISTORY
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
# PROCESS MESSAGE
# =========================================================

if user_input:

    current_time = datetime.now().strftime("%I:%M %p")


    # USER

    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "time": current_time
    })

    with st.chat_message("user"):

        st.markdown(user_input)
        st.caption(current_time)


    # JARVIS

    response = get_response(user_input)

    with st.chat_message("assistant"):

        st.markdown(response)
        st.caption(current_time)


    # SAVE

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
    'Bren\'s Jarvis • Course Registration Assistant • '
    'Built with Python & Streamlit'
    '</div>',
    unsafe_allow_html=True
)
