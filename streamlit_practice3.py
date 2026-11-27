import streamlit as st

st.set_page_config(page_title="Streamlit Practice #3")

option = st.sidebar.radio(
    "Navigation",
    ["Home", "Sign up Form", "Table Example"]
)

if option == "Home":
    st.title("Main dashboard ")
    st.write("Use the menu on the left to change sections.")

elif option == "Sign up Form":
    #st.form creates a form 
    with st.form("my_form", clear_on_submit=True):
        id = st.text_input("ID: ")
        email = st.text_input("Email Address: ")
        major = st.selectbox("Major", ["Engineering", "Business Management", "Design"])

        submit = st.form_submit_button("Submit")

        if submit: 
            if not id or not email:
                st.error("Information is missing. ")
            else: 
                st.success(f"Form submitted: {id} - {email} - {major}")

elif option == "Table Example":
    st.title("Examples list")

    data = [
        {"Code": "MAT101", "Course": "Calculus 1", "Credits": 4}, 
        {"Code": "PRO102", "Course": "Programming I", "Credits": 3}, 
        {"Code": "DB201", "Course": "Data Bases", "Credits": 4}, 
    ]

    st.table(data)

