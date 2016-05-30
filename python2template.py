import math
 
fin = open('input.txt', 'r')     # open the file to read
fout = open('output.txt', 'w') # open the file to write
 
TT = int(fin.readline()) # find the number of cases
#print TT
for T in xrange(0, TT): # read through each test case
    # read the line (use int(x) if necessary!)
    line = [x for x in fin.readline().split()]
    print line
    # alternatively, if numbers are fixed, you could do:
    # a, b = [int(x) for x in fin.readline().split()]
     
    # do more bullshit if necessary
     
fin.close() # keep it clean
fout.close()

#make sure input.txt has the amount of lines as the first line as per progcomp
