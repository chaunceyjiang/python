import uuid
import pymysql
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
def mysql_conn(host="192.168.174.131",Port=3307,user="root",passwd="123456",dbname="test"):
    db=pymysql.connect(host,user,passwd,dbname,port=Port)
    cursor=db.cursor()
    return db,cursor
def mysql_exec(db,cursor,result):
    for uuid_code in result:
        sql="insert into py_uuid_0002 values('"+uuid_code+"');"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        
if __name__=='__main__':
    result=create_code(201,21)
    db,cursor=mysql_conn()
    mysql_exec(db,cursor,result)
    db.close()
