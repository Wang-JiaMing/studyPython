import time

import sendMail

from weatherMail import mjWeather

msg = mjWeather.getWeatherMsg() + '\n\n——来自小明AI管家'

sendMailAddress = ['13422192925@163.com', '352294249@qq.com', '601229570@qq.com']
for address in sendMailAddress:
    sendMail.sendMail('小明AI管家-实时天气情况|' + time.strftime("%Y-%m-%d %H:%M", time.localtime()), msg, address)
