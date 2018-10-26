from sys import argv

script, filename = argv

print(f"We're goign to erase {filename}")
print("else hit CTRL-C")
print("else ENTER")

input("?")

print("Opening the file...")
target = open(filename, "w")

print("Truncating")
target.truncate()

print("three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1+"\n")
target.write(line2+"\n")
target.write(line3+"\n")

target.close()