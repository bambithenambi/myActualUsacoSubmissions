import random
s=""
for i in range(10):
    s+=str(random.randint(0, 1))
ones=s.split('0')
zeroes=s.split('1')
print(s)
trial=map(len,ones)
trial2=map(len,zeroes)
print("ONES: ", ones)
print("one count", list(trial))
print("ZEROES: ", zeroes)
print("zero count", list(trial2))
print(len(list(filter(None, ones))))
