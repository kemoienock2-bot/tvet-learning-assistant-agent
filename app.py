import streamlit as st

from agents.career_agent import CareerAgent
from agents.electrical_agent import ElectricalAgent
from agents.project_agent import ProjectAgent
from agents.quiz_agent import QuizAgent
from agents.robotics_agent import RoboticsAgent
from agents.safety_agent import SafetyAgent
from agents.tutor_agent import TutorAgent
from ui.chat import render_chat_interface
from ui.engineering_tools import render_engineering_tools
from ui.footer import render_footer
from ui.sidebar import render_sidebar
from utils.chat_manager import ChatManager


st.set_page_config(page_title="TVET Learning Assistant", page_icon="⚡", layout="wide")
ChatManager.initialize()

mode, selection = render_sidebar()
st.title("⚡ TVET Learning Assistant")


def handle_assistant(assistant_name: str, prompt: str) -> str:
    """Dispatch the selected assistant and return its response."""

    try:
        if assistant_name == "Tutor":
            return TutorAgent().answer_question(prompt)
        if assistant_name == "Electrical Expert":
            return ElectricalAgent().answer(prompt)
        if assistant_name == "Robotics Expert":
            return RoboticsAgent().answer(prompt)
        if assistant_name == "Project Advisor":
            return ProjectAgent().advise(prompt)
        if assistant_name == "Quiz Generator":
            return QuizAgent().generate(prompt)
        if assistant_name == "Career Advisor":
            return CareerAgent().advise()
        if assistant_name == "Safety Advisor":
            return SafetyAgent().answer()
        return "Unknown Assistant."
    except Exception as exc:
        return f"Error: {exc}"


if mode == "🤖 AI Assistant":
    render_chat_interface(selection or "Tutor", handle_assistant)
else:
    render_engineering_tools(selection or "Ohm's Law Calculator")

render_footer()
