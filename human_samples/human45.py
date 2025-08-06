#70x70 grid
array = []
file = open("text.txt", "r")
with open('text.txt') as f:
   array = f.read().splitlines()
for i in range(len(array)):
   e = array[i].split(" ")


char = ''
normal = 0
oddi = 0
numofonesi = []
oddj = 0
numofonesj = []
for i in range(70):
   numofonesi.append(0)
   numofonesj.append(0)


#row search
for i in range(70):
   for j in range(70):
       char = (array[i])[j]
       if char == '1':
           numofonesi[i] = numofonesi[i] + 1
if numofonesi[0] == numofonesi[1]:
   normal = numofonesi[0]
   for i in range(70):
       if numofonesi[i] != normal:
           oddi = i+1
           break
else:
   if numofonesi[0] == numofonesi[2]: #odd is index 1
       oddi = 2
   else:
       oddi = 1
print(oddi)


#column search
for i in range(70):
   for j in range(70):
       char = (array[j])[i]
       if char == '1':
           numofonesj[i] = numofonesj[i] + 1
if numofonesj[0] == numofonesj[1]:
   normal = numofonesj[0]
   for i in range(70):
       if numofonesj[i] != normal:
           oddj = i+1
           break
else:
   if numofonesj[0] == numofonesj[2]: #odd is index 1
       oddj = 2
   else:
       oddj = 1
print(oddj)