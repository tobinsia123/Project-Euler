n = 0
for a in range(999, 100, -1):
    for b in range(100, 999, 1):
        x = a*b
        if str(x)[0] == str(x)[-1]:
            if str(x)[1] == str(x)[-2]:
                if str(x)[2] == str(x)[-3]:
                    if x > n:
                        n = x


print(n)