#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
int(x [,base])
class int(x, base=10)
x -- 字符串或数字。
base -- 进制数，默认十进制。
'''

print int() 	# 不传入参数时，得到结果0
print int(3)	# 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制
print int(3.6)  
print int('12',16)
print int('0xa',16)
print int('10',8)

'''
函数					描述
int(x [,base])			将x转换为一个整数
long(x [,base] )		将x转换为一个长整数
float(x)				将x转换到一个浮点数
complex(real [,imag])	创建一个复数
str(x)					将对象x转换为字符串
repr(x)					将对象x转换为表达式字符串
eval(str)				用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)				将序列s转换为一个元组
list(s)					将序列s转换为一个列表
set(s)					转换为可变集合
dict(d)					创建一个字典。d必须是一个序列 (key,value)元组。
frozenset(s)			转换为不可变集合
chr(x)					将一个整数转换为一个字符
unichr(x)				将一个整数转换为Unicode字符
ord(x)					将一个字符转换为它的整数值
hex(x)					将一个整数转换为一个十六进制字符串
oct(x)					将一个整数转换为一个八进制字符串
'''

