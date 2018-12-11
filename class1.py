class Turtle:
    color='green'
    weight=48

    def climb():
        print("爬噢")

    def run(self):
        print("抢到就跑")


class Mylist(list):#继承list
    pass

class A:
    def fun(self):
        print("我是谁")
class Ball:
    __color='red'#虽然是私有变量,但是在类外可以用dd._Ball__color访问该变量
    def __init__(self,name):
        self.__name=name
    def kick(self):
        print("我叫%s,该死的,谁踢我..."%self.__name)
    def see(self):
        print("我是%s,颜色是%s"%(self.__name,self.__color))
