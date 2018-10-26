
class Student:

	def __init__(self, firstName, middleName, lastName):
		self.__firstName=firstName
		self.__middleName=middleName
		self.__lastName=lastName

	def setNames(self, first, middle, last):
		self.__firstName = first
		self.__middleName = middle
		self.__lastName =last

	def getFullName(self):
		return (self.__firstName+" "+self.__middleName[0]+". "+self.__lastName)


class UberService:

	def __init__(self, Name, costPerMin, costPerKM, baseFee, cancelFee):
		self.__Name = Name
		self.__costPerMin=costPerMin
		self.__costPerKM=costPerKM
		self.__baseFee=baseFee
		self.__cancelFee=cancelFee
	def setDetails(self, name, costPerMin, costPerKM, baseFee, cancelFee):
		self.__Name = name
		self.__cancelFee=cancelFee
		self.__baseFee=baseFee
		self.costPerKM=costPerMin
		self.__costPerKM=costPerKM
	def setName(self,name):
		self.__Name=name
	def getName(self):
		return self.__Name
	def setCostPerMinute(self, cents):
		self.__costPerMin=cents
	def getCostPerMinute(self):
		return self.__costPerMin
	def setCostPerKilometre(self, cents):
		self.__costPerKM=cents
	def getCostPerKilometre(self):
		return self.__costPerKM
	def setBaseFare(self, cents):
		self.__baseFee=cents
	def getBaseFare(self):
		return self.__baseFee
	def setCancelFee(self, amount):
		self.__cancelFee=amount
	def getCancelFee(self):
		return self.__cancelFee
	def calculateFare(self, minutes, distance):
		return (self.__costPerMin*minutes+self.__costPerKM*distance+self.__baseFee)


class Collator:
	def __init__(self, label):
		self.__label = label
	def label(self, newLabel):
		self.__label=newLabel
	def recordReding(self, reading):
		pass
	def label(self):
		return self.__label
	def maximum(self):
		pass
	def minimum(self):
		pass
	def average(self):
		pass
	def numberOfReadings(self):
		pass

if __name__ == "__main__":
	Thabo = Student("Thabo", "Thadishi", "Kopane")
	myUber = UberService("Thabo", 2.0, 4.5, 10, 20)
	print(Thabo.getFullName())
	print(myUber.calculateFare(20, 20))