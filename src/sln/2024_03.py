#       -------Part 1--------   --------Part 2--------
# Day       Time  Rank  Score       Time   Rank  Score
#   3   00:10:32  4454      0   00:16:21   2685      0

import re

def p1(f):
    arr = re.findall(r'mul\([0-9]+\,[0-9]+\)', f)
    res = 0

    for mul in arr:
        left, right = mul[4:-1].split(',')
        res += (int(left) * int(right))

    return res

def p2(f):
    arr = re.findall(r'mul\([0-9]+\,[0-9]+\)|do\(\)|don\'t\(\)', f)
    res = 0

    do = True
    for mul in arr:
        if mul[0:3] == 'don':
            do = False
        elif mul[0:2] == 'do':
            do = True
        elif do:
            left, right = mul[4:-1].split(',')
            res += (int(left) * int(right))

    return res
