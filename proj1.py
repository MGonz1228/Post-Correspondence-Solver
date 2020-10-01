import sys
domino_dict = {}
trailing_dict = {}
open_queue = []
visited = []
max_states = 0
max_queue_length = 0
goal_state_found = False
print_sequence_flag = 0

class Node:
	def __init__(self, strings, parent=None, prev_index=0):
		self.strings = strings
		self.parent = parent
		self.prev_index = prev_index
	def is_valid_state(self):
		if self in visited or self in open_queue:
			return False
		top = self.strings[0]
		bottom = self.strings[1]
		if top.startswith(bottom):
			trailing = '+' + top.replace(bottom,'',1)
			if trailing not in trailing_dict:
				trailing_dict[trailing] = 1
				return True 
			else:
				return False
		elif bottom.startswith(top):
			trailing = '-' + bottom.replace(top,'',1)
			if trailing not in trailing_dict:
				trailing_dict[trailing] = 1
				return True
			else:
				return False
		else:	
			return False

	def is_goal_state(self):
		top = self.strings[0]
		bottom = self.strings[1]
		if top == bottom:
			return True
			goal_state_found = True
			
		

	def generate_child_nodes(self, flag):
		visited.append(self)
		if flag == 0:
			print('popping: %s' % open_queue[0].strings)
			open_queue.pop(0)
		elif flag == 1:
			print('popping: %s' % open_queue[-1].strings)
			open_queue.pop()
		for index in domino_dict.keys():
			current_strings = self.strings
			first_string = domino_dict[index][0]
			second_string = domino_dict[index][1]
			new_node = Node(
			[current_strings[0] + first_string,
			current_strings[1] + second_string],
			self, index)
			if new_node.is_valid_state():
				if new_node.is_goal_state():
					exit_function(1, new_node,1, print_sequence_flag)
				if len(open_queue) < max_queue_length:
					print('appending: %s' % new_node.strings)
					open_queue.append(new_node)
					if len(open_queue) == max_queue_length:
						print('open_queue has reached its maximum. we must now begin depth-first.')
	def print_solution_sequence(self):
		sequence = []
		while self.parent:
			sequence.append(self.prev_index)
			self=self.parent
			
		print('The solution sequence is: %s' % sequence[::-1])

def graph_search(self):
	states=0
	while states < max_states and goal_state_found == False and len(open_queue) < max_queue_length:
		if open_queue == []:
			exit_function(0,'',1)
		open_queue[0].generate_child_nodes(0)
		states+=1
	# Begin DFS
	while states < max_states and goal_state_found == False:
		if open_queue == []:
			exit_function(0,'',1)
		for node in open_queue:
			node.generate_child_nodes(1)
			states+=1

def initialize_graph():
	initial_state = Node(['',''])
	open_queue.append(initial_state)
	initial_state.generate_child_nodes(0)
	graph_search(initial_state)

def exit_function(solutionFound, Node, solutionExists, printSequence):
	if solutionFound == 0 and solutionExists == 1:
		print('No solution found within bounds')
	elif solutionFound == 1:
		print('Goal state %s found!' % Node.strings)
		if printSequence == 1:
			Node.print_solution_sequence()
	elif solutionExists == 0:
		print('No solution exists')

	sys.exit()

def check_if_solution_exists(domino_dict):
	top_items = []
	bottom_items = []
	for key in domino_dict:
		top_items.append(domino_dict[key][0])
		bottom_items.append(domino_dict[key][1])
	if top_items[0] == bottom_items[1] and top_items[1] == bottom_items[0]:
		exit_function(0,'',0, 0)
		
def main():
	try:
#		uncomment an input file to test
		input = open("input1.txt", "r")
#		input = open("input2.txt", "r")
#		input = open("input3.txt", "r")
#		input = open("input4.txt", "r")
#		input = open('knownInput.txt', 'r')
		input_lines = input.readlines()
	except:
		print('Error loading input file.')
		exit(0)

	global max_queue_length
	max_queue_length = int(input_lines[0])
	print('Maximum queue length: %s' % max_queue_length)

	global max_states
	max_states = int(input_lines[1])
	print('Maximum number of nodes to expand: %s' % max_states)	

	global print_sequence_flag
	print_sequence_flag = int(input_lines[2])

	domino_count = input_lines[3]
	dominos = input_lines[4:]


	for domino in dominos:
		index = domino.split()[0]
		top_string = domino.split()[1]
		bottom_string = domino.split()[2]
		domino_dict[index] = [top_string, bottom_string]	

	check_if_solution_exists(domino_dict)
	initialize_graph()

if __name__ == '__main__':
	main()
