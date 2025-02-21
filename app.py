import asyncio
import streamlit as st
from dotenv import load_dotenv
from agents import CyberSecurityTeam
from ui_components import configure_ui, render_security_review
from settings import load_settings

# Load environment variables and settings
load_dotenv()
settings = load_settings()

# Configure the Streamlit UI
configure_ui()

def main():
    st.title("🛡️ Enterprise Cyber AI Council")

    with st.sidebar:
        st.header("Review Context")
        business_unit = st.selectbox("Business Unit", settings['business_units'])

    proposal = st.text_area("Security Proposal:", height=250,
                            placeholder="Describe system architecture, data flows, and security controls...")

    if "cyber_team" not in st.session_state:
        st.session_state.cyber_team = CyberSecurityTeam()
        st.session_state.business_unit = business_unit

    if st.button("Start Security Review"):
        st.session_state.messages = []
        st.session_state.review_complete = False

        async def run_analysis():
            final_msg = await st.session_state.cyber_team.analyze_proposal(
                proposal,
                st.session_state.business_unit
            )
            render_security_review(
                st.session_state.cyber_team.chat_history,
                final_msg
            )

        asyncio.run(run_analysis())


if __name__ == "__main__":
    main()