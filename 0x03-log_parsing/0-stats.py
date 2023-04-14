#!/usr/bin/python3
"""
read stdin line by line and compute metrics
"""

import sys

cache = {"200": 0, "301": 0, "400": 0, "401": 0,
         "403": 0, "404": 0, "405": 0, "500":0}

total = 0
counter = 0

try:
    for l in sys.stdin:
        l_list = l.split(" ")
        if len(l_list) > 4:
            code = l_list[-2]
            size = int(l_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total += size
            counter += 1
        
        if counter == 10:
            counter = 0
            print("File size: {}".format(total))
            for key, val in sorted(cache.items()):
                if val != 0:
                    print("{}: {}".format(key, val))

except Exception as err:
    pass

finally:
    print("File size: {}".format(total))
    for key, val in sorted(cache.items()):
        if val != 0:
            print("{}: {}".format(key, val))
