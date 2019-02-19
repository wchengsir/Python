#!/usr/bin/python
# -*- coding: UTF-8 -*-

s = 'abcdef'

print s[1:5]

str = 'Hello World!'
 
print str           # 输出完整字符串
print str[0]        # 输出字符串中的第一个字符
print str[2:5]      # 输出字符串中第三个至第五个之间的字符串
print str[2:]       # 输出从第三个字符开始的字符串
print str * 2       # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

letters = ['c', 'h', 'e', 'c', 'k', 'i', 'o']

print letters[1:4:2] # 列表截取可以接收第三个参数，参数作用是截取的步长.
# 在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串
