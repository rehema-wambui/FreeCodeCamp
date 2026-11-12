def dfs(adjacency_matrix, node):
	visited = []

	def visit(current):
		visited.append(current)
		for neighbor, connected in enumerate(adjacency_matrix[current]):
			if connected and neighbor not in visited:
				visit(neighbor)

	visit(node)
	return visited
    