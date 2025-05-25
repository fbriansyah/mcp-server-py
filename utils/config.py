import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

def get_config(key, default=None):
    """
    Get a configuration value from environment variables.
    
    Args:
        key: The configuration key to look up
        default: Default value if the key is not found
        
    Returns:
        The configuration value or the default
    """
    return os.environ.get(key, default)

def get_all_config():
    """
    Get all configuration values from environment variables.
    
    Returns:
        A dictionary of all environment variables
    """
    return dict(os.environ)

# Database configuration
DB_CONFIG = {
    'user': get_config('DB_USER', 'root'),
    'password': get_config('DB_PASSWORD', ''),
    'host': get_config('DB_HOST', 'localhost'),
    'port': get_config('DB_PORT', '3306'),
    'database': get_config('DB_NAME', 'mix_server')
}
