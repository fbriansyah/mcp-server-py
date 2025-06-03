from models.bank_transfer import BankTransfer, BTTransaction
from server import mcp
from utils.database import get_db
from datetime import datetime, timedelta

included_transfer_types = ["INTERBANK", "INTRABANK", "INTERBANK-BIFAST"]

@mcp.tool()
def summarize_today_transactions() -> str:
	"""
	Get today's bank transfer transactions.
	Returns:
			A string containing today's bank transfer transactions.
	"""
	db = get_db()
	transactions = db.query(BTTransaction).filter(BTTransaction.created_at.like(f"%{datetime.now().strftime('%Y-%m-%d')}%")).all()

	if not transactions:
		return "No bank transfer transactions found for today."

	# count successsful and failed transactions per bank acquirer
	successful_transactions = {}
	failed_transactions = {}
	pending_transactions = {}
	for transaction in transactions:
		## if transfer type not in included_transfer_type, then skip
		if transaction.transfer_type not in included_transfer_types:
			continue

		if transaction.status == "SUCCESS":
			if transaction.bank_acquirer in successful_transactions:
				successful_transactions[transaction.bank_acquirer] += 1
			else:
				successful_transactions[transaction.bank_acquirer] = 1
		if transaction.status == "FAILED":
			if transaction.bank_acquirer in failed_transactions:
				failed_transactions[transaction.bank_acquirer] += 1
			else:
				failed_transactions[transaction.bank_acquirer] = 1
		if transaction.status == "PENDING":
			if transaction.bank_acquirer in pending_transactions:
				pending_transactions[transaction.bank_acquirer] += 1
			else:
				pending_transactions[transaction.bank_acquirer] = 1

		total_transactions = len(transactions)
		
		result = f"Today's Bank Transfer Transactions (total: {total_transactions}):\n"
		result += f"Successful Transactions:\n"
		for bank_acquirer, count in successful_transactions.items():
			result += f"{bank_acquirer}: {count}\n"

		result += f"Failed Transactions:\n"
		for bank_acquirer, count in failed_transactions.items():
			result += f"{bank_acquirer}: {count}\n"
		
		result += f"Pending Transactions:\n"
		for bank_acquirer, count in pending_transactions.items():
			result += f"{bank_acquirer}: {count}\n"

	return result

@mcp.tool()
def summarize_yesterday_transactions() -> str:
	"""
	Get yesterday's bank transfer transactions.
	Returns:
			A string containing yesterday's bank transfer transactions.
	"""
	db = get_db()
	yesterday = datetime.now() - timedelta(days=1)
	transactions = db.query(BTTransaction).filter(BTTransaction.created_at.like(f"%{yesterday.strftime('%Y-%m-%d')}%")).all()

	if not transactions:
		return "No bank transfer transactions found for yesterday."

		# count successsful and failed transactions per bank acquirer
	successful_transactions = {}
	failed_transactions = {}
	pending_transactions = {}
	for transaction in transactions:
		if transaction.transfer_type not in included_transfer_types:
			continue

		if transaction.status == "SUCCESS":
			if transaction.bank_acquirer in successful_transactions:
				successful_transactions[transaction.bank_acquirer] += 1
			else:
				successful_transactions[transaction.bank_acquirer] = 1
		if transaction.status == "FAILED":
			if transaction.bank_acquirer in failed_transactions:
				failed_transactions[transaction.bank_acquirer] += 1
			else:
				failed_transactions[transaction.bank_acquirer] = 1
		if transaction.status == "PENDING":
			if transaction.bank_acquirer in pending_transactions:
				pending_transactions[transaction.bank_acquirer] += 1
			else:
				pending_transactions[transaction.bank_acquirer] = 1
		
		result = "Yesterday's Bank Transfer Transactions:\n"
		result += f"Successful Transactions:\n"
		for bank_acquirer, count in successful_transactions.items():
			result += f"{bank_acquirer}: {count}\n"

		result += f"Failed Transactions:\n"
		for bank_acquirer, count in failed_transactions.items():
			result += f"{bank_acquirer}: {count}\n"
		
		result += f"Pending Transactions:\n"
		for bank_acquirer, count in pending_transactions.items():
			result += f"{bank_acquirer}: {count}\n"

	return result
