import uuid
import redis
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
    return result
def save_redis(result):
    r=redis.Redis(host='192.168.174.128',port=7000,db=0)
    for uuid_code in result:
        r.lpush('uuid_code1',uuid_code)
if __name__=='__main__':
    result=create_code(200,21)
    save_redis(result)
