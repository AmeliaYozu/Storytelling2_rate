from TwitterAPI import TwitterAPI
import json
import time
import ast
from sys import stdout
from sys import stdin
from alchemyapi import AlchemyAPI

try:
#Tweet Streaming API Keys
    CONSUMER_KEY = '8aIDWdGQuFgC9oypr2yozz6KY'
    CONSUMER_SECRET = 'tn3FJdxt22QrHgim07mmaWOxFhNCtj7BB3pAjNVEw9aVZyECWC'
    ACCESS_TOKEN_KEY = '4883184502-tPuS4S7rC0gEqpGq08EFtkUo1HYTZbskez2YtYu'
    ACCESS_TOKEN_SECRET = '0xS7drlYHYb32ASOCEeeVo8Qx405RAreGkv0S2ARNsVLz'


    #Use AlchemyAPI to get sentiment analysis #need API key, which is stored in api_key.txt
    alchemyapi = AlchemyAPI()

    #connect to TwitterAPI, ready to get stream!
    api = TwitterAPI(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)

    #get stream here with specified location filter to only get Tweets from New York
    r = api.request('statuses/filter', {'locations':'-74,40,-73,41'})

    #Handling each received json format Tweet:
    #The core function of the following for loop is to get text messages and timestamps from
    #the Twitter Stream. Then I used AlchemyAPI to analyze each tweet content and get their emotion direction
    #either positive, neutral or negative. But here we only gather the negitive data, in order to
    #get the rate of the negative tweets showing, hence we can sense if there are lots of people upset, angry or 
    #having other negative emotions. If we deteched a very high rate of negative emotion. It can somewhat tell us
    #some bad event must happened, or there will not be such number of people feeling bad.
    #
    #and I flushed the time out for futher calculation
    for item in r:
       if r.status_code!=404: 

        text = item['text']#get Tweet text
        #get and format timestamp into readable time string
        timestamp = item['timestamp_ms']
        #get sentiment information of Tweet text (1000sentiment per 24 hours)
        response = alchemyapi.sentiment('text', text)
        status = response.get('status')
        if status != 'ERROR':
            feature = response['docSentiment']['type'];
            if str(feature) == "negative":
                print json.dumps({"time":time.time()})
                stdout.flush()
except KeyboardInterrupt:
    exit
            

    