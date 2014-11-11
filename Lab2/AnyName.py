class Animal():
	
	def __init__(self, name, age):
		self.name=name
		self.age=age
	
	def sleep(self):
		print str(self.name) + " of " + str(self.age) + " is sleeping" 
	def eat(self, food):
		print str(self.name) + " of " + str(self.age) + " is eating " + food

class Bird(Animal):
	def __init__(self, name, age, wingscolor):
		Animal,__init__(self, name,age)
		self.wingscolor=wingscolor 
	def fly(self):
		print str(self.name) + " of " + str(self.age) + " has " + srt(self.wingscolor) + " wings"

x=Animal("meet", 11)
x.sleep()
x.eat("Apple")
y=Animal("cat", 2)
y.sleep()
y.eat("pizza")
z=Bird("Roni", "17", "Blue")
z.fly()
