import string,urllib2

def baidu_tieba(url,begin_page,end_page):
	for i in range(begin_page,end_page):
		sName=string.zfill(i,5)+'.html'
		print 'Downloading No.'+str(i)+'page,save as '+sName+'...'
		f=open(sName,'w+')
		m=urllib2.urlopen(url+str(i)).read()
		f.write(m)
		f.close()

bdurl=str(raw_input(u'Input url\n'))
begin_page=int(raw_input(u'Input begin page:\n'))
end_page=int(raw_input(u'Input end page:\n'))

baidu_tieba(bdurl,begin_page,end_page)
