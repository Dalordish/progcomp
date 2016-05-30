#Initial pass - no template or file io yet

input = "71368054"
type = "e"

new = []
odd = 0
even = 0

for i in range(0,len(input)):
	if i % 2 == 0 and i != 0:
		if int(input[-i]) * 2 > 9:
			temp = str(int(input[-i])*2)
			#print(temp)
			even = even + int(temp[0]) + int(temp[1])
			#print(int(temp[0]))
			#print(int(temp[1]))
			#print(int(temp[0]) + int(temp[1]))
			#print("new")
	else:
		print(input[-i])
		odd = odd + int(input[-i])
		
print(even+odd)
