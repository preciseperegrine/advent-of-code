def p1(f):
    lines = [[int(x) for x in line.split('x')] for line in f.splitlines()]
    res = 0

    for line in lines:
        f1 = line[0] * line[1]
        f2 = line[0] * line[2]
        f3 = line[1] * line[2]
        minimum = min(f1, min(f2, f3))
        res += 2*f1 + 2*f2 + 2*f3 + minimum

    return res

def p2(f):
    lines = [[int(x) for x in line.split('x')] for line in f.splitlines()]
    res = 0

    for line in lines:
        sline = sorted(line)
        res += 2*sline[0] + 2*sline[1] + (line[0] * line[1] * line[2])

    return res
