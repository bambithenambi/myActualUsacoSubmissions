line1=list(map(int,input().split()))

numOfCows=line1[0]
numOfMoves=line1[-1]

moves=list()

for i in range(numOfMoves):
    moves.append(list(map(int,input().split())))

initialpos = list(range(1, numOfCows+1))
finalpos=list(range(1, numOfCows+1))

master = {pos_list: [pos_list] for pos_list in range(1, numOfCows+1)}

while True:
    for move in moves:
        temp=finalpos[move[1]-1]
        finalpos[move[1]-1]=finalpos[move[0]-1]
        finalpos[move[0]-1]=temp
        master[finalpos[move[0]-1]].append(move[0])
        master[finalpos[move[1]-1]].append(move[1])
    if finalpos==initialpos:
        break

for cow in master:
    print(len(set(master[cow])))
