def quick_sort(numbers):
	if len(numbers) <= 1:
		return numbers[:]

	pivot = numbers[0]
	less = [number for number in numbers if number < pivot]
	equal = [number for number in numbers if number == pivot]
	greater = [number for number in numbers if number > pivot]

	return quick_sort(less) + equal + quick_sort(greater)
