#coding:utf-8
import hashlib
def encryption(encryption_code):
    m = hashlib.md5()  # 创建md5对象
    m.update(encryption_code.encode("utf8")) # 生成加密串，其中password是要加密的字符串
    return m.hexdigest()

if __name__=='__main__':
    string='ztoyc'+'xwms-dev'
    print(encryption(string))