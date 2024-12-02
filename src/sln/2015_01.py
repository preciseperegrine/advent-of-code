def p1(f):
    lines = f.splitlines()
    res = 0

    for l in lines:
        for c in l:
            if (c == '('):
                res += 1
            elif (c == ')'):
                res -= 1

    return res

def p2(f):
    lines = f.splitlines()
    res = 0
    cnt = 0

    for l in lines:
        for c in l:
            if (c == '('):
                res += 1
            elif (c == ')'):
                res -= 1
            cnt += 1

            if (res < 0):
                return cnt

    return cnt
