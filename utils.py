import json
import os
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('cybersec_council.log')
    ]
)

logger = logging.getLogger(__name__)


def create_report_filename(business_unit):
    """Create a standardized filename for security reports"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    sanitized_bu = business_unit.lower().replace(" ", "_")
    return f"security_review_{sanitized_bu}_{timestamp}.md"


def extract_recommendations(chat_history):
    """Extract key recommendations from the chat history"""
    recommendations = []

    for msg in chat_history:
        content = msg.get('content', '')

        # Look for recommendation patterns in messages
        if 'recommend' in content.lower() or 'suggest' in content.lower():
            sentences = content.split('.')
            for sentence in sentences:
                if 'recommend' in sentence.lower() or 'suggest' in sentence.lower():
                    recommendations.append(f"{msg['name']}: {sentence.strip()}.")

    return recommendations


def format_markdown_report(chat_history, business_unit):
    """Format chat history as a professional Markdown report"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Extract recommendations
    recommendations = extract_recommendations(chat_history)

    # Build report header
    report = [
        f"# Security Analysis Report",
        f"## {business_unit}",
        f"Generated: {timestamp}",
        "",
        "## Executive Summary",
        "",
        "## Key Recommendations",
    ]

    # Add recommendations
    for rec in recommendations:
        report.append(f"- {rec}")

    report.append("")
    report.append("## Detailed Analysis")
    report.append("")

    # Add full conversation
    for msg in chat_history:
        report.append(f"### {msg['name']}")
        report.append(f"{msg['content']}")
        report.append("")

    return "\n".join(report)


def save_chat_history(chat_history, business_unit):
    """Save chat history to a JSON file"""
    filename = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    try:
        with open(filename, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'business_unit': business_unit,
                'messages': chat_history
            }, f, indent=2)
        return True
    except Exception as e:
        logger.error(f"Failed to save chat history: {e}")
        return False