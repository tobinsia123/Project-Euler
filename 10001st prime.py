limit = 10001
i = 3
count = 1
prime = 2

while count < limit:
    for x in range(3, int(i ** 0.5) + 1, 2):
        if i % x == 0:
            break
    else:
        prime = i
        count += 1

    i += 2

print(prime)