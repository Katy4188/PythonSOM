import numpy as np

class PrintColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Node(object):

	# attributes for a node are its weight, its position in the lattice, and the coordinates of its edges if you imagine a box around the node 
	def __init__(self, edgeLeft, edgeTop, edgeRight, edgeBottom, numberOfWeights):
		self.edgeLeft = edgeLeft
		self.edgeTop = edgeTop
		self.edgeRight = edgeRight
		self.edgeBottom = edgeBottom
		self.numberOfWeights = numberOfWeights
		self.nodesWeights = [] 

	# initialise the weights to small random variables
	def InitialiseWeights(self):
   		n = self.numberOfWeights
		s = 0

		for s in range(1, n+1):

			valueOfWeight = np.random.random_sample()
			print("Weight " + str(s) + " is initalised to " + str(valueOfWeight) + " ")
			self.nodesWeights.append(valueOfWeight)
			s+=1	
			print(PrintColors.WARNING + "List with the weight of the current node is: " + str(self.nodesWeights) + "\n") + PrintColors.ENDC
			
	

	def CalculateTheNodesCenter(self):
		centerx = self.edgeLeft + (self.edgeRight - self.edgeLeft)/2
     		centerY = self.edgeTop + (self.edgeBottom - self.edgeTop)/2

	# returns the euclidean space (squared) between the node's weight and the input vector, so the BMU can be found
	def CalculateDistance(self, inputVector):
		distance = 0
		s = 0 
		n = len(self.nodesWeights)
		for s in range(0, n):
			distance += (inputVector[s] - self.nodesWeights[s]) * (inputVector[s] - self.nodesWeights[s])
		print("The Distance between the " + str(inputVector) + " and " + str(self.nodesWeights) + " is " + str(distance) + "\n") 
		return distance
                 			
	# given a learning rate and a target vector this function adjusts the node's weights accordingly 
  	def AdjustWeights(self, target, learningRate, influence):
		s = 0
		n = len(target) 
		print(PrintColors.OKBLUE + "Current Weight of this node is " + str(self.nodesWeights))
		for s in range(0, n):
			x = self.nodesWeights[s]
			self.nodesWeights[s] += learningRate * influence * (target[s] - self.nodesWeights[s])
		print("Weight of node with edges " + str(self.edgeLeft) + ", " + str(self.edgeTop) + ", " +  str(self.edgeRight) + ", " + str(self.edgeBottom) + " is adjusted to" + str(self.nodesWeights) + "\n" + PrintColors.ENDC) 


if __name__ == "__main__":
	x = Node(1,2,3,5,3)
	x.InitialiseWeights()
	testTargetVector = [0.2, 0.5, 0.8]
	print(PrintColors.OKGREEN + str(len(testTargetVector)))
	x.CalculateDistance(testTargetVector)
 	x.AdjustWeights([0.8, 0.9, 0.3], 0.5, 0.88888888) 
