def verify_card_number(card_number):
	digits = card_number.replace("-", "").replace(" ", "")

	if not digits or not digits.isdigit():
		return "INVALID!"

	total = 0
	double_digit = False

	for digit in reversed(digits):
		value = int(digit)
		if double_digit:
			value *= 2
			if value > 9:
				value -= 9
		total += value
		double_digit = not double_digit

	return "VALID!" if total % 10 == 0 else "INVALID!"
