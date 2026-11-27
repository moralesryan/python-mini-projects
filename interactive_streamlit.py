import streamlit as st

st.title("Grade Calculator ")

name = st.text_input("Student's name: ")
grade1 = st.number_input("Grade 1: ", min_value=0.0, max_value=100.0, step=1.0)
grade2 = st.number_input("Grade 2: ", min_value=0.0, max_value=100.0, step=1.0)
grade3 = st.number_input("Grade 3: ", min_value=0.0, max_value=100.0, step=1.0)

if st.button("Calculate grade: "):
    if name.strip() == "":
        st.warning("Please type the student's name ")
    else:
        final_grade = (grade1 + grade2 + grade3) / 3
        st.write(f"Name: **{name}**")
        st.write(f"Final grade: **{final_grade:.2f}**")
    
        if final_grade >= 70:
            st.success("Approved!")

        else: 
            st.error("Failed. ")

            