import numpy as np


class Node(object):

	# attributes for a node are its weight, its position in the lattice, and the coordinates of its edges if you imagine a box around the node 
	def __init__(self, edgeLeft, edgeTop, edgeRight, edgeBottom, numberOfWeights):
		self.edgeLeft = edgeLeft
		self.edgeTop = edgeTop
		self.edgeRight = edgeRight
		self.edgeBottom = edgeBottom
		self.numberOfWeights = numberOfWeights


	# initialise the weights to small random variables
	def InitialiseWeights(self):
   		n = self.numberOfWeights
		s = 0
                nodesWeights = []
		for s in range(1, n+1):

			valueOfWeight = np.random.random_sample()
			print("Weight " + str(s) + " is initalised to " + str(valueOfWeight) + "\n")
			nodesWeights.append(valueOfWeight)
			s+=1	
			print("List with the weight of the current node is: " + str(nodesWeights) + "\n")
	
	def CalculateTheNodesCenter(self):
		centerx = self.edgeLeft + (self.edgeRight - self.edgeLeft)/2
		centerY = self.edgeTop + (self.edgeBottom - self.edgeTop)/2


if __name__ == "__main__":
	x = Node(1,2,3,5,7)
	x.InitialiseWeights() 
