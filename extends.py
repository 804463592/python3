class Parent:
      str1="read"
      def __init__(self,name='Parent_'):
          self.__a=name
          self.str1='not'
    
      def hello(self):
          print("正在调用父类的方法...",Parent.str1,self.str1)

      def say(self):
            print("我是Parent")


         
class Child():
      def __init__(self,name='Child',name2='Parent'):#会屏蔽掉基类的构造函数
        #  Parent.__init__(self,name2)#两种方法调用基类构造函数
          super().__init__(name2)
          self.__b=name
      def hello(self):
          print("正在调用子类的方法...",Parent.str1,self.str1,self._Parent__a,self.__b)
      def say(self):
            print("我是Child")


class Grandson():
      def say(self):
            print('我是Grandson')

            
#p=Parent('fishc')
#p.hello()

#print(Parent._Parent__str)#访问伪私有变量

#c=Child('fishc',"shark")
#Parent.__init__(c,"jiayu")#如果子类中不调用基类构造函数,也可以这样调用基类的构造函数
#c.hello()


class A(Child,Parent,Grandson):
      pass

a=A()
a.say()
      
