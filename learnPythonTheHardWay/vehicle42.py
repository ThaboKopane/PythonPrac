from playsound import playsound
from PIL import Image

class Vehicle(object):
	pass

class Aircraft(Vehicle):
	def __init__(self, type):
		self.type=type;
class Landcraft(Vehicle):
	def __init__(self, type):
		self.type=type;
class Watercraft(Vehicle):
	def __init__(self, type):
		self.type=type;


class FixedWing(Aircraft):
	def __init__(self, type, number):
		super(FixedWing, self).__init__(type)
		self.number = number
	def engine_sound(self):
		playsound("/Users/thabokopane/Documents/python/airp-engine2.wav")

	def imageOfPlan(self):
		image = Image.open('/Users/thabokopane/Documents/python/download.jpeg')
		image.rotate(45).show()


class Helicopter(Aircraft):
	def __init__(self, type, number):
		super(Helicopter, self).__init__(type)
		self.number = number
	def engine_sound(self):
		playsound("/Users/thabokopane/Documents/python/heli-running3.wav")
class Drone(Aircraft):
	def __init__(self, type, number):
		super(Drone, self).__init__(type)
		self.number = number
class Balloon(Aircraft):
	def __init__(self, type, number):
		super(Balloon, self).__init__(type)
		self.number = number

class Motorcycle(Landcraft):
	def __init__(self, type, wheels_max):
		super(Motorcycle, self).__init__(type)
		self.wheels_max=wheels_max
	def engine_sound(self):
		playsound("/Users/thabokopane/Documents/python/synth_voice.wav")
class Automobile(Landcraft):
	def __init__(self, type, wheels_max):
		super(Automobile, self).__init__(type)
		self.wheels_max=wheels_max
	def engine_sound(self):
		playsound("/Users/thabokopane/Documents/python/car-running1.wav")
class Truck(Landcraft):
	def __init__(self, type, wheels_max):
		super(Truck, self).__init__(type)
		self.wheels_max=wheels_max
	def engine_sound(self):
		playsound("/Users/thabokopane/Documents/python/beat_indian.wav")
class Skateboard(Landcraft):
	def __init__(self, type, wheels_max):
		super(Skateboard, self).__init__(type)
		self.wheels_max=wheels_max

class Ship(Watercraft):
	def __init__(self, type, min_size):
		super(Ship, self).__init__
		self.min_size=min_size
class Submarine(Watercraft):
	def __init__(self, type, min_size):
		super(Submarine, self).__init__
		self.min_size=min_size
class Surfboard(Watercraft):
	def __init__(self, type, min_size):
		super(Surfboard, self).__init__
		self.min_size=min_size
class Boat(Watercraft):
	def __init__(self, type, min_size):
		super(Boat, self).__init__
		self.min_size=min_size


if __name__ == "__main__":
	Bike = Motorcycle("Motocycle", 2)
	truckker = Truck("Truck",18)
	chopper = Helicopter("Helicopter", 727)
	fixed = FixedWing("FixedWing", 727)

	print("The bike is moving")
	Bike.engine_sound()
	print("The Helicopter")
	chopper.engine_sound()
	print("The sound of the eighteen wheeler")
	truckker.engine_sound()
	print("The sound of a fixed wing")
	fixed.imageOfPlan()
	fixed.engine_sound()