#*args and **kargs
from types import new_class

def f1(a=1,b=1,c=1) :
    return a+b+c

 #f ()

#f1(1)
#f1(a:1,b:2)
#f1(a:1,b:2,c:3)
#f(a=10,b=20,c=30)
r=f1(c=1,a=2,b=90)
print(r)