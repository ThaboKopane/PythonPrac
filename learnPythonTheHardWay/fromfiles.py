from sys import argv

from os.path import exists
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# read from the other file
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the ouput file exists? {exists(to_file)}")

print("Ready, hit ENTER to continue, CTRL-C to cancel")
input()

# open and write the data to the other file
out_file = open(to_file, "w")
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()