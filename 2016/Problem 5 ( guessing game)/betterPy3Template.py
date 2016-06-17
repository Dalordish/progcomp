import math

def encode(g):
	k = 0
	r = 0
	for i in str(g):
		c = int(i)
		d = (3*c +7) %10
		r = r + 2**(3*d+2) + k*(8**d)
		k = k+1
	return(r)

def match(gcode,scode):
	b = ""
	c = ""

	for k in range(0,10):
		print(k)
		p = math.floor(gcode/(8**k) % 8)
		q = math.floor(scode/(8**k) % 8)
		r = q - p
		s = (2*r) + (3*q)
		if s > 11 and s > (2*r):
			if s == (3*p):
				b += "B"

			else:
				c += "C"
	return(b,c)

print(encode("0586"))