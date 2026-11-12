def square_root_bisection(square_target, tolerance=1e-7, maximum=100):
	if square_target < 0:
		raise ValueError("Square root of negative number is not defined in real numbers")

	if square_target == 0 or square_target == 1:
		print(f"The square root of {square_target} is {square_target}")
		return square_target

	low = 0
	high = max(1, square_target)

	for _ in range(maximum):
		root = (low + high) / 2
		difference = root * root - square_target

		if abs(high - low) <= tolerance:
			print(f"The square root of {square_target} is approximately {root}")
			return root

		if difference < 0:
			low = root
		else:
			high = root

	print(f"Failed to converge within {maximum} iterations")
	return None
