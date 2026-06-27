import streamlit as st


class ChatManager:

    @staticmethod
    def initialize():

        if "chats" not in st.session_state:

            st.session_state.chats = {
                "New Chat": []
            }

        if "current_chat" not in st.session_state:

            st.session_state.current_chat = "New Chat"

    @staticmethod
    def get_messages():

        return st.session_state.chats[
            st.session_state.current_chat
        ]

    @staticmethod
    def add_message(role, content):

        st.session_state.chats[
            st.session_state.current_chat
        ].append(
            {
                "role": role,
                "content": content,
            }
        )

    @staticmethod
    def create_chat():

        number = len(st.session_state.chats) + 1

        name = f"New Chat {number}"

        st.session_state.chats[name] = []

        st.session_state.current_chat = name

    @staticmethod
    def switch_chat(name):

        st.session_state.current_chat = name

    @staticmethod
    def delete_current_chat():

        current = st.session_state.current_chat

        if len(st.session_state.chats) > 1:

            del st.session_state.chats[current]

            st.session_state.current_chat = list(
                st.session_state.chats.keys()
            )[0]