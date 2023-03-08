limit = int(input("Input number: "))
total = 0
a = 1
b = 1
c = a + b
while c < limit:
    total = total + c
    a = b + c
    b = c + a
    c = a + b
print(total)