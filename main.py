#! /bin/python
# -*- coding: utf-8 -*-


import datetime, sys, os
import time
from newscheck import NewsCheck
from weathercheck import WeatherCheck
from createtalk import CreateTalk, print_log, pygame_alert, pyaudio_alert

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    today = datetime.datetime.today().strftime('%Y_%m_%d_%H_%M_%S')
    dir_name = 'data/' + today

    weather_check = WeatherCheck()
    news_check = NewsCheck()

    weekday = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    date_talk = datetime.datetime.today().strftime('%Y年%m月%d日') + '、' + weekday[datetime.date.today().weekday()] + 'です。'
    weather_talk = '今日の天気は、' + weather_check.get_today_weather() + 'です。'
    temp_talk = '最高気温は、' + weather_check.get_temp('max') + '。' + '最低気温は、' + weather_check.get_temp('min') + 'です。'
    rss_news_talk = '今日の主要なニュース。ひとつ目は、' + news_check.get_rss_news_title(1) + '。次に、' + news_check.get_rss_news_title(2)
    rss_news_talk_2 = '。次に、' + news_check.get_rss_news_title(3) + '。最後に、' + news_check.get_rss_news_title(4) + '。以上です。'

    filename_weather = 'weather.wav'
    filename_news_1 = 'news.wav'
    filename_news_2 = 'news2.wav'


    speaker = 'hikari'

    CreateTalk.create_talk(date_talk + weather_talk + temp_talk, filename_weather, dir_name, speaker=speaker)
    CreateTalk.create_talk(rss_news_talk, filename_news_1, dir_name, speaker=speaker)
    CreateTalk.create_talk(rss_news_talk_2, filename_news_2, dir_name, speaker=speaker)

    @print_log
    @pygame_alert
    def talk():
        CreateTalk.pygame_speak(filename_weather, dir_name)
        time.sleep(1)
        CreateTalk.pygame_speak(filename_news_1, dir_name)
        time.sleep(1)
        CreateTalk.pygame_speak(filename_news_2, dir_name)


    talk()

if __name__ == '__main__':
    while True:

        alarm_hour = 1
        alarm_minute = 17

        now = datetime.datetime.today()

        if now.hour == alarm_hour and now.minute == alarm_minute:
            main()

        # list内方式
        # Reactiveプログラミング
        #
        # map
        time.sleep(10)
