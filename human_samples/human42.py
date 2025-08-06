array = []

file = open("text.txt", "r")
contents = file.read()
file.close()
array = contents.split(" ")
array = [int(i) for i in array]

array.sort()
medianposition = int((len(array)+1)/2)
print(array[medianposition-1])

#Ans = 521
