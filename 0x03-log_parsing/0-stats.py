#!/usr/bin/python3
"""
read stdin line by line and compute metrics
"""

import sys

# cache for storing HTTP status codes and their counts
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}

# variables for storing total size and counter for every 10 lines
total = 0
counter = 0

try:
    for l in sys.stdin:
        line_list = l.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total += size
            counter += 1

        # print metrics every 10 lines
        if counter == 10:
            counter = 0
            print('File size: {}'.format(total))
            for key, val in sorted(cache.items()):
                if val != 0:
                    print('{}: {}'.format(key, val))

except Exception as err:
    pass

finally:
    # print final metrics
    print('File size: {}'.format(total))
    for key, val in sorted(cache.items()):
        if val != 0:
            print('{}: {}'.format(key, val))
