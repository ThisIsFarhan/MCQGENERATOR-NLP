import streamlit as st
from generator import generateMCQS

st.title("Automated MCQS Generator (NLP)")
st.write("Developed and Deployed by Farhan Ali Khan")
st.divider()
text = st.text_input("Enter the text")
st.text_area("Text", text,)
numberofquestions = st.slider("No. of Questions",1, 8)
btn = st.button("Generate Questions")
st.divider()

if len(text) != 0 and btn == 1:
    form = st.form("my form")
    questions = generateMCQS(text, numberofquestions)
    for ques in questions:
        form.text_area("Question",ques.ques)
        # form.radio("Options",ques.choices, disabled=False)
        bullets = "\n".join([f"- {choice}" for choice in ques.choices])
        form.markdown(bullets)
        form.markdown(f"Correct Answer: {ques.correct_answer}")
        form.divider()
    submit = form.form_submit_button("Clear")


