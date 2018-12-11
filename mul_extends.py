class A1():
    def __init__(self):
        print ('A1')
class B1(A1):
    def __init__(self):
        A1.__init__(self)
        print ('B1')
class C1(B1, A1):
    def __init__(self):
        A1.__init__(self)
        B1.__init__(self)
        print ('C1')


class A2(object):
    def __init__(self):
        print ('A2')
        
class B2(A2):
    def __init__(self):
        print ('enter B2')
        super(B2, self).__init__()
        print ('leave B2')
class C2(A2):
    def __init__(self):
         print ('enter C2')
         super(C2, self).__init__()
         print ('leave C2')      
class D2(B2,C2):
    #def __init__(self):
     #   super(D2, self).__init__()
     #   print ('D2')
       pass


D2()

    

