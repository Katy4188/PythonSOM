class Roboter: 

	def __init__(self, name, baujahr):
		self.name = name
		self.baujahr = baujahr

 	
	def SageHallo(self):
		print("Hallo, mein Name ist " + self.name)

	def NeuerName(self, name):
		self.name = name 

 	def HoleNamen(self):
		return self.name

	def NeuesBaujahr(self, baujahr):
		self.baujahr = baujahr

	def HoleBaujahr(self):
		return str(self.baujahr)

if __name__ == "__main__":
	x = Roboter("Marvin", 1979)
	y = Roboter("Caliban", 1993)
	for rob in [x, y]:
		rob.SageHallo()
		print("Ich bin " + rob.HoleBaujahr() + " erschaffen worden! ")



Roboter.number = 1000

print (Roboter.number)








