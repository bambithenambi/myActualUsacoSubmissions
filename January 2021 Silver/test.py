

N=8
Q=2

sequence=[*"ABBAABCB"]

ranges=[[3,6],[1,4]]
for range in ranges:
    r1=dict()
    r2=dict()
    if range[0]==1 and range[1]==N:
        print(0)
    elif range[0]==1:
        for segment in sequence[range[1]:]:
            r1[segment] = r1.get(segment, 0) + 1
        print(len(r1))
        print(r1)
    elif range[1]==N:
        for segment in sequence[:range[0]-1]:
            r1[segment] = r1.get(segment, 0) + 1
        print(len(r1))
        print(r1)
    else:
        for segment in sequence[:range[0]-1]:
            r1[segment] = r1.get(segment, 0) + 1
        for segment in sequence[range[1]:]:
            r2[segment] = r2.get(segment, 0) + 1
        print(len(r1)+len(r2))
        print(r1)
        print(r2)
