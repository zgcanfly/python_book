#coding:utf-8

from  werkzeug.contrib.cache import GAEMemcachedCache,SimpleCache
cache = SimpleCache()

# def get_my_item():
#     rv = cache.get('my-item')
#     if rv is None:
#         cache.set('my-item','flask',timeout=5 * 60 )
#     return rv
#
# print(get_my_item())

# cache.set('my-item','flask')
rv=cache.get('my-item')
print(rv)