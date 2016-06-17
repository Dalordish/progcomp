fin = open("input.txt","r")
fout = open("output.txt","w")
input = fin.read().split("\n")
input.pop(0)
print(input)

vals = {
	"M":1000,
	"D":500,
	"C":100,
	"L":50,
	"X":10,
	"V":5,
	"I":1
}
def if1(letters):
	for x in letters:
		if x in vals:
			pass
		else:
			return("bad1")
		return(1)

def if2(letters):
	current = 0
	for i in range(0,len(letters)):
		if current > vals[i]:
			return("bad2")
		else:
			current = vals[i]

for x in input:
	print(x)
	let = list(x)
	print(if2(let))