import streamlit as st

from utils.chat_manager import ChatManager


def render_chat_interface(assistant_name: str, submit_handler) -> None:
    """Render chat messages and prompt input for the selected assistant."""

    messages = ChatManager.get_messages()

    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask your question...")

    if prompt:
        ChatManager.add_message("user", prompt)
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = submit_handler(assistant_name, prompt)
            st.markdown(response)

        ChatManager.add_message("assistant", response)
