#coding=utf-8
import pymongo
import time
class Mongodbconn(object):
	def __init__(self):
		self.date = time.strftime("%F-%T", time.localtime())
		self.clients = pymongo.MongoClient(['10.250.34.15:27017','10.250.34.16:27017','10.250.34.17:27017'],replicaSet = 'rs1')
		self.dbname="admin"
		# self.clients.dbname.authenticate("ttx", "ttx2011")
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

if __name__=='__main__':
	mc=Mongodbconn()
	for i in range(100):
		if i%2==0:
			mc.Insertcol1()
		else:
			mc.Insertcol2()
		time.sleep(10)