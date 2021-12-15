#!/usr/bin/python3
import pickle


class PickleMe:
    def __init__(self):
        self.x = 5
        self.y = 10

pm1 = PickleMe()
p1_str = pickle.dumps(pm1)
print(p1_str)

pm2 = pickle.loads(p1_str)
print(pm2.x)
