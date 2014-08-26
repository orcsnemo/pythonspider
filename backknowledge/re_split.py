import re

mystr='one1two2three3four4'

p=re.compile(r'\d+')

print "split:" , p.split(mystr)
print "findall:" , p.findall(mystr)
