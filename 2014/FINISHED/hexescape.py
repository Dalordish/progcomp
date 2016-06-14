fin = open("input.txt","r")
fout = open("output.txt","w")
input = fin.read().split("\n")
input.pop(0)
buffer = ""
test = ""
hack = 0
print(input)
for data in input:
	for letter in range(0,len(data)):
		if data[letter] == "%":
			hex = data[letter +1] + data[letter + 2]
			val = chr(int(hex,16))
			buffer += val
			hack = 2

		else:
			if hack != 0:
				hack = hack-1
			else:
				buffer += data[letter]
	fout.write(buffer)
	fout.write("\n")
	test += buffer
	buffer = ""
print("new")
print(test)