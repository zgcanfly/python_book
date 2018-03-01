import requests
import json
import subprocess

key = '72641824589b479e96f092da5f31b41e'


# def isAllZh(s):
#     for c in s:
#         if not ('\u4e00' <= c <= '\u9fa5'):
#             return False
#     return True
def onQQMessage(bot, contact, member, content):
    if content == '睡觉':
        bot.SendTo(contact, '好了我睡觉了 拜拜!')
        bot.Stop()
    if content  is not content:
        bot.SendTo(contact,str(content))
    # if '群' in str(content):
    #     if '七宿' in str(content):
    #         pass
    #     elif '@ME' in str(content):
    #         info = content
    #         url = 'http://www.tuling123.com/openapi/api?key=' + key + '&info=' + info
    #         res = requests.get(url)
    #         res.encoding = 'utf-8'
    #         jd = json.loads(res.text)
    #         bot.SendTo(contact, jd['text'])
    # elif '群' not in str(content):
    #     info = content
    #     url = 'http://www.tuling123.com/openapi/api?key=' + key + '&info=' + info
    #     res = requests.get(url)
    #     res.encoding = 'utf-8'
    #     jd = json.loads(res.text)
    #     bot.SendTo(contact, jd['text'])



# def onQQMessage(bot, contact, member, content):
#     if content == '睡觉':
#         bot.SendTo(contact, '好了我睡觉了 拜拜!')
#         bot.Stop()
#     if isAllZh(content):
#         info = content
#         url = 'http://www.tuling123.com/openapi/api?key=' + key + '&info=' + info
#         res = requests.get(url)
#         res.encoding = 'utf-8'
#         jd = json.loads(res.text)
#         bot.SendTo(contact, jd['text'])
#     else:
#         message = subprocess.getstatusoutput(content)
#         message = str(message)
#         bot.SendTo(contact, message)
