"""
Constants used throughout the application
"""

# CSS styles for the UI
CSS_STYLES = """
    <style>
    .main {background-color: #0a1929;}
    .agent-chat {padding: 1rem; border-radius: 5px; margin: 0.5rem 0; border: 1px solid #2d3b4d;}
    .securityarchitect {border-color: #4a6fa5;}
    .riskanalyst {border-color: #c44536;}
    .complianceofficer {border-color: #5a9367;}
    </style>
    """

# Maximum number of chat rounds
MAX_CHAT_ROUNDS = 12

# Default model configuration
DEFAULT_MODEL = "gpt-4"

# Speaker selection method
SPEAKER_SELECTION = "round_robin"