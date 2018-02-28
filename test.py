#!/usr/bin/python
#-*- coding: UTF-8 -*-

print ("hello python!\n");
"""
input("按下 enter 键，继续打印.....")

if True:
	print("True");	
else:
	print("False");
print("fdakfa");

x = 1
y = 2
#换行打印
print(x)
print(y)
#不换行打印
print(x, end=" ")
print(y, end=" ")
"""
#import 与 from...import
'''
import sys
print("============python import mode==================")
print("命令行参数为：")
for i in sys.argv:
	print(i)
	
print('\n python 路径为', sys.path)
'''
'''
from sys import argv, path
print('==============导入特定的成员==================')
print('path:', path)

'''

######基本数据类型#######
counter = 100
miles = 100.0
name = "runoob"

print(counter)
print(miles)
print(name)


###多个变量赋值
a = b = c = 1
d, e, f = 1, 2.0, "fahfo"

print(a,b,c)

print(d,e,f)



