from TwitterAPI import TwitterAPI
import json
import time
import ast
from sys import stdout
from sys import stdin
from alchemyapi import AlchemyAPI

i = 1
while(1):
	d = {"time":i,"dur":i*1000}
	i = i+1
	print json.dumps(d)
	stdout.flush()
	time.sleep(1)