#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import feedparser
import requests

from src.net import httpclient


class NewsCheck(httpclient.HttpClient):
    def __init__(self):
        print('Starting NewsCheck')
        requests_url = 'http://rss.dailynews.yahoo.co.jp/fc/rss.xml'
        super().__init__(requests_url)

        r = requests.get(requests_url)

        self.__status_code = r.status_code
        self.__encoding = r.encoding
        dom = feedparser.parse(r.text)

        self.__rss_news_title = []
        for entry in dom.entries:
            self.__rss_news_title.append(entry.title)

    def get_status_code(self):
        return self.__status_code

    def get_encoding(self):
        return self.__encoding

    def get_rss_news_title(self, num=None):
        if num is None:
            return self.__rss_news_title
        else:
            return self.__rss_news_title[num]
