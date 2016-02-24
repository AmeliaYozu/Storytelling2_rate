import json
import sys
import redis

conn = redis.Redis()

while 1:
	line = sys.stdin.readline()
	d = json.loads(str.strip(line))
	print d
	time = d["time"]
	dur = d["dur"]
	conn.setex(time, dur, 60)
	print json.dumps({"time":time, "dur":dur})
