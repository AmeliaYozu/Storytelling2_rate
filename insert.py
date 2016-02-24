import json
import sys
import redis

conn = redis.Redis()

while 1:
    line = sys.stdin.readline()
    d = json.loads(line)
    time = d["time"]
    delta = d["delta"]
    conn.setex(time, delta, 60)
    print json.dumps({"time":time, "delta":delta})
