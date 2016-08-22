#! /bin/python
# -*- coding: utf-8 -*-

import tweepy
from tweepy.error import TweepError


class TwitterClient(tweepy.API):
    def __init__(self, CK, CS, AT, AS):
        self.auth = tweepy.OAuthHandler(CK, CS)
        self.auth.set_access_token(AT, AS)
        super().__init__(self.auth)

    def follower_username(self, count):
        follower_list = {}
        try:
            pos = 1
            for user in tweepy.Cursor(self.followers, count=count, cursor=-1).items():
                follower_list.update({user.screen_name: str(user.name)})
                pos += 1

        except TweepError as e:
            follower_list.update({'error': '-----'})
            print(e)

        return follower_list

    def follower_user(self, count):
        follower_list = []
        """
        dir(user)
        ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
         '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__',
         '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
         '__subclasshook__', '__weakref__', '_api', '_json', 'blocked_by', 'blocking', 'contributors_enabled',
         'created_at', 'default_profile', 'default_profile_image', 'description', 'entities', 'favourites_count',
         'follow', 'follow_request_sent', 'followers', 'followers_count', 'followers_ids', 'following', 'friends',
         'friends_count', 'geo_enabled', 'has_extended_profile', 'id', 'id_str', 'is_translation_enabled',
         'is_translator', 'lang', 'listed_count', 'lists', 'lists_memberships', 'lists_subscriptions', 'location',
         'muting', 'name', 'notifications', 'parse', 'parse_list', 'profile_background_color',
         'profile_background_image_url', 'profile_background_image_url_https', 'profile_background_tile',
         'profile_banner_url', 'profile_image_url', 'profile_image_url_https', 'profile_link_color',
         'profile_sidebar_border_color', 'profile_sidebar_fill_color', 'profile_text_color',
         'profile_use_background_image', 'protected', 'screen_name', 'status', 'statuses_count', 'time_zone',
         'timeline', 'unfollow', 'url', 'utc_offset', 'verified']
        """
        try:
            pos = 1
            for user in tweepy.Cursor(self.followers, count=count, cursor=-1).items():
                print(dir(user))
                follower_list.append(user)
                pos += 1

        except TweepError as e:
            follower_list.append('-error-')
            print(e)

        return follower_list

    def get_time_line(self, user_id):
        print(tweepy.Cursor(self.user_timeline, id=user_id).items())
        return tweepy.Cursor(self.user_timeline, id=user_id).items(1)
