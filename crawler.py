#이게 oAuth포함한 전체 코드
import tweepy
#import csv
import pandas as pd

####input your credentials here



consumer_key = "4oqZjge7qM0n3WNftJiKHFtOF"
consumer_secret = "CZOzvRcdwFOzPZFoM5igXVGBbOBp7lQWBBtCRe76wuv738equP"
access_token = "1004411169568747520-7NBYDlDKlGXX9q5gjXasgRRo5p3HtT"
access_token_secret = "b3BSPhEfHGYCxuIaNPg1CFcJtKkCWnjIZESooDgT99GWL"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines

# Open/Create a file to append data
#csvFile = open('ua.csv', 'a')

#Use csv Writer
#csvWriter = csv.writer(csvFile)
print("[")
for tweet in tweepy.Cursor(api.search,
							q="이준하",
							count=10,
                        	lang="ko",
                        	since="2018-11-01").items():
    print ("{\"id\":",tweet.id,",\"name\":",tweet.user.name ,",\"text\":" , tweet.text,",\"date\":" ,tweet.created_at,",\"retweets\":0,\"favorites\":0,\"mentions\":\"\",\"hashtags\":\"\",\"geo\":\"\"}")
print("]")
    #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])