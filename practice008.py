# 一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如，6的因子为1、2、3，而6=1+2+3，因此6是完数。编程，找出1000之内的所有完数，并输出该完数及对应的因子

import time

l = [ ]
start =time.clock()
for n in range (1,10000000000000000000000000000000000000000000):
    for a in range (1,n):
        if n%a ==0:
            l.append(a)
    if sum(l)==n:
        print (l)
        print (n)
        end = time.clock()
        print('Running time: %s Seconds'%(end-start))
    l = []
