# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 15:23:54 2017

@author: feng_
"""
import pymysql
import tushare as ts
import pymysql
import datetime
import warnings

# con = pymysql.connect(host='192.168.1.74',port=3306,user='root',passwd='password')
# cursor = con.cursor()
con = pymysql.connect(host='192.168.1.74',port=3306,user='root',passwd='password',db='chinesestock')
cursor = con.cursor()
def createdatabase():
    try:
        sql = "create database if not exists `chinesestock` DEFAULT CHARSET utf8 COLLATE utf8_general_ci;"
        cursor.execute(sql)
        con.commit()
    except:
        con.rollback()
    results=cursor.fetchall()
    print(results)

def createtable1():
    try:
        sql = "create table stock_basic(`id` int not null auto_increment,`code` varchar(32) not null,`name` varchar(255) null,`industry` varchar(255) null,`timeToMarket` datetime not null,primary key(`id`))engine = innodb auto_increment = 1 default charset='utf8'"
        cursor.execute(sql)
        con.commit()
    except:
        con.rollback()
    results=cursor.fetchall()
    print(results)



def createtable2():
    try:
        sql = "create table daily_price(`id` int not null auto_increment,`stock_id` int not null,`code` varchar(32) not null,`price_date` datetime null,`open` decimal(19,4) null,`close` decimal(19,4) null,`high` decimal(19,4) null,`low` decimal(19,4) null,`volume` decimal(19,4) null,primary key(`id`))engine = innodb auto_increment = 1 default charset='utf8'"
        cursor.execute(sql)
        con.commit()
    except:
        con.rollback()
    results=cursor.fetchall()
    print(results)




def get_stock_basic():
    stocks = ts.get_stock_basics()
    info = []
    for i in range(len(stocks)):
        try:
            s_time = str(stocks['timeToMarket'][i])
            a = datetime.datetime.strptime(s_time,'%Y%m%d')
            b = datetime.datetime.strftime(a,'%Y-%m-%d')
            info.append(
                    (stocks.index[i],
                     stocks['name'][i],
                     stocks['industry'][i],
                     b
                     )
                    )
        except Exception as e:
            pass
    return info

def insert_chinesestock_basic(info):
    con = pymysql.connect(host='192.168.1.74',port=3306,user='root',passwd='password',db='chinesestock',charset='utf8')
    column_str = 'code,name,industry,timeToMarket'
    insert_str = ('%s,'*4)[:-1]
    final_str = "insert into stock_basic (%s) values (%s)"%(column_str,insert_str)
    with con:
        cur = con.cursor()
        cur.executemany(final_str,info)




def get_stock_inf():
    with con:
        cur = con.cursor()
        cur.execute("select id,code from stock_basic")
        data = cur.fetchall()
        return [(d[0], d[1]) for d in data]


def get_daily_hist_data(ticker):
    a = ts.get_k_data(ticker, start='2010-01-01', end='2017-11-16')
    prices = []
    for i in range(len(a)):
        try:
            prices.append(
                (a['code'][a.index[i]],
                 a['date'][a.index[i]],
                 float(a['open'][a.index[i]]),
                 float(a['close'][a.index[i]]),
                 float(a['high'][a.index[i]]),
                 float(a['low'][a.index[i]]),
                 float(a['volume'][a.index[i]])
                 )
            )
        except Exception as e:
            print(e)
    return prices


def insert_daily_data_into_db(stock_id, daily_hist_data):
    daily_data = [
        (stock_id,
         d[0],
         d[1],
         d[2],
         d[3],
         d[4],
         d[5],
         d[6]) for d in daily_hist_data]
    column_str = "stock_id,code,price_date,open,close,high,low,volume"
    insert_str = ("%s," * 8)[:-1]
    final_str = "insert into daily_price(%s) values(%s)" % (column_str, insert_str)
    with con:
        cur = con.cursor()
        cur.executemany(final_str, daily_data)




if __name__ == "__main__":
# createdatabase()
# createtable1()
# createtable2()
    warnings.filterwarnings('ignore')
    tickers = get_stock_inf()
    for i in range(2000, len(tickers)):
        daily_hist = get_daily_hist_data(tickers[i][1])
        insert_daily_data_into_db(tickers[i][0], daily_hist)
    # infos = get_stock_basic()
    # insert_chinesestock_basic(infos)
    # print("%s infos were successfully added."%len(infos))

