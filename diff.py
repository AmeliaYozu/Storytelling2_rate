import json
import sys

last = 0
while 1:
    line = sys.stdin.readline()
    d = json.loads(line)
    if last == 0 :
    #	print d["timestamp"]
        last = d["timestamp"]
        continue
    delta = d["timestamp"] - last
    print json.dumps({"delta":delta, "time":d["timestamp"]})
    sys.stdout.flush()
    last = d["timestamp"]
