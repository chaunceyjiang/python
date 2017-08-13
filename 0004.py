from collections import defaultdict
with open(r'C:\Users\chauncey\Desktop\English.txt','rt') as f:
    D=defaultdict(int)
    for line in f:
	    x=line.split(' ')
	    while '' in x:x.remove('')
	    while '\n' in x:x.remove('\n')
	    for word in x:
	    	D[word.strip('".(),\n')]+=1
    for k in D:
	    print(k,D[k])
