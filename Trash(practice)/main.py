import m1 # as m
m1.f1()
m1.f2()



from m1 import f1,f2
f1()
f2()

from m1 import *  #all function 
f1()
f2()

import m2 
m2.t1()
m2.t2()


from m2 import t1,t2
t1()
t2()

from m2 import *
t1()
t2()



import m1 , m2
m1t1()
m1t2()
m2f1()
m2f2()