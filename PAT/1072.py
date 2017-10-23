N,M=input().split(' ')
S1=set(input().split(' '))
result=[]
total=0
for i in range(int(N)):
    L=input().split(' ')
    l=[];l.append(L[0])
    for i in L[2:]:
        if i in S1:
            l.append(i)
            total+=1
    if len(l)!=1:
        result.append(l)
for i in result:
    print("%s:"%(i[0]),end='')
    for j in i[1:]:
        print(" %s"%(j),end='')
    print()
print(len(result),total)