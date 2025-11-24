#Map Function - map(function, iterable)
#             - Returns an iterator that applie function to every item of iterable

#Finding even numbers in an array

def make_even(num):
    if num % 2 == 1:
        return num + 1
    else:
        return num

x = [551, 641, 891, 122, 452, 223, 234, 343, 562, 115, 554, 111, 679, 516]

y =  list(map(make_even, x))
print(y)
