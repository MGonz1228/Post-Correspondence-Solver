import sys
domino_dict = {}
trailing_dict = {}
open_queue = []
visited = []
max_states = 0
max_queue_length = 0
goal_state_found = False

class Node:
	def __init__(self, strings):
		self.strings = strings

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
			
		

	def generate_child_nodes(self):
		visited.append(self)
		print('Removing state from queue: %s' % open_queue[0].strings)
		open_queue.pop(0)
		
		# generate child nodes, append valid child nodes to open queue
		for index in domino_dict.keys():
			current_strings = self.strings
			first_string = domino_dict[index][0]
			second_string = domino_dict[index][1]
			new_node = Node(
			[current_strings[0] + first_string,
			current_strings[1] + second_string])
			if new_node.is_valid_state():
				if new_node.is_goal_state():
					exit_function(1, new_node.strings,1)
				if len(open_queue) < max_queue_length:
					print('appending %s' % new_node.strings)
					open_queue.append(new_node)
					print('queue length %s' % len(open_queue))
				else:
					print('open_queue has reached its maximum. we must now begin depth-first.')


# function graph_search(problem) returns a solution or false:
# init frontier using initial state
# init empty explored set
# loop:
	# choose a node from the frontier
	# check if node doesn't suck
	# add node to explored
	# add new reachable nodes to frontier if not explored/already in

def graph_search(self):
	states=0
	while states < max_states and goal_state_found == False:
		if open_queue == []:
			exit_function(0,'',1)
		open_queue[0].generate_child_nodes()
		states+=1

def initialize_graph():
	initial_state = Node(['',''])
	open_queue.append(initial_state)
	initial_state.generate_child_nodes()
	graph_search(initial_state)

def exit_function(solutionFound, strings, solutionExists):
	# TODO store path give the option to print the path
	if solutionFound == 0 and solutionExists == 1:
		print('No solution found within bounds')
	elif solutionFound == 1:
		print('Goal state %s found!' % strings)
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
		exit_function(0,'',0)
		
def main():
#	input = open("input1.txt", "r")
	input = open("input2.txt", "r")
#	input = open("input3.txt", "r")
#	input = open("input4.txt", "r")
#	input = open('knownInput.txt', 'r')
	input_lines = input.readlines()

	global max_queue_length
	max_queue_length = int(input_lines[0])
	print('Maximum queue length: %s' % max_queue_length)

	global max_states
	max_states = int(input_lines[1])
	print('Maximum number of nodes to expand: %s' % max_states)	

	print_sequence_flag = input_lines[2]
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
