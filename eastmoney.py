
#coding=utf-8
from multiprocessing import Pool
import getstart
import requests,re
import pymongo
import _thread
import time
from bs4 import BeautifulSoup
clients=pymongo.MongoClient('106.15.224.237')
db=clients['everydayfund']
col1=db['fund']
col2=db['detail']
url='http://fund.eastmoney.com/allfund.html'

def int_value(value):
	if "%" in value:
		newint = float(value.strip("%")) / 100
		return newint
	elif isinstance(value, float):
		print(value)
	else:
		print("数值错误")

def run_detail2(code,name,url):
	soup=getstart.geturl_utf8(url)
	tags=soup.find_all(class_='ui-font-middle ui-color-red ui-num')
	try:
		m1=tags[3].string
		y1=tags[4].string
		m3=tags[5].string
		y3=tags[6].string
		m6=tags[7].string
		rece=tags[8].string
		nm1=int_value(m1)
		nm3=int_value(m3)
		nm6=int_value(m6)
		ny1=int_value(y1)
		ny3=int_value(y3)
		nrece=int_value(rece)
		detail1={'代码':code,'名称':name,'近1月':int_value(m1),'近3月':int_value(m3),'近6月':int_value(m6),'近1年':int_value(y1),'近3年':int_value(y3),'成立来':int_value(rece)}
		# detail={'代码':code,'名称':name,'近1月':m1,'近3月':m3,'近6月':m6,'近1年':y1,'近3年':y3,'成立来':rece}
		# print(detail)
		print("detail1",detail1)
		col2.insert(detail1)
	except:
		run_detail1(code,name,url)

	


def run_detail1(code,name,url):
	soup=getstart.geturl_utf8(url)
	tags=soup.select('dd')
	try:
		m1=(tags[1].find_all('span')[1].string)
		y1=(tags[2].find_all('span')[1].string)
		m3=(tags[4].find_all('span')[1].string)
		y3=(tags[5].find_all('span')[1].string)
		m6=(tags[7].find_all('span')[1].string)
		rece=(tags[8].find_all('span')[1].string)
		nm1=int_value(m1)
		nm3=int_value(m3)
		nm6=int_value(m6)
		ny1=int_value(y1)
		ny3=int_value(y3)
		nrece=int_value(rece)
		# detail = {'代码': code, '名称': name, '近1月': m1, '近3月': m3, '近6月': m6, '近1年': y1, '近3年': y3, '成立来': rece}
		# print(detail, "\n")
		detail1={'代码': code, '名称': name, '近1月': nm1, '近3月': nm3, '近6月': nm6, '近1年': ny1, '近3年': ny3, '成立来': nrece}

		print(detail1)
		col2.insert(detail1)

	except:
		pass



if __name__=="__main__":
	# int_value(value='78%')
	soup=getstart.geturl_gbk(url)
	tags=soup.select('.num_right > li')

	for tag in tags:
		if tag.a is None:
			continue
		else:
			content=tag.a.text
			code=re.findall(r'\d+',content)[0]
			#print(code)
			name=content.split('）')[1]
			#print(name)
			url=tag.a['href']
			#print(content)
			fund={'code':code,'name':name,'url':url}
			print(fund)
			col1.insert(fund)
			# time.sleep(0.1)
			# print(fund,"\n")
			run_detail1(code, name, url)
