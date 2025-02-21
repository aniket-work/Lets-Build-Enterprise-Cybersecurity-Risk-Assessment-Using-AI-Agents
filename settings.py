import yaml
from config import load_config_file


def load_settings():
    """Load application settings from file or return defaults"""
    settings_path = 'settings.yaml'

    # Default settings
    default_settings = {
        'business_units': [
            "Financial Systems",
            "Healthcare",
            "Industrial IoT",
            "Government Infrastructure"
        ],
        'ui': {
            'page_title': "CyberSec AI Council",
            'page_icon': "🛡️",
            'layout': "wide",
            'initial_sidebar_state': "expanded"
        },
        'analysis': {
            'max_rounds': 12,
            'speaker_selection': "round_robin"
        }
    }

    return load_config_file(settings_path, default_settings)