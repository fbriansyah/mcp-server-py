from server import mcp
from utils.config import get_config, get_all_config
from typing import Optional, Dict, Any

@mcp.tool()
def get_config_value(key: str, default: Optional[str] = None) -> str:
    """
    Get a configuration value from the .env file or environment variables.
    
    Args:
        key: The configuration key to look up
        default: Default value if the key is not found
        
    Returns:
        The configuration value or the default
    """
    value = get_config(key, default)
    if value is None:
        return f"Configuration key '{key}' not found"
    return f"{key} = {value}"

@mcp.tool()
def list_all_config() -> str:
    """
    List all configuration values from the .env file and environment variables.
    
    Returns:
        A formatted string with all configuration values
    """
    config = get_all_config()
    
    # Filter out sensitive information
    sensitive_keys = ['PASSWORD', 'SECRET', 'KEY', 'TOKEN']
    filtered_config = {}
    
    for key, value in config.items():
        # Mask sensitive values
        if any(sensitive in key.upper() for sensitive in sensitive_keys):
            filtered_config[key] = "********"
        else:
            filtered_config[key] = value
    
    # Format the output
    result = "Configuration values:\n"
    for key in sorted(filtered_config.keys()):
        result += f"{key} = {filtered_config[key]}\n"
    
    return result
