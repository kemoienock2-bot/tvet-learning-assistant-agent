import streamlit as st

from utils.chat_manager import ChatManager


def render_sidebar() -> tuple[str, str | None]:
    """Render the Streamlit sidebar and return the selected mode and option."""

    st.sidebar.title("⚡ TVET Learning Assistant")

    if st.sidebar.button("➕ New Chat", use_container_width=True):
        ChatManager.create_chat()
        st.rerun()

    st.sidebar.markdown("---")

    st.sidebar.subheader("💬 Chat History")

    for chat in st.session_state.chats.keys():
        if st.sidebar.button(chat, key=chat, use_container_width=True):
            ChatManager.switch_chat(chat)
            st.rerun()

    st.sidebar.markdown("---")

    mode = st.sidebar.radio(
        "Choose Mode",
        [
            "🤖 AI Assistant",
            "🛠 Engineering Tools",
        ],
    )

    assistant = None
    tool = None

    if mode == "🤖 AI Assistant":
        assistant = st.sidebar.selectbox(
            "Choose Assistant",
            [
                "Tutor",
                "Electrical Expert",
                "Robotics Expert",
                "Project Advisor",
                "Quiz Generator",
                "Career Advisor",
                "Safety Advisor",
            ],
        )
    else:
        tool = st.sidebar.selectbox(
            "Choose Tool",
            [
                "Ohm's Law Calculator",
                "Power Calculator",
                "Energy Calculator",
            ],
        )

    st.sidebar.markdown("---")

    if st.sidebar.button("🗑 Delete Current Chat"):
        ChatManager.delete_current_chat()
        st.rerun()

    return mode, assistant or tool
