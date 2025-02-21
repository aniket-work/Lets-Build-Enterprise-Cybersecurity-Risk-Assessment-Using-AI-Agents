import streamlit as st
from constants import CSS_STYLES


def configure_ui():
    """Configure the Streamlit UI appearance"""
    st.set_page_config(
        page_title="CyberSec AI Council",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.markdown(CSS_STYLES, unsafe_allow_html=True)


def render_security_review(chat_history, final_msg):
    """Render the security review analysis and final recommendation"""
    container = st.container()

    for msg in chat_history:
        with container:
            role = msg['name'].replace('_', ' ').title()
            css_class = f"agent-chat {msg['name'].lower()}"
            st.markdown(f"""
                <div class="{css_class}">
                    <strong>{role}:</strong><br>
                    {msg['content']}
                </div>
            """, unsafe_allow_html=True)

    if final_msg and 'FINAL_RECOMMENDATION' in final_msg['content']:
        st.session_state.review_complete = True
        st.markdown(f"## Final Security Recommendation\n{final_msg['content']}")
        st.download_button(
            "Download Audit Report",
            "\n\n".join([f"{m['name']}: {m['content']}" for m in chat_history]),
            file_name="security_review_audit.md"
        )