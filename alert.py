import redis
import json
import time
import sys
import slacker
from slacker import Slacker

#Here is the authorization of slack API interface
try:
    slack = Slacker('xoxp-22802814373-22806102896-22807444626-0748422aad')

    #I connect to Redis here, and get it ready for further work
    conn = redis.Redis()

    while 1:

        pipe = conn.pipeline()
        keys = conn.keys()
        values = conn.mget(keys)

    #Here is the duration I gathered from redis server, and I calculate them here to get 
    #the output rate. After watching the rate outputign for sometime, I noticed that the 
    #rate is normally under 5, so I set the threshold to 6-8. Once the rate exceeds this value
    #we detected unnormal emotion occurs. 
        durs = [float(v) for v in values]

        if len(durs):
            rate = sum(durs)/float(len(durs))
        else:
            rate = 0
        if rate>1.5:
            alert = "What is going on? People in NYC are not very happy! (current negative rate: "+str(rate)+'). '
            #Once the rate is higher than threshold, I push it to the slack channel "#storytelling_emotion"
            slack.chat.post_message('#storytelling_emotion', alert, as_user=True)

        print json.dumps({"rate":rate})
        sys.stdout.flush()

        time.sleep(0.5)
except KeyboardInterrupt:
    exit
