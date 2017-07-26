"""
Вхідні дані: довільна, відмінна від нуля, кількість значень - аргументів командного рядка. Значеннями-аргументами можуть бути числа або рядки, які складаються з цифр та літер латинського алфавіту без пробілів.

Результат роботи: рядок, що складається з отриманих значень в зворотньому порядку, записаних через пробіл. Пробіл в кінці рядка відсутній.
"""

import sys

a = sys.argv[1:]
a_list = list(reversed(a))    
new_a = " ".join(a_list)
print new_a