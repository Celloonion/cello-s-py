# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:37:28 2020
eval()函数的官网解释：
https://docs.python.org/3/library/functions.html?highlight=eval#eval

"""
print(eval("3.14"))
print(eval("3+14"))
print(eval("print(1+1)"),'程序结束')

'''输出窗口:
3.14
17
2
None 程序结束
'''