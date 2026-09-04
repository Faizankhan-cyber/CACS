import streamlit as st

st.title("Student Registration Form")

with st.form("student_form"):
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    age = st.number_input("Enter your age", min_value=1, max_value=100, step=1)

    course = st.selectbox(
        "Select your course",
        ["BCA", "BBA", "B.Com", "B.Sc", "Other"]
    )

    gender = st.radio(
        "Select your gender",
        ["Male", "Female", "Other"]
    )

    agree = st.checkbox("I agree to the terms and conditions")

    submitted = st.form_submit_button("Submit")

    if submitted:
        if name and email and agree:
            st.success("Form submitted successfully!")

            st.write("### Your Details")
            st.write("Name:", name)
            st.write("Email:", email)
            st.write("Age:", age)
            st.write("Course:", course)
            st.write("Gender:", gender)
        else:
            st.error("Please fill in all required fields.")