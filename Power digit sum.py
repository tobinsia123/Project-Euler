x = 2**1000
y = 0

for i in range(0, len(str(x)), 1):
    z = str(x)[i]
    y = y + int(z)

print(y)
