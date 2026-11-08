class Category:
	def __init__(self, name):
		self.name = name
		self.ledger = []

	def deposit(self, amount, description=""):
		self.ledger.append({"amount": amount, "description": description})

	def withdraw(self, amount, description=""):
		if not self.check_funds(amount):
			return False
		self.ledger.append({"amount": -amount, "description": description})
		return True

	def get_balance(self):
		return sum(entry["amount"] for entry in self.ledger)

	def transfer(self, amount, category):
		if not self.check_funds(amount):
			return False
		self.withdraw(amount, f"Transfer to {category.name}")
		category.deposit(amount, f"Transfer from {self.name}")
		return True

	def check_funds(self, amount):
		return amount <= self.get_balance()

	def __str__(self):
		lines = [f"{self.name:*^30}"]
		for entry in self.ledger:
			description = entry["description"][:23]
			amount = f"{entry['amount']:.2f}"[:7]
			lines.append(f"{description:<23}{amount:>7}")
		lines.append(f"Total: {self.get_balance():.2f}")
		return "\n".join(lines)


def create_spend_chart(categories):
	withdrawals = [
		sum(-entry["amount"] for entry in category.ledger if entry["amount"] < 0)
		for category in categories
	]
	total_spent = sum(withdrawals)
	percentages = [
		int((amount / total_spent * 100) // 10) * 10 if total_spent else 0
		for amount in withdrawals
	]

	lines = ["Percentage spent by category"]
	for level in range(100, -1, -10):
		line = f"{level:>3}| "
		line += "".join("o  " if percentage >= level else "   " for percentage in percentages)
		lines.append(line)

	lines.append("    " + "-" * (len(categories) * 3 + 1))
	max_name_length = max((len(category.name) for category in categories), default=0)
	for row in range(max_name_length):
		line = "     "
		line += "".join(
			(category.name[row] if row < len(category.name) else " ") + "  "
			for category in categories
		)
		lines.append(line)

	return "\n".join(lines)
