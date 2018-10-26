from sys import argv

script, filename = argv #argv is used for argument passing like java

txt = open(filename) 

print(f"Here is your {filename}")

print(txt.read())

print("Type your filename")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())