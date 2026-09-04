import streamlit as st
from datetime import datetime


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Bren's Jarvis - Course Registration",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# DARK THEME
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #080b10;
    color: #ffffff;
}

.block-container {
    max-width: 1100px;
    padding-top: 30px;
    padding-bottom: 100px;
}


/* SIDEBAR */

section[data-testid="stSidebar"] {
    background-color: #0b0f15;
    border-right: 1px solid #202630;
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb;
}


/* HEADER */

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: #ffffff;
    margin-top: 10px;
}

.main-subtitle {
    text-align: center;
    color: #8b95a3;
    font-size: 16px;
    margin-bottom: 8px;
}

.status {
    text-align: center;
    color: #4ade80;
    font-size: 14px;
    margin-bottom: 30px;
}


/* WELCOME */

.welcome-box {
    background-color: #10161e;
    border: 1px solid #242d39;
    border-radius: 18px;
    padding: 30px;
    text-align: center;
    margin-bottom: 25px;
}

.welcome-box h2 {
    color: #ffffff;
    margin-bottom: 10px;
}

.welcome-box p {
    color: #8993a1;
}


/* COURSE CARDS */

.course-card {
    background-color: #10161e;
    border: 1px solid #242d39;
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 12px;
}

.course-card h4 {
    color: #ffffff;
    margin-bottom: 5px;
}

.course-card p {
    color: #8b95a3;
}


/* CHAT */

[data-testid="stChatMessage"] {
    background-color: #10161e;
    border: 1px solid #222b37;
    border-radius: 15px;
    margin-bottom: 12px;
}


/* INPUT */

[data-testid="stChatInput"] {
    background-color: #080b10;
}

[data-testid="stChatInput"] textarea {
    background-color: #111821 !important;
    color: #ffffff !important;
    border: 1px solid #303b49 !important;
    border-radius: 14px !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #697586 !important;
}


/* BUTTONS */

.stButton > button {
    background-color: #10161e;
    color: #d8dee8;
    border: 1px solid #293442;
    border-radius: 10px;
    min-height: 42px;
}

.stButton > button:hover {
    background-color: #171e27;
    color: #ffffff;
    border-color: #4a5666;
}


/* METRICS */

[data-testid="stMetric"] {
    background-color: #10161e;
    border: 1px solid #242d39;
    border-radius: 12px;
    padding: 12px;
}


/* FOOTER */

.footer {
    text-align: center;
    color: #505a68;
    font-size: 12px;
    margin-top: 40px;
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
                "I'm **Bren's Jarvis**, your Course Registration Assistant. 🎓\n\n"
                "I can help you explore courses, understand prerequisites, "
                "check credits, find electives and plan your registration."
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
            f"Day: {course['day']} | "
            f"Time: {course['time']}\n\n"
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
# JARVIS RESPONSE SYSTEM
# =========================================================

def get_response(message):

    message = message.lower().strip()


    # GREETING

    if message in [
        "hello",
        "hi",
        "hey",
        "hii",
        "helo"
    ]:

        return (
            "Hello! 👋\n\n"
            "Bren's Jarvis is ready to help with your "
            "course registration."
        )


    # NAME

    if "your name" in message or "who are you" in message:

        return (
            "I'm **Bren's Jarvis** 🤖🎓.\n\n"
            "I'm your **Course Registration Assistant**. "
            "I help students choose and understand their courses."
        )


    # WHAT CAN YOU DO

    if "what can you do" in message:

        return (
            "I can help you with:\n\n"
            "📚 Find available courses\n"
            "🎯 Find electives\n"
            "✅ Check prerequisites\n"
            "📊 Calculate credits\n"
            "🕐 Check course timings\n"
            "📋 Explain registration steps\n"
            "💡 Suggest courses based on your interests\n"
            "📝 Build a sample course plan"
        )


    # AVAILABLE COURSES

    if (
        "available courses" in message
        or "courses available" in message
        or "list courses" in message
        or "show courses" in message
    ):

        return course_list()


    # ELECTIVES

    if (
        "elective" in message
        or "electives" in message
    ):

        return elective_list()


    # PREREQUISITE

    if (
        "prerequisite" in message
        or "prerequisite" in message
        or "requirement" in message
    ):

        code, course = find_course(message)

        if course:

            return (
                f"📘 **{course['name']} ({code})**\n\n"
                f"Prerequisite: **{course['prerequisite']}**"
            )

        return (
            "Please mention the course code or course name.\n\n"
            "For example:\n"
            "**What is the prerequisite for BCS305?**"
        )


    # COURSE DETAILS

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
                f"**Department:** {course['department']}\n\n"
                f"**Prerequisite:** {course['prerequisite']}\n\n"
                f"**Schedule:** {course['day']}, {course['time']}"
            )

        return (
            "Please provide a course code.\n\n"
            "Example: **Tell me about BCS305**"
        )


    # CREDITS

    if (
        "credits" in message
        or "credit" in message
    ):

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

        if st.session_state.selected_courses:

            return (
                f"Your currently selected courses carry "
                f"**{total} credits** in total."
            )

        return (
            "You haven't selected any courses yet.\n\n"
            "Use the **Course Planner** in the sidebar."
        )


    # PYTHON

    if "python" in message:

        return (
            "🐍 **Python Programming** is a core programming "
            "course in this sample catalog.\n\n"
            "It carries **4 credits**.\n\n"
            "It is also a prerequisite for Artificial Intelligence."
        )


    # CYBERSECURITY

    if (
        "cybersecurity" in message
        or "cyber security" in message
    ):

        return (
            "🔐 **Cybersecurity Fundamentals** is an elective "
            "focused on basic security concepts.\n\n"
            "Credits: **3**\n\n"
            "Prerequisite: **None**"
        )


    # CLOUD

    if "cloud" in message:

        return (
            "☁️ **Cloud Computing** is an elective focused "
            "on cloud platforms and services.\n\n"
            "Credits: **3**\n\n"
            "Prerequisite: **Computer Networks**"
        )


    # AI

    if (
        "artificial intelligence" in message
        or "what is ai" in message
    ):

        return (
            "🤖 **Artificial Intelligence** is an elective "
            "focused on AI concepts and applications.\n\n"
            "Credits: **3**\n\n"
            "Prerequisite: **Python Programming**"
        )


    # REGISTRATION PROCESS

    if (
        "how to register" in message
        or "registration process" in message
        or "register for course" in message
    ):

        return (
            "📋 **Typical Course Registration Process**\n\n"
            "**1.** Check the available courses.\n\n"
            "**2.** Review prerequisites.\n\n"
            "**3.** Check your timetable for conflicts.\n\n"
            "**4.** Select the required core courses.\n\n"
            "**5.** Choose your electives.\n\n"
            "**6.** Check your total credits.\n\n"
            "**7.** Submit your registration.\n\n"
            "Always follow your college's official registration "
            "rules and deadlines."
        )


    # RECOMMENDATION

    if (
        "recommend" in message
        or "suggest" in message
        or "which course" in message
    ):

        if (
            "cyber" in message
            or "security" in message
        ):

            return (
                "🔐 If you're interested in cybersecurity, "
                "I'd recommend **Cybersecurity Fundamentals**.\n\n"
                "It is a 3-credit elective with no prerequisite."
            )

        if (
            "cloud" in message
            or "azure" in message
        ):

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
                "You'll need Python Programming as a prerequisite."
            )

        return (
            "I can recommend a course based on your interest.\n\n"
            "Try:\n"
            "• **Recommend a cybersecurity course**\n"
            "• **Recommend a cloud course**\n"
            "• **Recommend an AI course**"
        )


    # THANK YOU

    if (
        "thanks" in message
        or "thank you" in message
    ):

        return (
            "You're welcome! 😊\n\n"
            "Happy to help with your registration."
        )


    # GOODBYE

    if message in [
        "bye",
        "goodbye"
    ]:

        return (
            "Goodbye! 👋\n\n"
            "Good luck with your course registration."
        )


    # DEFAULT

    return (
        "I'm not sure about that yet. 🤔\n\n"
        "Try asking me something like:\n\n"
        "📚 **Show available courses**\n"
        "🎯 **Show electives**\n"
        "📘 **Tell me about BCS305**\n"
        "✅ **What is the prerequisite for BCS306?**\n"
        "📊 **How many credits is BCS301?**\n"
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
        ]
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

        st.error("⚠️ Credit load is high.")

    elif total_credits > 0:

        st.success("✅ Credit load calculated.")

    st.divider()

    st.subheader("🔎 Quick Tools")

    if st.button(
        "📚 View All Courses",
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
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Chat cleared. 🧹\n\n"
                    "Bren's Jarvis is ready to help with "
                    "your course registration."
                ),
                "time": datetime.now().strftime("%I:%M %p")
            }
        ]

        st.rerun()


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
    '<div class="status">● Registration Assistant Online</div>',
    unsafe_allow_html=True
)


# =========================================================
# WELCOME
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
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        st.caption(message["time"])


# =========================================================
# USER INPUT
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


    # User message

    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "time": current_time
    })


    with st.chat_message("user"):

        st.markdown(user_input)

        st.caption(current_time)


    # Jarvis response

    response = get_response(user_input)


    with st.chat_message("assistant"):

        placeholder = st.empty()

        words = response.split()

        displayed = ""

        for word in words:

            displayed += word + " "

            placeholder.markdown(displayed)

            time.sleep(0.01)

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
    'Bren\'s Jarvis • Course Registration Assistant • '
    'Built with Python & Streamlit'
    '</div>',
    unsafe_allow_html=True
)
