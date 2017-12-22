
# -*- coding: utf-8 -*-
import mail
def onQQMessage(bot, contact, member, content):
    if content == '天气怎么样':
        bot.SendTo(contact, '今天天气不错，晚上可以看星星呢')
    elif content == 'hello':
        bot.SendTo(contact, '你好,我是cortana')
    elif content == '发邮件':
        sendEmail(content)
        bot.SendTo(contact, '邮件已发送')