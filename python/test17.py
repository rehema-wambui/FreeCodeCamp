def hanoi_solver(n):
	rods = [list(range(n, 0, -1)), [], []]
	states = []

	def record_state():
		states.append(" ".join(str(rod) for rod in rods))

	def move_disks(count, source, destination, auxiliary):
		if count == 0:
			return
		move_disks(count - 1, source, auxiliary, destination)
		rods[destination].append(rods[source].pop())
		record_state()
		move_disks(count - 1, auxiliary, destination, source)

	record_state()
	move_disks(n, 0, 2, 1)
	return "\n".join(states)
    