#       -------Part 1--------   -------Part 2--------
# Day       Time  Rank  Score       Time  Rank  Score
#   1   00:07:43  3385      0   00:10:47  2962      0

def p1(blob):
    lines = blob.splitlines()
    res = 0
    left = []
    right = []
    for line in lines:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    for i in range(0, len(lines)):
        res += abs(left[i] - right[i])

    return res

def p2(blob):
    lines = blob.splitlines()
    res = 0

    left = []
    right = []
    for line in lines:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    for l in left:
        res += l * right.count(l)

    return res
