#!encoding: utf-8
import requests, time
from pymongo import MongoClient
from fake_useragent import UserAgent

client = MongoClient()
db = client.lagou
# t = time.strftime("%Y-%m-%d", time.localtime())
# # job = 'job' + t
my_set = db.job

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false&isSchoolJob=0'


def get_job_info(page):
	for i in range(page):
		s_key = {
			'first': 'true',
			'pn': i,
			'kd': '运维',
		}

		headers = {
			'Cookie': 'user_trace_token=20171226132136-48c34fb5-eb91-4358-8037-f9990c7fff54; _ga=GA1.2.1429461395.1514265697; LGUID=20171226132138-a5f8d079-e9fc-11e7-adbd-525400f775ce; JSESSIONID=ABAAABAAAGFABEF1A33844AED7777C2D1DB0BE4F9922D6A; _gid=GA1.2.1684904298.1515377272; LGSID=20180108100752-bb96b7b5-f418-11e7-803e-525400f775ce; PRE_UTM=; PRE_HOST=www.google.ae; PRE_SITE=https%3A%2F%2Fwww.google.ae%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1514265697,1515377273; index_location_city=%E4%B8%8A%E6%B5%B7; X_HTTP_TOKEN=7acb2682906dac8f90a05e06c39e20ed; ab_test_random_num=0; _putrc=ACA637CD10C5ABBE; login=true; unick=%E9%87%91%E7%A3%8A; _gat=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=70; gate_login_token=8d68362ce47031c4ce9f4f6eb85eaea43d6e0ce9c8238eb8; LGRID=20180108102208-b9f53ae5-f41a-11e7-8042-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515378129; TG-TRACK-CODE=index_search; SEARCH_ID=8832075aae2c433db15303754c976bb5',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
			'Referer': 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4?labelWords=&fromSearch=true&suginput='
		}

		# ua = UserAgent()
		# headers['User-Agent'] = ua.random

		response = requests.post(url, data=s_key, headers=headers)

		if response.status_code == 200:
			# my_set.insert(response.json()['content']['positionResult']['result'])
			# print(response.json())
			#
			# print(response.json()['content'])
			# print(response.json()['content']['positionResult'])
			print(response.json()['content']['positionResult']['result'])
		else:
			print("something wrong")

		print("正在爬取" + str(i + 1) + "页.")
		time.sleep(20)


if __name__ == "__main__":
	get_job_info(31)