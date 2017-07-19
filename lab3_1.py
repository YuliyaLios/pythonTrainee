"""
Вхідні дані: 3 дійсних числа a, b, c. Передаються в програму як аргументи командного рядка.

Результат роботи: рядок "triangle", якщо можуть існувати відрізки з такою довжиною та з них можна скласти трикутник, або "not triangle" -- якщо ні.
"""

import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a > 0 and b > 0 and c > 0:
    if a < (b + c) and b < (a + c)and c < (a + b):
        print ('triangle')
    else:
        print ('not triangle')
else:
    print ('not triangle')
