import json
import sys
from sys import stdout

#In this code, I received the incoming stream from tt3.py, which generates 
#time when tweets are created. And I process these time here to calculate them and 
#get the duration between each message and the following one
#Eventually, flush them out for futher calculation
try:
	last = 0
	while 1:
	    line = sys.stdin.readline()
	    d = json.loads(str.strip(line))
	    if last == 0:
	        last = d['time']
	        continue
	    dur = d['time']-last
	    print json.dumps({"time":d['time'],"dur": dur})
	    last = d['time']
	    stdout.flush()
except KeyboardInterrupt:
	exit
	 