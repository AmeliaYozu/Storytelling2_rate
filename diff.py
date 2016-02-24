import json
import sys
from sys import stdout

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
 