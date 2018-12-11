try:
     f=open('nihao.txt','r+')
     for each_line in f:
         print(each_line)
     
     f.seek(1,0)
     f.write("wwwwww")

     

except OSError as reason:
       print("出错了"+str(reason))

f.close()
