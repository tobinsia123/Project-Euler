x = 0

def factors(z):
    count = 0
    for j in range(1, z + 1):
        if z % j == 0:
            count = count + 1
    if count == 500:
        print("Number:", x)

for i in range(76576500,76576501, 1):
    x = x + i
    factors(x)

