import sys
a = str(sys.argv[1])
a = ''.join(a.split())
a = a.upper()
a = list(a)
b = list(reversed(a))
if a == b:
  print("YES")
else:
  print("NO")
