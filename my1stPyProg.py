import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])

x = (a*b)**0.5 / (math.e**a * b) + math.e**(2*a/b) * a

print x
