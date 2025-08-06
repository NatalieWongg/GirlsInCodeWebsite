def fibonacci(n):
  if n==0:
      return 7
  elif n==1:
      return 9
  else:
      a = fibonacci(n-1)
      b = fibonacci(n-2)
      return (3*a) + (2*b)


number = int(input('How many terms of the fibonacci sequence do you want to see? '))
for i in range(number):
   print(fibonacci(i))