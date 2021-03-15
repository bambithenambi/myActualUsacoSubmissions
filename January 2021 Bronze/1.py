count=1
curIndex=-1

alphabet=list(input())
letters=list(input())


for letter in letters:
    if alphabet.index(letter)<=curIndex:
        count+=1
    curIndex=alphabet.index(letter)

print(count)
