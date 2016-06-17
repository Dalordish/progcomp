fin = open("input.txt","r")
fout = open("output.txt","w")
input = fin.read().split("\n")

print(input)

wood = int(input[0])
cuts = input[1].split("\n")
print(wood)
print(cuts)