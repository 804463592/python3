import time as t

class Mytimer():
    def __init__(self):
        self.unit=['年','月','日','小时','分钟','秒']
        self.prompt="还未开始运行"
        self.lasted=[]
        self.begin=0
        self.end=0
    
    def __str__(self):
        return self.prompt  #作为字符串时自动调用

    __repr__=__str__  #__repr__作为表达式
    def __add__(self,other):
        prompt="总共运行了"
        result=[]
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
               prompt+=str(result[index])+self.unit[index]
        return prompt

    
    #开始⏲计时
    def start(self):
        self.begin=t.localtime()
        self.prompt="提示:请先调用stop()停止计时"
        print('计时开始...')


    #停止计时
    def stop(self):
        if not self.begin:
            print("请先调用start()进行进行计时")

        else:
            self.end=t.localtime()
            #self._calc(self)#这样就两个self参数了,错误
            #_calc(self)#错误
            self._calc()
            print('计时结束!')


    def _calc(self):
        self.lasted=[]
        self.prompt='总共运行了'
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
               self.prompt+=str(self.lasted[index])+self.unit[index]
        print(self.prompt)
        #为下一轮计时初始化变量
        self.begin=0
        self.end=0
