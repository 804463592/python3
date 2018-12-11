def c2f(cel):
    fah=cel*1.8+32
    return fah

def f2c(fah):
    cel=(fah-32)/1.8
    return cel    

def test():
    print("测试,32摄氏度=%.2f华氏度"%c2f(32))
    print("测试,99华氏度=%.2f摄氏度"%f2c(99))

if __name__=="__main__":#作为主程序时才调用
    test()    
