# This program calculates the next number
## in the Fibonacci sequence after
### your input number.
#########################################

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Please enter your number : "))
print(fib(n))         
