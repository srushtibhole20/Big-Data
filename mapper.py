#!/usr/bin/env python3

import sys
import re

for line in sys.stdin:
    line = line.strip()

    hashtags = re.findall(r'#\w+', line)

    for hashtag in hashtags:
        print(f"{hashtag}\t1")
