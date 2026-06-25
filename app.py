import streamlit as st
from agents.tutor_agent import TutorAgent

st.title("TVET Learning Assistant Agent")

st.write(
"AI-powered tutor for Electrical Installation, Electronics, and Robotics."
)

question = st.text_input("Ask a question")

if question:
tutor = TutorAgent()
response = tutor.answer_question(question)
st.write(response)

