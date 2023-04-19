n=100
fact=1
num=[]
sum=0

for i in range(1,n+1):
    fact=fact*i
    num=map(int, str(fact))

for i in num:
    sum=sum+i
print(sum)