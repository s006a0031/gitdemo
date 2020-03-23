#Script Name         : 7-2.py
#Author              : Wanghaoyu
#Created             : 21th May 2019
#Last Modified       :
#Version             : 1.0
#Modifications       :

#Description         : 
import numpy as np
n=int(input())
for i in range(n):
    m=map(int,input().split())
    m0=list(m)
    
a=map(int,input().split())
a=list(a)
b=map(int,input().split())


x1=list(b)
y1=np.array(b)
c=[]
d=[]
for i in range(0,n,3):
   c.append(m0[i])
   c.append(m0[i+1])
   c.append(m0[i+2])
   x2=list(c)
   y2=np.array(x2)

   array1=np.tile(x1,(n,1))
   array2=np.tile(x2,(n,1))
   array3=array1-array2
   
   result=array3.sum
   result0=result**(1/2)
   d.append(result0)
e=min(d)
for i in range(len(d)):
    if d[i] == e:
        print(a[i])
    else:
        i+=1
for i in range(len(d)):
    if d[i] == e:
        print(a[i])
    else:
        i+=1