# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:14:08 2020

@author: Administrator
"""
import time
scale = 63
print("执行开始".center(scale//2,'-'))
t = time.process_time()

for i in range(scale+1):
    a = '*'*i
    b = '.'*(scale - i)
    c = (i/scale)*100
    t -= time.process_time()
    time.sleep(0.05)
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,-t/100),end='')
print("\n"+"执行结束".center(scale//2,'-'))
