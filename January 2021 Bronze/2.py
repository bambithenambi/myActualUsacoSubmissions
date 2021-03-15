count=0
e=0

N=int(input())
ids=list(map(int,input().split()))

for id in ids:
    if id%2==0:
        e+=1

o = N-e
#print(N, e, o)

if o==e:
    print(N)
    quit()

elif (o+1)==(e):
    print(N+1)
    quit()

elif e<o:
    o = o-e
    count+=2*e
    e=0
    if o%3==0:
        steps=(o/3)*2
        count+=steps
        o=0
        print(int(count))
        quit()
    elif o%3==2:
        steps=((o-2)/3)*2+1
        count+=steps
        o=0
        print(int(count))
        quit()
    elif o%3==1:
        steps=((o-1)/3)*2-1
        count+=steps
        o=0
        print(int(count))
        quit()

elif o<e:
    e = e-o-1
    count+=(2*o+1)
    o=0
    print(int(count))
    quit()
