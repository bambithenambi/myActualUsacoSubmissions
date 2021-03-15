imp=input().split()
N=int(imp[0])
K=int(imp[1])


years=list()
for i in range(N):
    years.append(int(input()))
years.sort(reverse=True)

maxyear=years[0]
startbucket=maxyear-(maxyear%12)+12

buckets=""
ones=0
jumphomecorrection=0

while startbucket>12:
    if any(year > startbucket-12 and year < startbucket for year in years):
        buckets+="1"
        ones+=1
    else:
        buckets+="0"
    startbucket-=12

if any(year > 0 and year < 12 for year in years):
    buckets+="1"
    ones+=1
    jumphomecorrection=1
else:
    buckets+="0"

"""
print(buckets)
"""
chunks=len(list(filter(None, buckets.split('0'))))+jumphomecorrection
zeroes=list(map(len,buckets.split('1')))
"""
print("Chunks: ",chunks)
print("ZEROES: ",zeroes)
print("Ones: ",ones)
print("K: ", K)
"""
if chunks<=K:
    print(ones*12)
else:
    overshoot=chunks-K
    ones+=sum(zeroes[0:overshoot])
    print(ones*12)
