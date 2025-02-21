import yaml
import json
import os


def load_config_file(file_path, default_data=None):
    """Load configuration from file with fallback to default data"""
    try:
        if file_path.endswith('.json'):
            with open(file_path, 'r') as file:
                return json.load(file)
        elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
            with open(file_path, 'r') as file:
                return yaml.safe_load(file)
    except (FileNotFoundError, json.JSONDecodeError, yaml.YAMLError) as e:
        print(f"Warning: Could not load config from {file_path}: {e}")

    return default_data if default_data is not None else {}


def get_agent_configs():
    """Get agent configurations from file or return defaults"""
    agent_config_path = 'agent_config.yaml'

    # Default configurations if file is not available
    default_configs = {
        "security_architect": {
            "agent_name": "SecurityArchitect",
            "system_message": """Senior Security Architect analyzing technical vulnerabilities. 
            Focus on attack vectors, security controls, and system hardening."""
        },
        "risk_analyst": {
            "agent_name": "RiskAnalyst",
            "system_message": """Risk Management Expert evaluating business impacts. 
            Quantify financial, reputational, and operational risks."""
        },
        "compliance_officer": {
            "agent_name": "ComplianceOfficer",
            "system_message": """Compliance Officer ensuring regulatory adherence.
            Verify GDPR, HIPAA, PCI-DSS, and industry standards compliance."""
        }
    }

    return load_config_file(agent_config_path, default_configs)