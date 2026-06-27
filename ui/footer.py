import streamlit as st


def render_footer() -> None:
    """Render footer and branding for the application."""

    st.markdown("---")
    st.markdown(
        "Built for TVET learners in Electrical Installation, Electronics, Robotics, PLCs, Arduino, and Industrial Automation."
    )
    st.caption(
        "⚡ Developed by Enock Kiplangat Kemoi | TVET Learning Assistant Agent | Powered by Gemini"
    )
