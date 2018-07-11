#coding=utf-8

import redis
# r=redis.Redis(host='localhost',port=6379,db=0)
# r.set('name','baby')

pool=redis.ConnectionPool(host='localhost',port=6379)
r=redis.Redis(connection_pool=pool)
print(r.get('name'))
print(r.dbsize())