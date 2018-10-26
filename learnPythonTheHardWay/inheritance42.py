
from playsound import playsound



class Animal(object):
	pass

##Specific animal
class Dog(Animal):

	def __init__(self, name):
		self.name=name

	def bark(self):
		playsound("/Users/thabokopane/Documents/python/dog-bark1.wav")

class Cat(Animal):

	def __init__(self, name):
		self.name=name

	def cat_sound(self):
		playsound("/Users/thabokopane/Documents/python/cat-kitten1.wav")

class Person(object):

	def __init__(self, name):
		self.name=name

		self.pet=None

class Employee(Person):

	def __init__(self, name, salary):

		super(Employee, self).__init__(name)
		self.salary=salary

class Fish(object):
	pass
class Salmon(Fish):
	pass
class Halibut(Fish):
	pass


rover =Dog("Rover")
satan =Cat("Satan")
mary=Person("Mary")
mary.pet=satan
frank=Employee("Frank",120000)

frank.pet=rover
flipper=Fish()
crouse=Salmon()
harry=Halibut()
print("the cat is meouwing")
satan.cat_sound()
print("the dog barking")
rover.bark()

"""frank.pet=rover
flipper=Fish()
crouse=Salmon()
harry=Halibut()
satan.cat_sound()"""

#if __name__ == "__main__":
	