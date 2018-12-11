#斐波那契,方法1:
def libs():
    a=0
    b=1
    while True:
        a,b=b,a+b
        yield a
        
for each in libs():
    if each<10:
        print(each)

     
        


  
