'''
Script to generate undirectional graph formated as 
matrix of connections. 
Created graph can be:
1. Randomly connected
2. Fully connected (without self-loops)
3. Empty of connections
'''

import argparse
import random

def arguments():
	parser = argparse.ArgumentParser()

	mode = parser.add_mutually_exclusive_group()
	mode.add_argument("-f", "--full", action='store_true',
		help="create fully connected graph (default)")
	mode.add_argument("-r", "--random", action='store_true',
		help="create graph with random connections")
	mode.add_argument("-e", "--empty", action='store_true',
		help="create empty graph (no connections)")

	required = parser.add_argument_group('required arguments')
	required.add_argument("-n", "--nodes", 
		help="number of nodes in graph", required=True)

	return parser.parse_args()

def create_matrix(args, n, default_random):
	# Randomly connected graph
	if args.random or default_random:

		# Create zeroed numpy 2D array
		matrix = [[0 for x in range(n)] for y in range(n)] 

		# Randomize connections only at and above main diagonal of matrix
		x = 1
		for i in range(0, n):
			for j in range(x, n):
				matrix[i][j] = random.randint(0, 1)
			x += 1

		# Make matrix symmetrical by main diagonal
		y = 1
		for i in range(0, n):
			for j in range(y, n):
				matrix[j][i] = matrix[i][j]
			y += 1

	# Fully connected graph (without self-loops)
	elif args.full:

		# Fill matrix with ones
		matrix = [[1 for x in range(n)] for y in range(n)]

		# On main diagonal put zeroes
		for i in range(0, n):
			matrix[i][i] = 0

	# Empty of connections
	elif args.empty:
		matrix = [[0 for x in range(n)] for y in range(n)]

	return matrix

def generate():
	# Parsing arguments
	args = arguments()

	# If mode is not provided, default to randomly connected
	default_random = False
	if not (args.random or args.full or args.empty):
		default_random = True

	# Save number of nodes
	num_of_nodes = int(args.nodes)

	# Fill matrix based on mode
	matrix = create_matrix(args, num_of_nodes, default_random)

	return matrix, num_of_nodes