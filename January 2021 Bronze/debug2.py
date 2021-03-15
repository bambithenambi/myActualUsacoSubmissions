N=2
e=0
totalcases=0
printcases=0
while N<10:
    for e in range(N):
        start=printcases
        o = N-e
        count=0
        save=list()
        #save.append(N)
        save.append(e)
        save.append(o)
        if o==e:
            print(N)
            printcases+=1

        elif (o+1)==(e):
            print(N+1)
            printcases+=1


        elif e<o:
            o = o-e
            count+=2*e
            e=0
            if o%3==0:
                steps=(o/3)*2
                count+=steps
                o=0
                print(int(count))
                printcases+=1

            elif o%3==2:
                steps=((o-2)/3)*2+1
                count+=steps
                o=0
                print(int(count))
                printcases+=1

            elif o%3==1:
                steps=((o-1)/3)*2-1
                count+=steps
                o=0
                print(int(count))
                printcases+=1

        elif o>e:
            e = e-o-1
            count+=(2*o+1)
            o=0
            print(int(count))
            printcases+=1
        if start==printcases:
            print(save)
        totalcases+=1

    N+=1
print("totalcases:", totalcases)
print("printcases:", printcases)
