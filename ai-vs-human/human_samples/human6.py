
primeNumbers = []
for x in numbers:
    isPrime = True
    for y in range(2,int(x**0.5)+1):
        if x%y == 0:
            isPrime = False
                
    if isPrime == True:
        primeNumbers.append(x)
print(set(primeNumbers))