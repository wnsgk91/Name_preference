#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 22:18:46 2018

@author: ck
"""
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import random
import tweepy
import os
import json
import io
from datetime import datetime
import re
####트위터 개발자 정보를 입력해 줍니다.
consumer_key = "4oqZjge7qM0n3WNftJiKHFtOF"
consumer_secret = "CZOzvRcdwFOzPZFoM5igXVGBbOBp7lQWBBtCRe76wuv738equP"
access_token = "1004411169568747520-7NBYDlDKlGXX9q5gjXasgRRo5p3HtT"
access_token_secret = "b3BSPhEfHGYCxuIaNPg1CFcJtKkCWnjIZESooDgT99GWL"

#개발자 인증을 받습니다.
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_delay=10)


#트윗 크롤링을 날짜 기준으로 저장합니다.
def get_tweets(keyword, num_limit):
    i=0
    for tweet in tweepy.Cursor(api.search, q=keyword, since='2018-11-01', until='2018-12-10',lang="ko").items(num_limit):
        StatusObject = tweet._json
        dict1 = {
                'id': StatusObject['id_str'],
                'permalink':"",
                'username':StatusObject['user']['name'],
                'text': StatusObject['text'],
                'date':StatusObject['created_at'],
                'retweets': StatusObject['retweet_count'],
                'favorites': StatusObject['favorite_count'],
                'mentions':StatusObject['entities']['user_mentions'],
                'hashtags':StatusObject['entities']['hashtags'],
                'geo':StatusObject['geo']
                }
        ##print(str(i)+':'+str(dict1))
        
        ####날짜 형태 변환하기####
        unformatted = StatusObject['created_at']
        # Use re to get rid of the milliseconds.
        remove_ms = lambda x:re.sub("\+\d+\s","",x)
        # Make the string into a datetime object.
        mk_dt = lambda x:datetime.strptime(remove_ms(x), "%a %b %d %H:%M:%S %Y")
        # Format your datetime object.
        my_form = lambda x:"{:%Y-%m-%d}".format(mk_dt(x))
        formatted = my_form(unformatted)
        #print(formatted)
        ####날짜 형태 변환하기####
        dirname = "/Users/junha_lee/Documents/Junha/School/Projects/SentimentName/sentiment/tmp_twitter/"+keyword
        if not os.path.isdir("/Users/junha_lee/Documents/Junha/School/Projects/SentimentName/sentiment/tmp_twitter/"+keyword):
            os.mkdir("/Users/junha_lee/Documents/Junha/School/Projects/SentimentName/sentiment/tmp_twitter/"+keyword)
    
        with open("/Users/junha_lee/Documents/Junha/School/Projects/SentimentName/sentiment/tmp_twitter/"+keyword+"/{}.json".format(str(formatted)),'a+',encoding="utf-8") as make_file:
            twitter = json.dumps(dict1, ensure_ascii=False, indent=2)
            make_file.write(twitter+',')
    i+=1
            
#크롤링 대상을 명시합니다.
def crawl():
    keyword = input()
    num_limit = 100
    get_tweets(keyword, num_limit)


#메인에서 작업 진행을 합니다.
if __name__ == '__main__':
    crawl()