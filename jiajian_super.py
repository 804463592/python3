

class New_int(int):
      def __add__(self,other):
          return  int.__sub__(other,self)#可以交换位置,结果相反
          #return  super(New_int,self).__sub__(other) 
      def __sub__(self,other):
          #return  super(New_int,self).__add__(other)
          #return  super().__add__(other)
          
          return  super(New_int,aa).__add__(other)#甚至可以强行绑定其他的子类对象
        
          #return  super(New_int).__add__(self,other)#错误,super不能只有一个参数
        
class A(New_int):
    pass

aa=A(10)
#New_int中的super中,哪怕是没有参数,即super(),也是绑定了self的,故后面的__add__,
#不用再绑定self
