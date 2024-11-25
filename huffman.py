
import heapq 

# It has:
# huff: Direction of the branch (0 for left, 1 for right).

class node: 
	def __init__(self, freq, symbol, left=None, right=None): 
		# frequency of symbol 
		self.freq = freq 

		# symbol name (character) 
		self.symbol = symbol 

		# node left of current node 
		self.left = left 

		# node right of current node 
		self.right = right 

		# tree direction (0/1) 
		self.huff = '' 

	def __lt__(self, nxt): 
		#  compare nodes based on their frequency (freq). It ensures the node with the smallest frequency is processed first.
		return self.freq < nxt.freq 



def printNodes(node, val=''): 

	# huffman code for current node The function starts at the root node and traverses down the tree.
	newVal = val + str(node.huff) 

	# if node is not an edge node 
	# then traverse inside it 
	if(node.left): 
		printNodes(node.left, newVal) 
	if(node.right): 
		printNodes(node.right, newVal) 

	# if node is edge node then 
	# display its huffman code 
	if(not node.left and not node.right): #if a node is a leaf node (no left or right child), print the character and its Huffman Code.
		print(f"{node.symbol} -> {newVal}") 


# characters for huffman tree 
chars = ['a', 'b', 'c', 'd', 'e', 'f'] 

# frequency of characters  how many times they are appear in the string
# The goal is to create shorter codes for characters with higher frequencies 
freq = [5, 9, 12, 13, 16, 45] 

# list containing unused nodes 
nodes = [] 

# converting characters and frequencies 
# into huffman tree nodes All nodes are pushed into a priority queue (heapq), which ensures the smallest frequencies are processed first.
for x in range(len(chars)): 
	heapq.heappush(nodes, node(freq[x], chars[x])) 


while len(nodes) > 1: 

	# sort all the nodes in ascending order 
	# based on their frequency two nodes with the smallest frequencies are removed from the queue 
	left = heapq.heappop(nodes) 
	right = heapq.heappop(nodes) 

	# assign directional value to these nodes 
	left.huff = 0
	right.huff = 1

	# combine the 2 smallest nodes to create 
	# new node as their parent 
	newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right) #sum of two child node frequencies & symbole 

	heapq.heappush(nodes, newNode) #This node is pushed back into the queue.


printNodes(nodes[0]) 

# Output:
#f -> 0
# c -> 100
# d -> 101
# a -> 1100
# b -> 1101
# e -> 111
# This means:

# f gets the shortest code (0) as it has the highest frequency.
# a gets a longer code (1100) as it has the lowest frequency.

# Huffman Coding is a compression algorithm used to minimize the storage required for data. 
# it assigns shorter binary codes to characters that occur more frequently and longer binary codes to characters that occur less frequently. 
# data structure is used to implement the priority queue? heapq in Python.

# How Backtracking Works:

# When traversing the tree, the function keeps adding 0 or 1 to the code (val).
# If the function reaches a leaf node, it prints the code.
# After printing, the function backtracks to explore other branches of the tree.
# Why Backtracking?

# It ensures all paths (left and right subtrees) are explored to generate the correct Huffman Code for each character.

# O(n log n) 