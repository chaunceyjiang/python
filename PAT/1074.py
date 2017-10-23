Hex=list(map(int,list(input())))[::-1]
A=list(map(int,list(input())))[::-1]
B=list(map(int,list(input())))[::-1]
for l in range(len(Hex)-len(A)):A.append(0)
for l in range(len(Hex)-len(B)):B.append(0)
def adder(a,b,h,d):
    if h==0:h=10
    x=(a+b+d)//h
    y=(a+b+d)%h
    print(x,y)
    return x,y
t=0
result=[]
for i in range(len(Hex)):
    t,x=adder(A[i],B[i],Hex[i],t)
    result.append(x)
s=''.join(list(map(str,result[::-1]))).lstrip('0')
if len(s)==0:
    print(0)
else:
    print(s)