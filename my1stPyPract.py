import sys
import math

x = float(sys.argv[1])
m = float(sys.argv[2])
s = float(sys.argv[3])

f = 1 / (s * (2*math.pi)**0.5) * math.e**(- (x - m)**2 / (2*s**2))

print f
