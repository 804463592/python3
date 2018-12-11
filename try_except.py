try:
    sum=1+'1'
    f=open('nihao11.txt')
    print(f.read())
except OSError as reason111:
    print("文件出错了\n错误的原因是:"+str(reason111))
except TypeError as reason:
    print("计算出错了\n错误的原因是:"+str(reason))

finally:
    f.close()
