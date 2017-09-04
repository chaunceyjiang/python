from socket import *
import time
HOST=''
PORT=3306
Tcp_Sock=socket(AF_INET,SOCK_STREAM)
BUFFSIZE=4096

DATA = {}

def handle_put(key,value):
    DATA[key]=value
    return 'True | KEY [{0}] SET to [{1}]'.format(key,value)
def handle_get(key):
    if key in DATA:
        return 'True | [{0}]'.format(DATA[key])
    else:
        return 'Flase | key [{0}] not exists.'.format(key)
def handle_getlist(key):
    handle_get(key)
def handle_putlist(key,value):
    DATA[key]=value
    return 'True | KEY [{0}] SET to [{1}]'.format(key, value)
def handle_increment(key):
    if key in DATA:
        if isinstance(DATA[key],int):
            DATA[key]+=1
            return 'True | KEY [{0}] value increment 1'.format(key)
        else:
            return 'Flase | KEY [{0}] contains non-int value'.format(key)
    else:
        return 'Flase | KEY [{}] not exists'.format(key)
def handle_append(key,value):
    if key in DATA:
        if isinstance(DATA[key],list):
            DATA[key].append(value)
            return 'True | Key [{0}] had value [{1}] appended'.format(key, value)
        else:
            return 'Flase | Key [{0}] contains non-list value '.format(key)
    else:
        return  'Flase | key [{0}] not exists. '.format(key)
def handle_delete(key):
    if key in DATA:
        del(DATA[key])
        return 'True | DELETE Key [{0}]'.format(key)
    else:
        return 'Flase | Key [{0}] not exists'.format(key)
def parser_message(message):
    command=message.split(';')[0]
    key = message.split(';')[1]
    value=''
    value_type=message.split(';')[-1]
    if value_type.upper()=='LIST':
        value=message.split(';')[2].split(',')
        return command.upper(),key,value
    if value_type.upper() == 'INT':
        value = int(message.split(';')[2])
        return command.upper(), key, value
    if value_type.upper() == 'STRING':
        value = str(message.split(';')[2])
        return command.upper(), key, value
    return command.upper(),key,''
COMMAND_HANDLERS = {
    'PUT': handle_put,
    'GET': handle_get,
    'GETLIST': handle_getlist,
    'PUTLIST': handle_putlist,
    'INCREMENT': handle_increment,
    'APPEND': handle_append,
    'DELETE': handle_delete,
    }
def judge(recv):
    command,key,value=recv
    resopnse=''
    if command in ('GET','DELETE','INCREMENT','GETLIST'):
        resopnse=COMMAND_HANDLERS[command](key)
    elif command in ('PUT','PUTLIST','APPEND'):
        resopnse=COMMAND_HANDLERS[command](key,value)
    else:
        resopnse='Flase | Unknown command type [{}]'.format(command)
    return resopnse

if __name__=='__main__':
    Tcp_Sock.bind((HOST,PORT))
    Tcp_Sock.listen(1)
    while True:
        connection,addr=Tcp_Sock.accept()
        print('New connection from {0}'.format(addr))
        while True:
            try:
                data=connection.recv(BUFFSIZE).decode()
                if data == 'exit':
                    break
                response=judge(parser_message(data))
                connection.send(response.encode())
            except ConnectionResetError:
                break
            except IndexError:
                connection.send('Flase | Unknown command type [{}]'.format(data).encode())
        connection.close()