import sys
sys.setrecursionlimit(10000)
def cipher(number):
	output = 0
	numstr = str(number)
	for i in range(0,len(numstr)):
		output = int(numstr[i])*int(numstr[i]) + output
		print(output)
	if output == 1:
		return "YES"
	else:
		cipher(output)

try:
	print(cipher("2")) #input number here
except:
	print("no")