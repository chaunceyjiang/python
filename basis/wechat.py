import requests
import itchat
def get_response(msg):
    apiUrl='http://www.tuling123.com/openapi/api'
    data={
        'key':'71f28bf79c820df10d39b4074345ef8c',
        'info':msg,
        'userid':'wechat-1'
    }
    try:
        r=requests.post(apiUrl,data=data).json()
        return r.get('text')
    except:
        return
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    reply=get_response(msg['Text'])
    print(reply)
    msg.user.send(reply)
itchat.auto_login(hotReload=False)
itchat.run()