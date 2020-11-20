import string

connector = "+"
filename = "dummy.txt"
s = "this is the first try of github action"

tokens = s.split()

with open(filename, "a+") as f:
	f.write(connector.join(tokens)+"\n")

