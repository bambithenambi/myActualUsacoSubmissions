line1=list(map(int,input().split()))

N=line1[0]
Q=line1[-1]

sequence=[*input()]

ranges=list()
for i in range(Q):
    ranges.append(list(map(int,input().split())))

for range in ranges:
    r1=dict()
    r2=dict()
    if range[0]==1 and range[1]==N:
        print(0)
    elif range[0]==1:
        for segment in sequence[range[1]:]:
            r1[segment] = r1.get(segment, 0) + 1
        print(len(r1))

    elif range[1]==N:
        for segment in sequence[:range[0]-1]:
            r1[segment] = r1.get(segment, 0) + 1
        print(len(r1))

    else:
        for segment in sequence[:range[0]-1]:
            r1[segment] = r1.get(segment, 0) + 1
        for segment in sequence[range[1]:]:
            r2[segment] = r2.get(segment, 0) + 1
        print(len(r1)+len(r2))
        
