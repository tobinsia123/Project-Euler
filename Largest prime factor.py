import math

# requesting an input from the user
x = int(input("Input a number: "))

# setting the largest prime factor originally to 0
max_prime = 0

# modulo the input and divide it by 2 till it is an odd number
while x % 2 == 0:
    maxPrime = 2
    x = x / 2

# Every composite number has a proper factor less than or equal to its square root, proof by contradiction
for i in range (3, int(math.sqrt(x)) + 1, 2):
    while x % i == 0:
        maxPrime = i
        x = x/i

print("The largest prime Factor of number is ", int(maxPrime))
