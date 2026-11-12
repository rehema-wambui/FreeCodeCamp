def dfs_n_queens(n):
	"""Return all solutions, each represented by a list of length n."""
	if n < 1:
		return []

	solutions = []
	placement = []
	columns = set()
	descending_diagonals = set()
	ascending_diagonals = set()

	def search(row):
		if row == n:
			solutions.append(placement.copy())
			return

		for column in range(n):
			descending = row - column
			ascending = row + column
			if (column in columns or descending in descending_diagonals
					or ascending in ascending_diagonals):
				continue

			placement.append(column)
			columns.add(column)
			descending_diagonals.add(descending)
			ascending_diagonals.add(ascending)

			search(row + 1)

			placement.pop()
			columns.remove(column)
			descending_diagonals.remove(descending)
			ascending_diagonals.remove(ascending)

	search(0)
	return solutions
