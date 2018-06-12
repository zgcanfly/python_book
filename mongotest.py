import pymongo
import time
class Mongodbconn(object):
	def __init__(self):
		self.date = time.strftime("%F-%T", time.localtime())
		self.clients = pymongo.MongoClient('192.168.95.146',22117)
		self.dbname="test"
		self.db=self.clients[self.dbname]
		self.col1=self.db['detail']

	def Insertcol1(self):
		detail1 = {'时间': self.date, 'message': 'are you ok'}
		self.col1.insert_one(detail1)
		print(detail1,"已经存入")



mc=Mongodbconn()
result=mc.Insertcol1()