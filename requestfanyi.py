#coding=utf-8
from urllib import  request
from urllib import parse
import json
import hashlib
import random

def curlmd5(src):
    m = hashlib.md5()
    m.update(src.encode('UTF-8'))
    return m.hexdigest()

if __name__=='__main__':
	Request_url='http://openapi.youdao.com/api'
	#创建from_data 格式
	From_data={}
	From_data['q']='jack'
	From_data['from']='auto'
	From_data['to']='auto'
	From_data['appKey']='4818badcf7f9cec1'
	From_data['salt']=random.randint(1, 65536)
	From_data['salt2']=str(From_data['salt'])
	From_data['sign']=curlmd5(From_data['appKey'] + From_data['q'] + From_data['salt2']+ 'X5kCwfGbmpi2KyKTZC8kjgkZgofZqdsN')
	print(From_data['sign'])
	#使用 urlencode转换格式
	data=parse.urlencode(From_data).encode('utf-8')
	responese=request.urlopen(Request_url,data)
	html=responese.read().decode('utf-8')
	# print(html)
	translate_results=json.loads(html)
	translate_results = translate_results['web'][0]['value']
	print(translate_results)