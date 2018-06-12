#coding=utf-8
import pymongo
import time
class Mongodbconn(object):
	def __init__(self):
		self.date = time.strftime("%F-%T", time.localtime())
		self.clients = pymongo.MongoClient(['localhost:21117','localhost:22117','localhost:23117'],replicaSet = 'rs1')

		self.dbname="test"
		self.db=self.clients[self.dbname]
		self.col1=self.db['detail']


	def Insertcol1(self):
		detail1 = {'date': self.date, 'message': 'are you ok'}
		try:
			self.col1.insert(detail1)
			print(detail1,"save done")
		except Exception as e:
			print(e)
			time.sleep(10)
			pass

	def Insertcol2(self):
		detail2 = {'date': self.date, 'message': 'i am ok'}
		try:
			self.col1.insert(detail2)
			print(detail2, "save done")
		except Exception as e:
			print(e)
			time.sleep(10)
			pass


mc=Mongodbconn()
for i in range(100):
	if i%2==0:
		mc.Insertcol1()
	else:
		mc.Insertcol2()
	time.sleep(10)