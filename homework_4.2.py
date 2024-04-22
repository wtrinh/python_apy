"""
    homework_4.2.py -- build a dict from web server log and sum up server usage
    Author: Winston Trinh (nvth@hotmail.com)
    Last Revised: 04/21/2024
"""

import re

fh = open('access_log.txt')                                     # file object
lines = fh.readlines()                                          # dict, ['172.26.93.208 - - [28/Jun/2012:21:00:17 -0400] "GET /~cmk380/pythondata/image2b.txt HTTP/1.1" 200 30\n'
dod = {}

for line in lines:                                              # str, '172.26.93.208 - - [28/Jun/2012:21:00:17 -0400] "GET /~cmk380/pythondata/image2b.txt HTTP/1.1" 200 30\n'
    userid_match = re.search(r'~[a-z]{2,3}[0-9]{2,3}', line)    # class, <re.Match object; span=(53, 60), match='~cmk380'>
    if userid_match:                                            # bool, true
        userid = userid_match.group().lstrip('~')               # str, 'cmk380'
        byte_match = re.search(r'200\s\d+$', line)              # class, <re.Match object; span=(94, 100), match='200 30'>
        if byte_match:                                          # bool, true
            key = f'{userid}'                                   # str, 'cmk380'
            if not key in dod:                                  # bool, true
                dod[key] = 0                                    # int, 0
            dod[key] += int(byte_match.group().lstrip('200'))   # str, '30'

for key,value in dod.items():                                   # tuple, ('cmk380', 135724)
    if value > 10000000:
        print(f'{key}: {value}')