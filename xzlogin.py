#coding:utf-8
import urllib
import urllib2
import cookielib
import re
import time
import os
import uuid


#获取一个保存cookie的对象
cj = cookielib.LWPCookieJar()
#将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
cookie_support = urllib2.HTTPCookieProcessor(cj)
#创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
#将包含了cookie、http处理器、http的handler的资源和urllib2对象板顶在一起
urllib2.install_opener(opener)

def login(username,password):
	postdata=urllib.urlencode({
	"UserName":username,
    "Password":password,
    "UserType":"stu",
    "btn":"登陆"		
	})

	headers={
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip,deflate",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"73",
    "Content-Type":"application/x-www-form-urlencoded",
    "Host":"202.115.71.131",
    "Origin":"http://202.115.71.131",
    "Referer":"http://202.115.71.131/course/page/widered/index.jsp?c_id=196&c_name=3C0CD8506934059CA20281C5737DA286&c_count=753FA6786E4A2BFF&c_domain=289F67C16B2D311A&c_template=B7564C0FD61B679B",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
	}

	url="http://202.115.71.131/course/servlet/UserLoginDataAction"

	req=urllib2.Request(url,data=postdata)

	for n in headers:
		req.add_header(n,headers[n])
	html=urllib2.urlopen(req).read()
	print html
	return html
#======================================================

def watchvideo(resourceID):
	postdata=urllib.urlencode({
	"resource_id":resourceID
	})

	headers={
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip,deflate,sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Host":"202.115.71.131",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
	}

	url="http://202.115.71.131/course/websys/videoview.jsp?resource_id="+resourceID

	req=urllib2.Request(url,data=postdata)

	for n in headers:
		req.add_header(n,headers[n])
	html=urllib2.urlopen(req).read()
	return html
	#print html
#=====================================================

def addTime(resourceID):
	now=int(1000*time.time())
	stringnow=str(now)
	postdata=urllib.urlencode({
	"resource_id":resourceID,
    "SetType":"ADD",
    "ranstring":"",
    "sid":"",
    "tt":""
	})

	headers={
	"Accept":"*/*",
    "Accept-Encoding":"gzip,deflate,sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Connection":"keep-alive",
    "Host":"202.115.71.131",
    "Referer":"http://202.115.71.131/course/websys/videoview.jsp?resource_id="+resourceID,
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
	}

	url="http://202.115.71.131/course/servlet/UserStudyRecordAction?resource_id="+resourceID+"&SetType=ADD&ranstring=&sid=&tt="+stringnow

	req=urllib2.Request(url,data=postdata)

	for n in headers:
		req.add_header(n,headers[n])
	html=urllib2.urlopen(req).read()
	output = re.findall("(?<=e>)\S+(?=</)",html)
	return output[1].decode('gbk')

#=========================================================

def updateTime(resourceID,sid,ranstring):
	now=int(1000*time.time())
	stringnow=str(now)
	postdata=urllib.urlencode({
	"resource_id":resourceID,
    "SetType":"UPDATE",
    "ranstring":"jywj",
    "sid":sid,
    "tt":stringnow
	})

	headers={
	"Accept":"*/*",
    "Accept-Encoding":"gzip,deflate,sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Connection":"keep-alive",
    "Host":"202.115.71.131",
    "Referer":"http://202.115.71.131/course/websys/videoview.jsp?resource_id="+resourceID,
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
	}

	url="http://202.115.71.131/course/servlet/UserStudyRecordAction?resource_id="+resourceID+"&SetType=UPDATE&ranstring="+ranstring+"&sid="+sid+"&tt="+stringnow

	req=urllib2.Request(url,data=postdata)

	for n in headers:
		req.add_header(n,headers[n])
	html=urllib2.urlopen(req).read()
	output = re.findall("(?<=e>)\S+(?=</)",html)
	print output[1].decode('gbk')

#===========================================================
def getRandomPic(resourceID):

	headers={
	"Accept":"image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip,deflate,sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Connection":"keep-alive",
    "Host":"202.115.71.131",
    "Referer":"http://202.115.71.131/course/websys/videoview.jsp?resource_id="+resourceID,
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
	}

	url="http://202.115.71.131/course/servlet/GetRandomNumberToJPEG"

	req=urllib2.Request(url)

	for n in headers:
		req.add_header(n,headers[n])
	html=urllib2.urlopen(req).read()

	return html

#=========================================================保存文件操作
def get_file_extension(filename):
	return os.path.splitext(filename)[1]

def save_file(path,filename,data):
	if data ==None:
		return
	if (not os.path.exists(path)):
		print "path does not exists!"
		return
	file=open(path+filename,"wb")
	file.write(data)
	file.flush()
	file.close()

#==========================================================

resourceid="CE3E966A68970356"
savepath="/Users/Landon_pro/xzfile/"

firstnow=time.time()
now=int(1000*firstnow)
stringnow=str(now)
#-----------第一次跑这一段程序----------------------
username=raw_input("please input your username: ")
password=raw_input("please input your password: ")

login(username,password)
watchvideo(resourceid)
sid=addTime(resourceid)
pic=getRandomPic(resourceid)
save_file(savepath,"islogin"+stringnow+".png",pic)

print "请速到/Users/Landon_pro/xzfile/目录下查看验证码"

randstr=raw_input("please input the answer:")

updateTime(resourceid,sid,randstr)
print "-------------------------------------------"

#--------第二次跑这段程序--------------------------
while(1):
	if (time.time()-firstnow)>360:
		if (time.time()-firstnow)>3000:
			break
		else:
			updateTime(resourceid,sid,randstr)
			firstnow=time.time()
			print str(firstnow)
			print "========================="







