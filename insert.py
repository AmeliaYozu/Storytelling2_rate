import json
import sys
import redis

conn = redis.Redis()

while 1:
    line = sys.stdin.readline()
    d = json.loads(line)
    text = d["text"]
    time = d["timestamp"]
    conn.setex(time, text, 120)
    print json.dumps({"time":time, "text":text})
