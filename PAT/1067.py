PASSWD,N=input().split(' ')
t=0
while True:
    passwd=input()
    if passwd == '#':break
    t += 1
    if passwd==PASSWD:
        print('Welcome in')
        break
    else:
        print('Wrong password:',passwd)
        if t == int(N):
            print('Account locked')
            break
