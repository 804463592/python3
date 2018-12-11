class MyNumbers:
  def __init__(self,n):
      self.n=n
      self.a = 1
  def __iter__(self):
       #下面的两个next不影响for循环的输出,原因就在此,
    return self  #将self.a放在构造函数中,next则会影响for循环
 
  def __next__(self):
    x = self.a
    self.a += 1
    if self.a > self.n:
       raise StopIteration
    return x
myclass = MyNumbers(30)
myiter = iter(myclass)
next(myiter)
next(myiter)
for each in myclass:
    if each<8:
        print(each)
