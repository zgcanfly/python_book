#coding=utf-8

import  pymysql
import logging

class MySqLCommand(object):
    def __init__(self,host,port,user,password,db,table):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.table = table
    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,db=self.db,charset='utf8')

            self.cursor = self.conn.cursor()
        except:
            print('connect mysql error.')

    def queryMysql(self):
        sql = 'SELET * FROM ' + self.table
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchall()
            print(row)
        except:
            print(sql + 'excute failed')
    def insertMysql(self,id,name,sex):
        sql = "INSERT INTO " + self.table + "VALUES(" + id + "," + "" + name + ","+"" + sex + ")"
        try:
            self.cursor.execute(sql)
        except:
            print("insert failed")

    def updateMysqlSN(self,name,sex):
        sql = "UPDATE"+self.table + "SET sex="+sex+""+"WHERE name=" + name + ""
        print("update sn:"+sql)
        try
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
    def closeMysql(self):
        self.cursor.close()
        self.conn.close()
        