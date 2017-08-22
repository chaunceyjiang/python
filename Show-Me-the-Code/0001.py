import uuid
def create_code(num,length):
    result=[]
    while True:
        uid_4=uuid.uuid4()
        uid_1=uuid.uuid1()
        x=str(uid_1).replace('-','')
        y=str(uid_4).replace('-','')
        result.append((x+y)[:length])
        if len(result)==num:
            break
    for code in result:
        print(code)
if __name__=='__main__':
    create_code(200,21)
