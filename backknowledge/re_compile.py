# -*- coding:utf-8 -*-
import re
a=re.compile(r"""\d+
		\.
		\d*""",re.X)
b=re.compile(r"\d+\.\d*")

match11=a.match('3.1415')
match12=a.match('33')
match21=b.match('3.1415')
match22=b.match('33')

if match11:
	print match11.group()
else:
	print u'match11不是小数'
	

if match12:
	print match12.group()
else:
	print u'match12不是小数'


if match21:
	print match21.group()
else:
	print u'match21不是小数'


if match22:
	print match22.group()
else:
	print u'match22不是小数'
