import math
import os
import time
import wave
import pyaudio
import pygame
import requests


class CreateTalk:
    @staticmethod
    def create_talk(talk_content, file_name, fire_dir_name=None, speaker='hikari'):
        print('creating' + file_name)
        requests_url = 'https://api.voicetext.jp/v1/tts'
        username = 'gelg4d8cjdjxgt15'

        form = {'text': talk_content, 'speaker': speaker}
        talk_sound = requests.post(requests_url, auth=(username, ''), data=form)

        if fire_dir_name is not None and not (os.path.exists(fire_dir_name)):
            os.mkdir(fire_dir_name)
        with open(fire_dir_name + '/' + file_name, 'wb') as weather_sound:
            for chunk in talk_sound.iter_content(chunk_size=1024):
                weather_sound.write(chunk)

        print('create' + file_name)

    @staticmethod
    def pyaudio_speak(filename, file_dir_name=None):
        print('pyaudio_speak')
        if file_dir_name is not None:
            file_dir_name += '/'
            file = (file_dir_name + filename)
        else:
            file = filename
        wf = wave.open(file, 'r')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # チャンク単位でストリームに出力し音声を再生
        chunk = 102400000

        data = wf.readframes(chunk)
        stream.write(data)

        #  後で直して
        # while(data != ''):
        #    stream.write(data)
        #    data = wf.readframes(1024)

        stream.close()
        p.terminate()

    @staticmethod
    def pygame_speak(filename, file_dir_name=None):
        print('pygame_speak')
        if file_dir_name is not None:
            file_dir_name += '/'
            file = file_dir_name + filename
        else:
            file = filename

        play_time = 3
        wf = wave.open(file, 'r')
        print('wave_open : ' + file)
        play_time = math.ceil(float(wf.getnframes()) / wf.getframerate())
        print('wave_close : ' + file)
        wf.close()

        pygame.mixer.init(frequency=44100)  # 初期設定
        pygame.mixer.music.load(file)  # 音楽ファイルの読み込み
        pygame.mixer.music.play(1)  # 音楽の再生回数(ループ再生)
        time.sleep(play_time)  # 音楽の再生時間
        pygame.mixer.music.stop()  # 再生の終了


def pyaudio_alert(func):
    import functools
    import time
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        CreateTalk.pyaudio_speak('Alarm_1.wav')
        time.sleep(1)
        CreateTalk.pyaudio_speak('good_morning.wav')
        time.sleep(1)
        func(*args, **kwargs)
        time.sleep(1)
        CreateTalk.pyaudio_speak('Alarm_1.wav')

    return wrapper


def pygame_alert(func):
    import functools
    import time
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        CreateTalk.pygame_speak('Alarm_1.wav')
        time.sleep(1)
        CreateTalk.pygame_speak('good_morning.wav')
        time.sleep(1)
        func(*args, **kwargs)
        time.sleep(1)
        CreateTalk.pygame_speak('Alarm_1.wav')

    return wrapper


def print_log(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(os.path.dirname(os.path.abspath(__file__)))
        print('-----talk_start-----')
        func(*args, **kwargs)
        print('-----talk   end-----')

    return wrapper
