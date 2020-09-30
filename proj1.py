class Domino:
	def __init__(self, index, strings):
		self.index = index
		self.strings = strings




# def bfs(self, frontier):
# def dfs(frontier, max_states):
def main():
	input = open("input1.txt", "r")
	input_lines = input.readlines()
	print(input_lines)

	frontier_index = input_lines[0]
	max_states = input_lines[1]
	print_sequence_flag = input_lines[2]
	domino_count = input_lines[3]
	dominos = input_lines[4:]

	print(frontier_index)
	print(max_states)
	print(print_sequence_flag)
	print(domino_count)
	# d1 =1 bb b
	# d2 =2 a aab
	# d3 =3 abbba bb
	
	for domino in dominos:
		index = domino.split()[0]
		front = domino.split()[1],
		back = domino.split()[2],
		print(index,front,back)

#		print(domino.split())














if __name__ == '__main__':
	main()
