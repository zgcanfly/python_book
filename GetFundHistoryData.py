# coding=utf-8
'''
createdate: 2018-01-09
author: yangzhiguang
QQ技术群:540085853
'''
from multiprocessing import Pool
import re
import pymongo
import time
from bs4 import BeautifulSoup
import requests, random

UA_LIST = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
           "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
          'Connection': 'keep-alive', 'User-Agent': random.choice(UA_LIST)}
clients = pymongo.MongoClient('106.15.224.237')
date = time.strftime("%F", time.localtime())
dbname = "fund" + date
db = clients[dbname]
col1 = db['fund']
col2 = db['detail']
url = 'http://fund.eastmoney.com/allfund.html'


def geturl_gbk(url):
	html = requests.get(url, headers=header).content.decode('gbk')
	soup = BeautifulSoup(html, 'lxml')
	print("soup----------------------------------:"+str(soup))
	return soup


def geturl_utf8(url):
	html = requests.get(url, headers=header).content.decode('utf-8')
	soup = BeautifulSoup(html, 'lxml')
	print("soup----------------------------------:"+str(soup))
	return soup


def int_value(value):
	if "%" in value:
		newint = float(value.strip("%")) / 100
		return newint
	elif isinstance(value, float):
		print(value)
	else:
		print("数值错误")


def run_detail2(code, name, url):
	soup = geturl_utf8(url)
	tags = soup.find_all(class_='ui-font-middle ui-color-red ui-num')
	try:
		m1 = tags[3].string
		y1 = tags[4].string
		m3 = tags[5].string
		y3 = tags[6].string
		m6 = tags[7].string
		rece = tags[8].string
		nm1 = int_value(m1)
		nm3 = int_value(m3)
		nm6 = int_value(m6)
		ny1 = int_value(y1)
		ny3 = int_value(y3)
		nrece = int_value(rece)
		detail1 = {'代码': code, '名称': name, '近1月': int_value(m1), '近3月': int_value(m3), '近6月': int_value(m6),
		           '近1年': int_value(y1), '近3年': int_value(y3), '成立来': int_value(rece)}
		print("detail1", detail1)
		# col2.insert(detail1)
	except:
		pass


def run_detail1(code, name, url):
	soup = geturl_utf8(url)
	tags = soup.select('dd')
	try:
		m1 = (tags[1].find_all('span')[1].string)
		y1 = (tags[2].find_all('span')[1].string)
		m3 = (tags[4].find_all('span')[1].string)
		y3 = (tags[5].find_all('span')[1].string)
		m6 = (tags[7].find_all('span')[1].string)
		rece = (tags[8].find_all('span')[1].string)
		nm1 = int_value(m1)
		nm3 = int_value(m3)
		nm6 = int_value(m6)
		ny1 = int_value(y1)
		ny3 = int_value(y3)
		nrece = int_value(rece)
		detail1 = {'代码': code, '名称': name, '近1月': nm1, '近3月': nm3, '近6月': nm6, '近1年': ny1, '近3年': ny3, '成立来': nrece}

		print(detail1)
		col2.insert(detail1)
	except:
		run_detail2(code, name, url)


if __name__ == "__main__":
	soup = geturl_gbk(url)
	tags = soup.select('.num_right > li')

	for tag in tags:
		if tag.a is None:
			continue
		else:
			print(tag)
	# 		content = tag.a.text
	# 		code = re.findall(r'\d+', content)[0]
	# 		name = content.split('）')[1]
	# 		url = tag.a['href']
	# 		fund = {'code': code, 'name': name, 'url': url}
	# 		print(fund)
	# 		col1.insert(fund)
			# run_detail1(code, name, url)
