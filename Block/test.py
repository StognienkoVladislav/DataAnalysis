

mas = [13, 123, 145]

z = 1
maX = [x for x in sorted(mas)[-3:]]
for x in maX:
    z *= x
print(z)