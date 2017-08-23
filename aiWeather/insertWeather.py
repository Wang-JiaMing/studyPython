# -*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import uuid


def getSoup():
    # 网址
    url = "https://tianqi.moji.com/weather/china/guangdong/nansha-district"
    # 请求
    request = urllib.request.Request(url)
    # 爬取结果
    response = urllib.request.urlopen(request)
    data = response.read()
    # 设置解码方式
    data = data.decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    return soup


def getWeatherMsg():
    soup = getSoup();
    sql = """insert into weather(id,overview,province,county,pm25,warning,temperatuer,weather_condition,humidity,
                                  wind_direction,msg_update_time,today_weather,tomorrow_weather,ofter_tomorrow_weather,dress,
                                  influenza,vehicle_cleaning,air,dressing,ultraviolet_rays,sport,go_fishing,create_date) values(uuid.uuid4(),"""
    sql += soup.find_all('meta')[2]['content'].replace('墨迹天气', '小明同学') + ','
    sql += soup.find_all('em')[0].string + "".split('，')[1] + ","
    sql += soup.find_all('em')[0].string + "".split('，')[0] + ","
    sql += soup.find(attrs={'class': 'wea_alert clearfix'}).em.string + ","
    weatherWarning = soup.find(attrs={'class': 'warning_aqi'})
    if weatherWarning != None:
        sql += weatherWarning.select('em')[
                   0].string + ","  # weatherConntent += '现悬挂' + weatherWarning.select('em')[0].string + '预警信号\n\n'
    else:
        sql += '"",'

    # 摄氏度+天气情况
    ssd = soup.find(attrs={'class': 'wea_weather clearfix'})
    # 湿度+风向
    sd_fx = soup.find(attrs={'class': 'wea_about clearfix'})
    sql += ssd.em.string + ','
    sql += ssd.b.string + ','
    sql += sd_fx.span.string + ','
    sql += sd_fx.em.string + ','
    weatherConntent += '天气更新时间:' + ssd.strong.string + '\n\n'
    weatherConntent += '--------天气预报--------\n'
    tqyb = soup.find(attrs={'class': 'forecast clearfix'}).select('ul')
    i = 1
    while i < len(tqyb):
        weatherConntent += tqyb[i].find_all('li')[0].a.string + ' ' + tqyb[i].find_all('li')[1].get_text(
            strip=True) + ' ' + \
                           tqyb[i].find_all('li')[2].string + '(最低温度/最高温度) ' + tqyb[i].find_all('li')[3].em.string + \
                           tqyb[i].find_all('li')[3].b.string + '\n\n'
        i += 1

    weatherConntent += '--------生活指栏--------\n'
    live = soup.find(attrs={'class': 'live_index_grid'}).select('li')
    ii = 0

    while ii < len(live):
        if live[ii].dd != None:
            weatherConntent += live[ii].dd.string + ':' + live[ii].dt.string + '\n\n'
        ii += 1
    print(weatherConntent)
    return weatherConntent


def getWeatherTitle():
    soup = getSoup()
    tip = soup.find(attrs={'class': 'wea_tips clearfix'})
    return tip.em.string


getWeatherMsg()
