from TwitterAPI import TwitterAPI
import json
import time
import ast
from sys import stdout
from sys import stdin
from alchemyapi import AlchemyAPI

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
#Extract userID, user name, Tweet content, Tweet time&location information and sentiment analysis result
#for each Tweet text, as 'mood'.
#
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
        if str(feature) != "negative":
            print json.dumps({"time":time.time()})
            stdout.flush()
        

    