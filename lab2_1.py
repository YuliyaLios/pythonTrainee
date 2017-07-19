"""
Вхідні дані: 3 дійсних числа -- аргументи командного рядка.

Вихідні дані: результат обчислення формули: https://upload.wikimedia.org/math/2/9/d/29ddb53a3b131631bd9da67ccbc3ec76.png
Аргументи передаються в порядку, зазначеному у формулі, назви змінних можуть використовуватися будь-які.
"""

import sys
import math

x = float(sys.argv[1])
m = float(sys.argv[2])
s = float(sys.argv[3])

f = 1 / (s * (2*math.pi)**0.5) * math.e**(- (x - m)**2 / (2*s**2))

print f
