import math

fin = open("input.txt","r")
fout = open("output.txt","w")
input = fin.read().split("\n")
input.pop(0)
print(input)


def area(a,b,c):
	s = (a+b+c)/2
	return(math.sqrt(s*(s-a)*(s-b)*(s-c)))

def canExist(a,b,c):
	order = sorted([a,b,c])
	a = order[0]
	b = order[1]
	c = order[2]
	if a + b > c:
		return(1)
	else:
		return(0)

def angle(a,b,c):
	order = sorted([a,b,c])
	a = order[0]
	b = order[1]
	c = order[2]

	if a*a + b*b == c*c:
		return("right-angled")
	elif a*a + b*b > c*c:
		return("acute")
	elif a*a + b*b < c*c:
		return("obtuse")

def type(a,b,c):
	order = sorted([a,b,c])
	a = order[0]
	b = order[1]
	c = order[2]

	if a == b == c:
		return("equalateral")
	elif a == b or b == c:
		return("isoceles")
	else:
		return("scalene")


for line in input:
	buffer = ""
	vals = line.split(" ")
	a = float(vals[0])
	b = float(vals[1])
	c = float(vals[2])
	if canExist(a,b,c) == 1:
		buffer = line + " is " + type(a,b,c) + " & " + angle(a,b,c) + ". " + "Area = " + str(area(a,b,c)) + "\n"
	else:
		buffer = line + " is not a triangle" +"\n"

	print(buffer)
	fout.write(buffer)
