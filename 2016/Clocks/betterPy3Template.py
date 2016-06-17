fin = open("input.txt","r")
fout = open("output.txt","w")
input = fin.read().split("\n")
input.pop(0)
print(input)

hours = {
	"00":"midnight",
	"01":"1am",
	"02":"2am",
	"03":"3am",
	"04":"4am",
	"05":"5am",
	"06":"6am",
	"07":"7am",
	"08":"8am",
	"09":"9am",
	"10":"10am",
	"11":"11am",
	"12":"noon",
	"13":"1pm",
	"14":"2pm",
	"15":"3pm",
	"16":"4pm",
	"17":"5pm",
	"18":"6pm",
	"19":"7pm",
	"20":"8pm",
	"21":"9pm",
	"22":"10pm",
	"23":"11pm",
	"24":"midnight"
}

minutes = {
	"15": "a quarter past " ,
	"30": "half past ",
	"45": "a quarter to "
}

for i in input:
	buffer = ""
	print(i)
	hour = i[0:2]
	minute = i[2:4]
	buffer += i + " is "

	if minute == "00":
		pass
	elif minute == "01":
		buffer += "a minute past " 
		pass
	elif minute in minutes:
		buffer += minutes[minute]
	elif int(minute) > 30:
		buffer += minute + " minutes to "
	elif int(minute) > 30:
		hours = str(int(hours) + 1)
	elif minutes > 9:
		buffer += minute + " minutes past "
	else:
		buffer += minute[0] + " minutes past "

	buffer += hours[hour]
	buffer += "\n"


	print(buffer)
	fout.write(buffer)




#if 15
# if 30
#if <30
#if >30
#if after 12
# if 12
# if 00