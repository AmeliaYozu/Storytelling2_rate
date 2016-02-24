import redis
import json
import time
import sys

conn = redis.Redis()

while 1:

    pipe = conn.pipeline()

    keys = conn.keys()

    values = conn.mget(keys)

    print values
    try:
        durs = [float(v) for v in values]
    except TypeError:
        print keys
        continue

    if len(durs):
        rate = sum(durs)/float(len(durs))
    else:
        rate = 0

    print json.dumps({"rate":rate})
    sys.stdout.flush()

    time.sleep(0.5)