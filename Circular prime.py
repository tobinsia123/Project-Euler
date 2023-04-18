import math

def chkPrime(num):
    ret = 0
    if num == 2:
        ret = num
    elif num > 2:
        chk = math.ceil(math.sqrt(num))
        for i in range(2, chk + 1):
            if (num % i) == 0:
                break
        else:
            ret = num
    return (ret)

def rgtCircular(num):
    snum = str(num)
    return (int(snum[-1] + snum[0:len(snum) - 1]))


lower = 1
upper = 1000000
prime = []

for num in range(lower, upper + 1):
    if chkPrime(num) > 0 and num not in prime:
        # Taking special care for 11
        if num == 11:
            prime.append(num)
        else:
            cprime = [num]
            cnum = num
            for i in range(len(str(num)) - 1):
                cnum = rgtCircular(cnum)
                if chkPrime(cnum) > 0:
                    cprime.append(cnum)
            if len(cprime) == len(str(num)):
                prime += cprime

prime.sort()
print(len(prime))
