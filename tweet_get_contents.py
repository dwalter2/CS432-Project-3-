import twitter
import tweepy
import csv
import textblob

acc = tweepy.OAuthHandler('sK5JvXtJDPrwq7ipwjZ7LANrW','iBUoOOiEmV2JCy2XgjSuzPwSp6vLKPlAh8lm2P0pzWDFTIQD1b')
auth.set_access_token('861494809-LqLi9nv22p982DNzBR32DNrDfvdeWGhgbvYTESiv','5CQ9PcKqPFcF0W7uaO5DgtYpS4SG2uiNZ8JYqg9v2XmO4')
twit_api = tweepy.API(acc)

temp_f = [] #holds full list of twitter ids
req_tweets_ids = [] #holds every third tweet from original list of twitter ids
cov_tweets = [] #stores the actual tweets
cov_dates = [] #stores the date of the tweet with matching index of list
f = open('ny_covid_tweets.txt','r')
try:
    temp_f = list(f) #opens list of original tweet ids and stores them in a list 
finally:
    f.close()
temp_f = temp_f[1:] #cuts off first line from file because it isn't a tweet id   
for i,t in enumerate(temp_f, start=0):  #puts every third tweet id into the req_tweets
    if(i % 3 == 0):
        req_tweets_ids.append(temp_f[i])
if(len(req_tweets_ids <= 25000)): #makes sure the tweet ids list being used doesn't go over api limit
    for i in req_tweets_ids: #uses api to get the tweet content and the date of the tweet. 
        cur_tweet = twit_api.get_status(i)
        cov_tweets.append(cur_tweet.text)
        date = curr_tweet.created_at
        date = date.split(' ')
        date = date[0]
        cov_dates.append(date)


