# -*- coding:utf-8 -*-

import re

pattern = re.compile(r'world')

#注意，match只有在第一个位置匹配成功才有返回
#match = pattern.match('hello world!')
#上面这一句是不会有输出的，返回为none

#search采用从头到尾的方式扫描会有找到相应输出
match = pattern.search('hello world!')

if match:
	print match.group()

