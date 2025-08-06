numbers = eval(input('list the numbers'))
numbers.sort()
a = numbers[0]
b = numbers[1]
if a + b == numbers[3]:
    c = numbers[4]
elif a + b == numbers[4]:
    c = numbers[3]

print(f'{a} {b} {c}')