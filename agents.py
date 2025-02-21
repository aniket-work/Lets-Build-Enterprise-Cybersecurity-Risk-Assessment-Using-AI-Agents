import streamlit as st
import os
from autogen import AssistantAgent, GroupChat, GroupChatManager, UserProxyAgent
from config import get_agent_configs

class CyberSecurityTeam:
    def __init__(self):
        self.agent_configs = get_agent_configs()
        self.agents = self._create_agents()
        self.group_chat = self._create_group_chat()
        self.manager = GroupChatManager(
            groupchat=self.group_chat,
            llm_config={"config_list": [{"model": "gpt-4", "api_key": os.getenv("OPENAI_API_KEY")}]}
        )
        self.chat_history = []

    def _create_agents(self):
        agents = {}
        for name, config in self.agent_configs.items():
            agents[name] = AssistantAgent(
                name=config["agent_name"],
                system_message=config["system_message"],
                llm_config={"config_list": [{"model": "gpt-4", "api_key": os.getenv("OPENAI_API_KEY")}]}
            )
        return agents

    def _create_group_chat(self):
        return GroupChat(
            agents=list(self.agents.values()),
            messages=[],
            max_round=12,
            speaker_selection_method="round_robin"
        )

    async def analyze_proposal(self, proposal, business_unit):
        self.chat_history = []
        user_proxy = UserProxyAgent(
            name="UserProxy",
            human_input_mode="NEVER",
            code_execution_config=False
        )

        await user_proxy.a_initiate_chat(
            self.manager,
            message=f"""Analyze this security proposal for {business_unit}:
            {proposal}
            Provide FINAL_RECOMMENDATION when complete."""
        )

        self.chat_history = self.group_chat.messages
        return self.chat_history[-1] if self.chat_history else None