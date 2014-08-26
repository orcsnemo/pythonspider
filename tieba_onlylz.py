#-*- coding:utf-8 -*-

import string
import urllib2
import re

#----处理页面上的各种标签-----
class HTML_Tool:
	#用 非贪婪 匹配 \t \n 空格 超链接 图片
	BgnCharToNoneRex=re.compile("(\t|\n| |<a.*?>|<img.*?>)")

	#用 非贪婪 匹配 任意<> 标签
	EndCharToNoneRex=re.compile("(<.*?>)")
	
	#用 非贪婪 匹配任意<p> 标签
	BgnPartRex=re.compile("<p.*?>")
	CharToNewLineRex=re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
	CharToNextTabRex=re.compile("<td>")

	#将一些 html的符号实体转变为原始符号
	replaceTab=[("&lt;",">"),("&gt;",">"),("&amp;","&"),("&quot;","\""),("&nbsp;"," ")]

	def Replace_Char(self,x):
		x=self.BgnCharToNoneRex.sub("",x)
		x=self.BgnPartRex.sub("\n   ",x)
		x=self.CharToNewLineRex.sub("\n",x)
		x=self.CharToNextTabRex.sub("\t",x)
		x=self.EndCharToNoneRex.sub("",x)

		for t in self.replaceTab:
			x=x.replace(t[0],t[1])
		
		return x


#-----定义百度贴吧爬虫代码-----
class Baidu_Spider:
	#申明相关属性
	def __init__(self,url):
		self.myUrl=url+'?see_lz=1'
		self.datas=[]
		self.myTool=HTML_Tool()
		print u'已启动百度贴吧爬虫...'
	
	#初始化加载页面并将其转码
	def baidu_tieba(self):
		#读取页面原始信息并将其从gbk转码
		user_agent='MOzilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		headers={'User-Agent':user_agent}
		req=urllib2.Request(self.myUrl,headers=headers)
		myPage=urllib2.urlopen(req).read().decode('gbk')
		#计算lz发帖内容共多少页
		endPage=self.page_counter(myPage)
		title=self.find_title(myPage)
		print u'文章名字:'+title
		#获取最终数据
		self.save_data(self.myUrl,title,endPage)

	#计算页数
	def page_counter(self,myPage):
		#根据 "共<span clas="red"></span>页" 来获取页数
		myMatch=re.search(r'class="red">(\d+?)</span>',myPage,re.S)
		if myMatch:
			endPage = int(myMatch.group(1))
			print u'爬虫报告：共找到lz:%d页内容'%endPage
		else:
			endPage=0
			print u'爬虫报告：无法计算lz发布帖子页数！'
		return endPage

	#寻找帖子标题
	def find_title(self,myPage):
		#匹配 <h1 class="core_title_txt" title="">xxxxxxxxxx</h1> 标题
		myMatch=re.search(r'<h1.*?>(.*?)</h1>',myPage,re.S)
		title=u'无标题'
		if myMatch:
			title=myMatch.group(1)
		else:
			print u'爬虫报告:无法加载文章标题！'
		#文件名不能包含以下字符:\/:*?"<>|
		tmpstr={'\\','/',':','*','?','"','<','>','|'};
		for t in tmpstr:
			title=title.replace(t,'');
		return title

	#存贮帖子内容
	def save_data(self,url,title,endPage):
		#加载页面数据到数组中
		self.get_data(url,endPage)
		#打开本地文件
		f=open(title+'.txt','w+')
		f.writelines(self.datas)
		f.close()
		print u'爬虫报告:文件已下载到本地成txt文件'
		print u'请按任意key退出...'
		raw_input();

	#获取页面源码并存储到数组中
	def get_data(self,url,endPage):
		url=url+'&pn='
		for i in range(1,endPage+1):
			print u'爬虫报告:爬虫%d号正在加载...'%i
			myPage=urllib2.urlopen(url+str(i)).read()
			self.deal_data(myPage.decode('gbk'))
	
	#将内容从页面代码中抠出来
	def deal_data(self,myPage):
		myItems=re.findall('id="post_content.*?>(.*?)</div>',myPage,re.S)
		for item in myItems:
			data = self.myTool.Replace_Char(item.replace("\n","").encode('utf-8'))
			self.datas.append(data+'\n')


#入口点

print u"""#--------------
#   程序：百度贴吧爬虫 
#   版本：0.5 
#   作者：why 
#   日期：2013-05-16 
#   语言：Python 2.7 
#   操作：输入网址后自动只看楼主并保存到本地文件 
#   功能：将楼主发布的内容打包txt存储到本地。 
#--------------------------------------- 
"""  

print u'请输入贴吧的地址最后的数字串：'  
bdurl = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))   

mySpider=Baidu_Spider(bdurl)
mySpider.baidu_tieba()
