for x in range(1, 1000, 1):
    for y in range(1, 1000, 1):
        for z in range(1, 1000, 1):
            if x + y + z == 1000:
                if x**2 + y**2 == z**2:
                    print(x)
                    print(y)
                    print(z)