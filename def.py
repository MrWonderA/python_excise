#!/usr/bin/python3

'''
total = 0; # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
	total = arg1 + arg2; # total在这里是局部变量.
	print("函数内是局部变量 : ", total)
	return total;

#调用sum函数
sum( 10, 20 );
print ("函数外是全局变量 : ", total)
'''

#这个是错的

'''
总结：
1、内部函数，不修改全局变量可以访问全局变量
2、内部函数，修改同名全局变量，则python会认为它是一个局部变量
3、在内部函数修改同名全局变量之前调用变量名称（如print sum），则引发Unbound-LocalError
'''
'''
a = 10
def test():
	a = a + 1
	print(a)
test()
'''