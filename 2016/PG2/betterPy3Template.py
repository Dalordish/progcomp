fin = open("input.txt","r")
fout = open("output.txt","w")
input = fin.read().split("\n")
people = input[0].split(" ")[0]
groups = input[0].split(" ")[1]

input.pop(0)

list = []

for x in range(0,len(input)):
	print(x)
	list.append(input[x].split(" "))

print(list)

def findNext(current,used):
	if current == 0:
		len(list)
	if used < len(list)
	list.pop(used[1])
