import json
import sys
import redis

try:
	conn = redis.Redis()

	#In this file, I received the incoming data flushed out from get_delta file.
	#And put them into Redis server for futher monitoring. 
	#Here I set time 60s to hold the data in the server
	while 1:
		line = sys.stdin.readline()
		d = json.loads(str.strip(line))
		print d
		time = d["time"]
		dur = d["dur"]
		conn.setex(time, dur, 120)
		print json.dumps({"time":time, "dur":dur})
except KeyboardInterrupt:
	exit