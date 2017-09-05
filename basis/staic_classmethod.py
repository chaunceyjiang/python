class A(object):
    bar=1
    def __init__(self):
        self.fo='C'
    def foo(self):
        print('foo')
    @staticmethod
    def static_foo():
        print('static_foo')
        print(A.bar)
    @classmethod
    def class_foo(xx):
        print('class_foo')
        print(xx.bar)
        xx.static_foo()
        xx().foo()
    @property
    def size(self):
        return self.fo
    @size.setter
    def size(self,s):
        self.fo=s
        print('yes')
if __name__=='__main__':
    a=A()
    a.static_foo()
    print('----static---')
    a.class_foo()
    print('----class----')
    print(a.size)
    a.size='D'
    print(a.size)
