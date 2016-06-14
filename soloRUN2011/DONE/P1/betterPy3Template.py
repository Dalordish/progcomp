fin = open("input.txt","r")
fout = open("output.txt","w")
input = fin.read().split("\n")
input.pop(0)
print(input)

#initialise

dict = {
	"M": 1000,
	"D": 500,
	"C": 100,
	"L": 50,
	"X": 10,
	"V": 5,
	"I": 1
}
print(dict)

for line in input:
	total = 0
	buffer = ""
	print(line)
	for i in line:
		if i in dict:
			total = total + dict[i]
	print(total)
	buffer = str(total) + " " + line + "\n"
	print(buffer)
	fout.write(buffer)