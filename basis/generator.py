'''
def gen():
    value=0
    while True:
        receive=yield value#返回value 并且将接收的值赋值给receive
        if receive=='exit':
            break
        value='get: %s' % receive


g=gen()
#print(g.send(Nonex))#注意：在启动生成器函数时只能send(None),如果试图输入其它的值都会得到错误提示信息。
print(g.send(None))#通过g.send(None)或者next(g)可以启动生成器函数
print(g.send('aaa'))
print(g.send(3))
print(g.send('exit'))
'''
'''
out:
0
get: aaa
get: 3
Traceback (most recent call last):
  File "C:/Users/chauncey/Desktop/generator.py", line 16, in <module>
    print(g.send('exit'))
StopIteration
'''
        

def gen():
    while True:
        try:
            yield 'normal value'
            yield 'normal value 2'
            print('here')
        except ValueError:
            print('we get ValueError here')
        except TypeError:
            break

g=gen()
print(next(g))
print(g.throw(ValueError))
print(next(g))
print(g.throw(TypeError))

'''
out:
normal value
we get ValueError here
normal value
normal value 2
Traceback (most recent call last):
  File "C:/Users/chauncey/Desktop/generator.py", line 34, in <module>
    print(g.throw(TypeError))
StopIteration
'''
