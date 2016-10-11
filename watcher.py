import os, sys, time
import datetime
import socket
import threading

from createtalk import CreateTalk, pygame_alert
from createtalk import print_log
from newscheck import NewsCheck
from weathercheck import WeatherCheck


class WatcherApi:
    def __init__(self, port=6789):
        list = []
        for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]:
            s.connect(('8.8.8.8', 80))
            nlist = s.getsockname()
            for n in nlist:
                name = nlist[0]
                list.append(name)
            s.close()

        self.stop_event = False
        self.server_info = (list[0], port)
        self.max_size = 1000

        self.ALARM_HOUR = 6
        self.ALARM_MINUTE = 30
        self.alarm_repeat_minute = 30
        self.alarm_repeat_num = 4

        threading.Thread(target=self.server_start).start()
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        print('Starting watcher')
        for now in iter(datetime.datetime.today, ()):
            self.stop_event = False
            if now.hour == self.ALARM_HOUR and now.minute == self.ALARM_MINUTE:
                self.alarm_start()
                time.sleep(self.alarm_repeat_minute * 60)
        time.sleep(30)

    def alarm_start(self):
        if not self.stop_event:
            for i in range(self.alarm_repeat_num):
                if not self.stop_event:
                    today = datetime.datetime.today().strftime('%Y_%m_%d_%H_%M_%S')

                    DIR_NAME = 'data/' + today
                    if not os.path.exists('data'):
                        os.mkdir('data')

                    weather_check = WeatherCheck()
                    news_check = NewsCheck()

                    weekday = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
                    date_talk = datetime.datetime.today().strftime('%Y年%m月%d日') + '、' + weekday[
                        datetime.date.today().weekday()] + 'です。'
                    weather_talk = '今日の天気は、' + weather_check.get_today_weather() + 'です。'
                    temp_talk = '最高気温は、' + weather_check.get_temp('max') + '。' + '最低気温は、' + weather_check.get_temp(
                            'min') + 'です。'
                    rss_news_talk = '今日の主要なニュース。ひとつ目は、' + news_check.get_rss_news_title(1) + '。次に、'\
                                    + news_check.get_rss_news_title(2)
                    rss_news_talk_2 = '。次に、' + news_check.get_rss_news_title(3) + '。最後に、' \
                                + news_check.get_rss_news_title(4) + '。以上です。'

                    filename_weather = 'weather.wav'
                    filename_news_1 = 'news.wav'
                    filename_news_2 = 'news2.wav'

                    speaker = 'hikari'

                    CreateTalk.create_talk(date_talk + weather_talk + temp_talk, filename_weather, DIR_NAME, speaker=speaker)
                    CreateTalk.create_talk(rss_news_talk, filename_news_1, DIR_NAME, speaker=speaker)
                    CreateTalk.create_talk(rss_news_talk_2, filename_news_2, DIR_NAME, speaker=speaker)

                    @print_log
                    @pygame_alert
                    def talk():
                        if not self.stop_event:
                            CreateTalk.pygame_speak(filename_weather, DIR_NAME)
                            time.sleep(1)
                        if not self.stop_event:
                            CreateTalk.pygame_speak(filename_news_1, DIR_NAME)
                            time.sleep(1)
                        if not self.stop_event:
                            CreateTalk.pygame_speak(filename_news_2, DIR_NAME)

                    talk()

        self.stop_event = False
        print('-- watcher is the end --')

    def server_start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.bind(self.server_info)
        except Exception:
            print('Waiting for the end of the process.')
            time.sleep(10)

        print('Starting the server at', datetime.datetime.now())
        print('Waiting for a client to call.')
        while True:
            server.listen(5)

            client, addr = server.accept()
            data = client.recv(self.max_size)

            print('At', datetime.datetime.now(), client, 'said', data)
            self.stop_event = True
            client.sendall(b'stop event = true')
            client.close()
        server.close()

        print('Reset connection')

if __name__ == '__main__':
    a = WatcherApi(6789)

    #プロトコルバッファー

