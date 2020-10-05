# -*- coding: utf-8 -*-
"""
本程序的知识点：
1.字符串,字符的下标（正反）和切片（左闭右开）
2.input(),eval()
3.print(),format()
4.list[],in
5.条件循环if-elif-else
6.变量类型，整数、浮点数......
"""

s = input("请输入带有符号的温度值")
try:
    n = eval(s[:-1])
except NameError:
    print("输入格式错误")
if s[-1] in ['C','c']:
    nF = n*1.8-32
    nK = n+273
    print("转换后的温度是{:.2f}F,{:d}K".format(nF,nK))
elif s[-1] in ['F','f']:
    nC = n/1.8+32
    nK = nC+273
    print("转换后的温度是{:.2f}C,{:d}K".format(nC,nK))
