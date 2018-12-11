try:
    file_name=input('请输入需要打开的文件名(加上后缀名):')
    f=open(file_name)
    print('文件内容是:')
    for each_line in f:
        print(each_line)
except OSError as reason:
    print('出错了'+str(reason))
else:
    print("一切正常")
    
#print(f.read(-1))
