def number_pattern(n):
	if not isinstance(n, int) or isinstance(n, bool):
		return "Argument must be an integer value."
	if n < 1:
		return "Argument must be an integer greater than 0."

	numbers = []
	for number in range(1, n + 1):
		numbers.append(str(number))
	return " ".join(numbers)
