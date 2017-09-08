def hi():
    return "hi yasoob!"
def doSomethingforeHi(func):
    print('I am doing some boring work before executing hi()')
    print(func())

doSomethingforeHi(hi)

def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print('I am doing some boring work after executing a_func()')

    return wrapTheFunction#返回一个内部定义的函数

@a_new_decorator
def a_function_requiring_decoration():
    print('I am the function which needs some decoration to remove my foul smell')

print('---------------')

#第一次调用
a_function_requiring_decoration()


print('---------------')


#第二次调用
#a_function_requiring_decoration=a_new_decorator(a_function_requiring_decoration)
#将a_function_requiring_decoration传参给a_new_decorator，同时将返回值赋值给a_function_requiring_decoration
#这样a_function_requiring_decoration其实是一个新的函数，这个新的函数是来源a_new_decorator的返回值
a_function_requiring_decoration()

#可以看出@符号是a_function_requiring_decoration=a_new_decorator(a_function_requiring_decoration) 这句话的简写




