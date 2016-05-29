#Initial pass - no template or file io yet

input = "the quick brown fox"
 
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
 
lower = input.lower()
for i in lower:
	if i in alphabet:
		alphabet.remove(i)
if len(alphabet) == 0:
	print("panagram")
else:
	print("Not a pangram, does not contain:",end='',)
	for i in alphabet:
		print(i,end='', sep = '')
