def add(a,b):
	print(f"ADDING {a}+{b}")
	return a+b

def subtract(a,b):
	print(f"SUBTRACTING {a} - {b}")
	return a -b

def multiply(a,b):
	print(f"MULTIPLYING {a} * {b}")
	return a*b

def divide(a,b):
	print(f"DIVIDE {a}/{b}")
	return a/b

print("enter the values of x & y")
x = int(input())
y = int(input())
age = add(x,y)
height = subtract(170,4)
weight = multiply(65, 2)
iq = divide(280, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

whatBYH = (height - ((iq/2)*weight))+age
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))


print("by hand it is equal to: ", whatBYH)
print("That becomes: ",what)
