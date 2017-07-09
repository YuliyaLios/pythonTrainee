import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

str1 = 'la'
str2 = ' ' + str1 + ('-' + str1) * (x-1)
if z == 1:
    str3 = '!'
else:
    str3 = '.'
song = 'Everybody sing a song:' + str2 * y + str3

print song
