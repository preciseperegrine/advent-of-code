import hashlib

def p1(f):
    res = 0
    line = f'{f.strip()}{res}'
    out = hashlib.md5(line.encode()).hexdigest()
    while out[0:5] != "00000":
        res += 1
        line = f'{f.strip()}{res}'
        out = hashlib.md5(line.encode()).hexdigest()

    return res

def p2(f):
    res = 0
    line = f'{f.strip()}{res}'
    out = hashlib.md5(line.encode()).hexdigest()
    while out[0:6] != "000000":
        res += 1
        line = f'{f.strip()}{res}'
        out = hashlib.md5(line.encode()).hexdigest()

    return res
