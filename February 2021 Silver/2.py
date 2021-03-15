imp=input().split()
#imp=input("enter ").split()
N=int(imp[0])
K=int(imp[1])


years=list()
for i in range(N):
    years.append(int(input()))
    #years.append(int(input("year ")))
years.sort(reverse=True)



buckets=dict()

for year in years:
    bucketid=year-(year%12)+12
    buckets[bucketid]=buckets.get(bucketid, 0)+1

distances=list()
keys = list(buckets.keys())
keys.append(0)
adjacent=0
for key1 in keys:
    try:
        key2=keys[keys.index(key1)+1]
        if key1-key2>12:
            distances.append(int((key1-key2)/12-1))
        else:
            if key2!=0:
                adjacent+=1
    except:
        break

ones=len(keys)-1
chunks=ones-adjacent

#print("ones: ", ones)
if chunks<=K:
    print(ones*12)
else:
    overshoot=chunks-K
    ones+=sum(distances[0:overshoot])
    print(ones*12)

"""
print("buckets: ", buckets)
print("keys: ", keys)
print("distances: ", distances)
print("adjacent: ", adjacent)

print("chunks: ", chunks)
"""
