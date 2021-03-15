import math
N=int(input())
cows=list(sorted(map(int,input().split())))
stalls=list(sorted(map(int,input().split())))

count=0
product=1

for stall in stalls:
    mult=0
    for i in range(N):
        if cows[i]<=stall:
            mult+=1
    product=(mult-count)*product
    count+=1

print(product)
