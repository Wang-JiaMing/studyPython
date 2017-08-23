#!/usr/bin/python
# -*- coding: UTF-8 -*-
class weather:
    id = ''
    overview = ''
    province = ''
    county = ''
    temperature = ''
    weatherCondition = ''
    humidity = ''
    windDiretion = ''
    msgUpdateTime = ''
    todayWeather = ''
    tomorrowWeather = ''
    ofterTomorrowWeather = ''
    dress = ''
    influenza = ''
    vehicleCleaning = ''
    air = ''
    dressing = ''
    ultravoiletRays = ''
    sport = ''
    goFishing = ''
    createDate = ''

    def __init__(self, overview, province, county, temperature, weatherCondition, humidity, windDiretion, msgUpdateTime,
                 todayWeather, tomorrowWeather, ofterTomorrowWeather,
                 dress, influenza, vehicleCleaning, air, dressing, ultravoiletRays, sport, goFishing, createDate):
        self.overview = overview
        self.province = province
        self.county = county
        self.temperature = temperature
        self.weatherCondition = weatherCondition
        self.humidity = humidity
        self.windDiretion = windDiretion
        self.msgUpdateTime = msgUpdateTime
        self.todayWeather = todayWeather
        self.tomorrowWeather = tomorrowWeather
        self.ofterTomorrowWeather = ofterTomorrowWeather
        self.dress = dress
        self.influenza = influenza
        self.vehicleCleaning = vehicleCleaning
        self.air = air
        self.dressing = dressing
        self.ultravoiletRays = ultravoiletRays
        self.sport = sport
        self.goFishing = goFishing
        self.createDate = createDate
