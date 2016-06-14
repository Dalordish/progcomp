import sys
sys.setrecursionlimit(1000)
seed = 64493

def calculate(seed,iter):

	num = seed*seed
	strnum = str(num)
	if len(str(num)) != 10:
		for i in range(0, 10-len(strnum)):
			strnum = "0" + strnum
		num = float(strnum)
	# We have 10 digits now
	newnum = strnum[2] + strnum[3] + strnum[4] + strnum[5] + strnum[6]
	if newnum == seed:
		#return("is cycle")
		print("is cycle")
	elif iter == 100:
		#return(" Hundred Element" + str(num))
		print(" Hundred Element" + str(num))
	elif num == 0:
		#return("Degenerate" )
		print("Degenerate")
	else:
		calculate(float(newnum),iter+1)

print(calculate(seed,1))