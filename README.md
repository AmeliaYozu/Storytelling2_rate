# Storytelling2_rate

Instruction:
1. To generate and put data in to Redis:
	$ python tt3.py | python get_delta.py | python to_redis.py
2. Open another terminal, open redis-server:
	$ redis-server
3. Run alert.py to monitor rate, once the rate exceeds the threshold, push notification to Slack Channel:
	$ python alert.py

Slack Channel: #storytelling_emotion
