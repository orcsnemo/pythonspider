# -*- coding:utf-8 -*-
import re
p=re.compile(r'\d')
for m in p.finditer('one1two2three3four4'):
#注意：print m.group(),与print m.group()输出结果不一样，具体见如下:
	print m.group()


for m in p.finditer('one1two2three3four4'):
	print m.group(),
