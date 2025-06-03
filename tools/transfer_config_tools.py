from models.transfer_config import TransferConfig
from server import mcp
from utils.database import get_db

@mcp.tool()
def list_transfer_configs() -> str:
	"""
	List all transfer configurations.

	Returns:
			A string containing transfer configuration
	"""
	db = get_db()
	transfer_configs = db.query(TransferConfig).filter(TransferConfig.is_active == True).all()
	if not transfer_configs:
		return "No transfer configurations found in the database."

	result = "Transfer Configurations:\n"
	for config in transfer_configs:
		result += f"UUID: {config.uuid}\n"
		result += f"Priority: {config.priority}\n"
		result += f"Transfer Type: {config.transfer_type}\n"
		result += f"Bank Name: {config.account.bank_name}\n"
		result += f"Bank Code: {config.account.bank_code}\n"
		result += f"Is Active: {config.is_active}\n"
		result += "\n"

	return result