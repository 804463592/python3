links={1:'nihao',2:'hello',3:'hi'}
for each in links.keys():
#for each in links: #效果一样   
    print(each,links[each])
    
string ="FishC"
it =iter(string)
while True:
    try:
        each=next(it)

    except StopIteration:
           break
    print(each)    

class Fibs:#实质上是一个迭代器类
    def __init__(self,n=60):
        self.a=0
        self.b=1
        self.n=n
    def __iter__(self):
        #self.a=0#如果不更新的话.for循环将不会从头开始迭代
        #self.b=1
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>=self.n:
            raise StopIteration
        return self.a
fibs1=Fibs()
it=iter(fibs1)
next(fibs1)
next(it)
next(it)
for each1 in fibs1:#并不是同一个对象使用同一个迭代器哈,虽然上面的next
    if each1<20:   #影响到了下面的for循环,但是是因为for循环调用iter时,
        print(each1)#返回的是self,且对self.a,self.b没有更新
    else:  
        break
    
#fibs2=Fibs()   
for each1 in fibs1:
        print(each1,"我是第二个for循环")
    
    
