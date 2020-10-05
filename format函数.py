# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:52:54 2020
@author: Celloonion
更详细请戳官网：https://pyformat.info/
阿谋的笔记：https://www.cnblogs.com/amou/p/9222512.html
format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
"""
print("{}x{}x{}".format(1,2,3)) #输出1x2x3
print("{0}x{0}x{2}".format(1,2,3)) #输出1x1x3,这里的2表示在tup:format()中下标为2的元素

print("{2:-^+#30x}".format(1,2,252)) #输出------------+0xfc-------------
#右对齐> 左对齐< 居中^ +是带正负号 #是显示进制类型 30是设定的槽输出宽度 x是小写十六进制数字输出
print("{2:->30.2f}".format(1,2,252))#输出------------------------252.00
        
print("{:,.2f}".format(12345678)) #输出12,345,678.00
print("{:.2%}".format(0.25)) #输出25.00%
print("{:.2e}".format(12345678)) #输出1.23e+07 科学计算法
print("{:+,.2f}".format(12345678)) #输出+12,345,678.00

print("{:.4}".format("Python")) #输出Pyth 设定字符串最大输出长度
print("{:.4}".format("Py")) #输出Py

'''参数传入'''
s1 = 'world'
s2 = 'python'
print('hello, {obj} ,i am {name}'.format(obj = s1,name = s2))
# 输出结果：hello, world ,i am python

'''datetime.now的四个参数Y,m,d,X'''
from datetime import datetime
now=datetime.now()
print('{:%Y-%m-%d %X}'.format(now))
# 输出结果：2020-10-05 15:24:26

'''{}的转义'''
print('{{hello}} {{{0}}}'.format('world')) #输出结果：{hello} {world}

