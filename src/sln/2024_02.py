#       -------Part 1--------   --------Part 2--------
# Day       Time  Rank  Score       Time   Rank  Score
#   2   00:30:34  9644      0   20:56:28  85339      0

def p1(f):
    lines = [[int(x) for x in line.split()] for line in f.splitlines()]
    res = 0

    for line in lines:
        last_diff = 0
        valid = True
        for i in range(1, len(line)):
            diff = line[i] - line[i-1]
            if (abs(diff) > 3):
                valid = False
                break
            if (diff > 0 and last_diff < 0) or (diff < 0 and last_diff > 0) or (diff == 0):
                valid = False
                break
            last_diff = diff
        if valid:
            res += 1
    return res

def p2(f):
    lines = [[int(x) for x in line.split()] for line in f.splitlines()]
    res = 0

    for line in lines:
        for i in range(0, len(line)):
            false_arr = line[:i] + line[i+1:]
            if (false_arr not in (sorted(false_arr), sorted(false_arr, reverse=True))):
                continue
            if (not all(1 <= abs(y- x) <= 3 for x, y in zip(false_arr, false_arr[1:]))):
                continue
            res += 1
            break
    return res
