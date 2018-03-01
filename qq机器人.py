''' Python3'''
import requests
import json
key = '72641824589b479e96f092da5f31b41e'
while True:
    info = input('\n我：')
    url = 'http://www.tuling123.com/openapi/api?key='+key+'&info='+info
    res = requests.get(url)
    res.encoding = 'utf-8'
    jd = json.loads(res.text)
    print('\nTuling: '+jd['text'])