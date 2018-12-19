from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import random
import tweepy

import os 

import json
import io

# Go to http://dev.twitter.com and create an app. 
# The consumer key and secret as well as the access_token and secret will be generated for you after you register with Twitter Developers
consumer_key = "4oqZjge7qM0n3WNftJiKHFtOF"
consumer_secret = "CZOzvRcdwFOzPZFoM5igXVGBbOBp7lQWBBtCRe76wuv738equP"
access_token = "1004411169568747520-7NBYDlDKlGXX9q5gjXasgRRo5p3HtT"
access_token_secret = "b3BSPhEfHGYCxuIaNPg1CFcJtKkCWnjIZESooDgT99GWL"


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_delay=10)

#wfile = open("C:/Users/wlgo6/Desktop/kvs_code/all/clo.json", mode='w', encoding='utf-8')        # 텍스트 파일로 출력(쓰기모드)


def get_tweets(listOfTweets, keyword, numOfTweets):
    # Iterate through all tweets containing the given word, api search mode
    i=0
    with open('/Users/junha_lee/Desktop/c.json', 'a', encoding='utf-8') as outfile: 
        for tweet in tweepy.Cursor(api.search, q=keyword, since='2008-01-01').items(numOfTweets):
            # Add tweets in this format        # listOfTweets.append(dict_)
            # print(tweet)
            # print("stop")
            raw_data = tweet._json

            dict1 = {
                    'created_at':raw_data['created_at'],
                    'id': raw_data['id'],
                    'id_str': raw_data['id_str'],
                    'text': raw_data['text'],
                    'truncated': raw_data['truncated'],
                    'is_quote_status': raw_data['is_quote_status'],

                    'retweet_count': raw_data['retweet_count'],
                    'favorite_count': raw_data['favorite_count'],
                    'favorited':raw_data['favorited'],
                    'retweeted':raw_data['retweeted'],
                    'lang':raw_data['lang'],
                    'source':raw_data['source'],
                    'in_reply_to_status_id':raw_data['in_reply_to_status_id'],
                    'in_reply_to_status_id_str':raw_data['in_reply_to_status_id_str'],
                    'in_reply_to_user_id':raw_data['in_reply_to_user_id'],
                    'in_reply_to_user_id_str':raw_data['in_reply_to_user_id_str'],
                    'in_reply_to_screen_name':raw_data['in_reply_to_screen_name'],
                    'is_quote_status':raw_data['is_quote_status'],

                    'hashtags':raw_data['entities']['hashtags'],
                    'symbols':raw_data['entities']['symbols'],
                    'user_mentions':raw_data['entities']['user_mentions'],
                    'urls':raw_data['entities']['urls'],

                    'iso_language_code':raw_data['metadata']['iso_language_code'],
                    'result_type':raw_data['metadata']['result_type'],

                    'geo':raw_data['geo'],
                    'coordinates':raw_data['coordinates'],
                    'place':raw_data['place'],
                    #없음 'quote_count': raw_data['quote_count'], ==> 프리미엄 결제를 해야 뽑힘  
                    #없음 'reply_count': raw_data['reply_count'], ==> 프리미엄 결제를 해야 뽑힘  
                    #없음 'filter_level': raw_data['filter_level'], ==> filter API를 써야 뽑히는 column
                    #없음 'matching_rules':raw_data['matching_rules'], ==> ㄹfilter API를 써야 뽑히는 column 
                    #'possibly_sensitive':raw_data['entities']['urls']['possibly_sensitive'], ==> retweet_status에서 등장 
                    # 'quoted_status_id': raw_data['quoted_status_id'], ==>  retweet_status에서 등장 
                    # 'quoted_status_id_str':raw_data['quoted_status_id'] ==>  retweet_status에서 등장 

                    }
            #print(dict_)
            print(str(i))


            twitter=json.dumps(dict1, indent=4, ensure_ascii=False)
            outfile.write(twitter+',')
            i+=1    


def main():
#    l = StdOutListener()    
    i=0
    listOfTweets=[]
    keyword='lol'
    numOfTweets=10000000000

    get_tweets(listOfTweets, keyword, numOfTweets)




if __name__ == '__main__':
    main()