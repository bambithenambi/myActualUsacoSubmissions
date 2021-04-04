
var=input().split()

n=int(var[0])
k=int(var[1])
l=int(var[2])
'''
n=6
k=5
l=2
raw = input("Enter a list: ").split()
data = list(map(int,raw))
data.sort()
print("Start:", data)
'''
raw = input().split()
data = list(map(int,raw))
data.sort()
copy = data.copy()
def hindex(citations, n):
    hindex = 0
    # Set the range for binary search
    low = 0
    high = n - 1
    while (low <= high):
        mid = (low + high) // 2
        # Check if current citations is
        # possible
        if (citations[mid] >= (mid + 1)):
            # Check to the right of mid
            low = mid + 1
            # Update h-index
            hindex = mid + 1
        else:
            # Since current value is not
            # possible, check to the left
            # of mid
            high = mid - 1
    return hindex

comp=0
if l>=n:
    for i in range(n):
        data[i]+=k
    current = hindex(list(reversed(data)), n)
else:
    for counter in range(k):
        for i in range(l):
            data[i]+=1
        data.sort()
    current = hindex(list(reversed(data)), n)
    if n-(current+1)>0:
        for i in range(n-(current+1)):
            comp+=(data[i]-copy[i])
        data[n-(current+1)]+=comp
        if hindex(data, n)>current:
            current=hindex(list(reversed(data)), n)
data.sort()
print(current)
