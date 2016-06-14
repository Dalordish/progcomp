fin = open("input.txt","r")
fout = open("output.txt","w")
input = fin.read().split("\n")
input.pop(0)
print(input)

keys = {}
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num = [1,1,1]
buffer = ""
conArray = [[],[]]

def incNum(numb):
	if numb[2] == 3:
		if num[1] == 3:
			num[0] = numb[0] + 1
			num[1] = 1
			num[2] = 1
		else:
			num[1] = numb[1]+ 1
			num[2] = 1
	else:
		num[2] = num[2] + 1

for i in input[0].lower(): #import secret
	if i in keys:
		pass
	else:
		keys[i] = str(num[0]) + str(num[1]) + str(num[2])
		incNum(num)
if "" not in keys:
	keys[" "] = str(num)
	incNum(num)

for x in alphabet: #Alphabet
	if x in keys:
		pass
	else:
		keys[x] = str(num[0]) + str(num[1]) + str(num[2])
		incNum(num)

for sent in input:
	for x in range(0,len(sent)):
		vert = keys[sent[x].lower()]
		conArray[x][0] = vert[0]
		conArray[x][1] = vert[1]
		conArray[x][2] = vert[2]
		print(conArray)