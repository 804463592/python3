seq = ('Google', 'Runoob', 'Taobao')
 
dic1 = dict.fromkeys(seq)
print("新字典为 : %s"%  str(dic1))

dic2 = dict.fromkeys(seq, 10)
print("新字典为 : %s" %  str(dic2))

dic3 ={}.fromkeys(seq, '10')
print("新字典为 : %s" %  str(dic3))
