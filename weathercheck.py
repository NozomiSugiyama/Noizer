#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

from net import httpclient


class WeatherCheck(httpclient.HttpClient):
    def __init__(self):
        print('Starting WeatherCheck')
        requests_url = 'http://weather.livedoor.com/area/forecast/130010'
        super().__init__(requests_url)
        html_class_name_weather = 'icon'
        html_class_name_max_temp = 'maxtemp'
        html_class_name_min_temp = 'mintemp'

        r = requests.get(requests_url)

        self.__status_code = r.status_code
        self.__encoding = r.encoding

        soup = BeautifulSoup(r.text, 'html.parser')
        self.weather_list = soup.findAll(class_=html_class_name_weather)
        self.max_temp = soup.findAll(class_=html_class_name_max_temp)
        self.min_temp = soup.findAll(class_=html_class_name_min_temp)
        self.overview = soup.find(class_='gaikyo')

    def get_status_code(self):
        return self.__status_code

    def get_encoding(self):
        return self.__encoding

    def get_today_weather(self):
        today_weather = self._html_format(str(self.weather_list[0]))
        return today_weather

    def get_tomorrow_weather(self):
        tomorrow_weather = self._html_format(str(self.weather_list[1]))
        return tomorrow_weather

    def get_temp(self, max_min, day='today'):

        undefined_check = '---'
        num = 1

        if day == 'tomorrow':
            num += 2

        if max_min == 'max':
            temp = self._html_format(str(self.max_temp[num]))
            if temp == undefined_check:
                temp = '不明'
        elif max_min == 'min':
            temp = self._html_format(str(self.min_temp[num]))
            if temp == undefined_check:
                temp = '不明'
        else:
            temp = 'エラー'

        return temp

    def get_overview(self):
        overview = self._html_format(str(self.overview))
        return overview
