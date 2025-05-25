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
		result += f"UUID: {config.uuid}, Priority: {config.priority}, Transfer Type: {config.transfer_type}, Bank Name: {config.account.bank_name}, Bank Code: {config.account.bank_code}, Is Active: {config.is_active}\n"

	return result