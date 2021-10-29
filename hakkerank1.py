def fizzBuzz(n):
    for i in range (1,(n+1)):
        if (i%3==0):print("Fizz",end="")
        if (i%5==0):print("Buzz")
        else:print(i)
a=int(input("Input here"))
fizzBuzz(a)
