#!/bin/python3

import signal
import time
import random
import termcolor as tc


signal.alarm(2)

colors = list(tc.COLORS.keys())
high = list(tc.HIGHLIGHTS.keys())

while True:
    sium = ''
    for word in 'sium':
        sium += random.choice([word, word.upper()]) * random.randint(2, 100)

    text = tc.colored( sium, random.choice(colors), random.choice(high))
    print(text)
    time.sleep( random.randint(0, 100)/1000)
