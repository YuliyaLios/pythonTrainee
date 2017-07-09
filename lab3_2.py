import sys

n = int(sys.argv[1])
counter = 0
fib1 = 0
fib2 = 1
fib_res = None
if n == fib1:
    print(fib1)
elif n == fib2:
    print(fib2)
else:
    for counter in range(n-1):
        fib_res = fib1 + fib2
        fib1 = fib2
        fib2 = fib_res
    print fib_res
