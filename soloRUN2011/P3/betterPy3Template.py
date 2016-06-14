fin = open("input.txt","r")
fout = open("output.txt","w")
input = fin.read().split("\n")
input.pop(0)
print(input)

vals = {
	
}
from collections import OrderedDict

for n in range(1,21):
	vals[n] = "S" +str(n)
	vals[n*2] = "D" + str(n)
	vals[n*3] = "T" + str(n)
vals[50] = "IB"
vals[25] = "OB"
sortedKeys = sorted(vals.keys(),reverse = True)
print(sortedKeys)
#sorted(vals,reverse = True)

def check(goal):
	if goal > 180:
		return([T20,T20,T20])
	else:
		for i in sortedKeys:
			if i < goal:
				pass
			else:
				pass
			#print(i)

print(check(60))

# REALLY GUYS
# TRAVELLING SALESMAN?
# FUCK YOU