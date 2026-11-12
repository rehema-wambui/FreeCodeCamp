def adjacency_list_to_matrix(adjacency_list):
	nodes = list(adjacency_list)
	for neighbors in adjacency_list.values():
		for neighbor in neighbors:
			if neighbor not in nodes:
				nodes.append(neighbor)
	node_indices = {node: index for index, node in enumerate(nodes)}
	number_of_nodes = len(nodes)
	matrix = [[0] * number_of_nodes for _ in range(number_of_nodes)]

	for node, neighbors in adjacency_list.items():
		for neighbor in neighbors:
			matrix[node_indices[node]][node_indices[neighbor]] = 1

	for row in matrix:
		print(row)

	return matrix
