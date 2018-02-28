#!/usr/bin/python3
#-*- coding: UTF-8

#isinstance 和 type 区别
'''
a,b,c,d = 3,2.1,False,4+3j
#print(type(a), type(b), type(c),type(d))

e = 111
isinstance(e,bool);

class A:
    pass

class B(A):
    pass
type(A()) == A        # returns True
	
isinstance(A(), A)    # returns True

isinstance(B(), A)    # returns True
type(B()) == A        # returns False
'''
#del
'''
var1 = 1
var2 = 10

print(var1,"\n",var2)

print("\n")

del var1
print(var1)
print(var2)
'''

#String 字符串
'''
str = 'Runoob'

print(str)
print(str[0:-1])	#输出第一个到 倒数第二个的所有字符
print(str[0])
print(str[2:5])
print(str[2:])		#输出从第三个开始的后的所有的字符
print(str * 2)		#输出字符串两次
print(str + "fajfwojngbi af")	#连接字符串
'''

#转义字符
"""
print('Ru\noob')

print(r'Ru\noob')
"""

#List
'''
list = ['abcd',	786, 3.21, 'runoob', 230.9]
tinylist = [123, 'runoob']

print(list, '\n',tinylist,'\n')
print(list[0])
print(list[-1])
print(list[1:3])		# 输出从第三个元素开始的所有元素
print(tinylist * 2)		# 输出两次列表
print(list + tinylist)	# 连接列表
'''

#Tuple 元组
'''
tuple = ('abcd', 786, 3.21, 'runoob', 230.9)
tinytuple = (123, 'runoob')

print(tuple, '\n',tinytuple,'\n')
print(tuple[0])
print(tuple[-1])
print(tuple[1:3])		# 输出从第三个元素开始的所有元素
print(tinytuple * 2)		# 输出两次元组
print(tuple + tinytuple)	# 连接元组
'''

#Set集合
'''
student = {'Tom', 'Jim', 'Mary', 'Jack', 'Rose'}

print(student)
if('Rose' in student) :
	print('Rose 在集合中')
else :
	print('Rose 不在集合中')
'''

#set 可以进行集合运算
'''
a = set('abcdefgh')
b = set('efgh')

print(a)
print(b)
print('a和b的差集:',a - b)	#a和b的差集
print('a和b的并集:',a | b)	#a和b的并集
print('a和b的交集:',a & b)	#a和b的交集
print('a和b不同时存在的元素:',a ^ b)	#a和b不同时存在的元素
'''

#Dictionary字典

dict = {}
dict['one'] = "1 - 菜鳥教程"
dict[2] = " 2 - 菜鳥工具"

tinydict = {'name' : 'runoob', 'code':1, 'site': 'www.runoob.com'}

print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())	#输出所有键
print(tinydict.values())	#输出所有值	











