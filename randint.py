import random as r
def ran(min,max,n):
    result=[]
    while(n):
            i=r.randint(min,max)
            if i not in result:
               result.append(i)
               n-=1

    result.sort()
    return result

