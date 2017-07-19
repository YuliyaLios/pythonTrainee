"""
Вхідні дані: 2 невід'ємних дійсних числа a та b -- аргументи командного рядка. b не дорівнює 0.

Вихідні дані: дійсне число -- результат обчислення формули: https://courses.prometheus.org.ua/assets/courseware/f3cc3947fcf1f8d732729a7a8bd08007/c4x/KPI/Programming101/asset/sandbox2_1.gif
"""

import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])

x = (a*b)**0.5 / (math.e**a * b) + math.e**(2*a/b) * a

print x
