def p1(f):
    lines = f.splitlines()
    res = 0

    lookup = {}
    mapping_flag = True
    for line in lines:
        if (line == ""):
            mapping_flag = False
            continue
        if (mapping_flag):
            first, second = [int(val) for val in line.split("|")]
            if first not in lookup:
                lookup[first] = []
            lookup[first].append(second)
            continue
        valid = True
        entries = [int(val) for val in line.split(",")]
        for i in range(0, len(entries)-1):
            if entries[i] not in lookup:
                valid = False
                break;
            if entries[i+1] not in lookup[entries[i]]:
                valid = False
                break;
        if valid:
            res += entries[int((len(entries)-1)/2)]

    return res

def p2(f):
    res = 0
    pairs, updates = [x.splitlines() for x in f.split("\n\n")]
    pairs = [[int(x) for x in p.split("|")] for p in pairs]
    updates = [[int(x) for x in u.split(",")] for u in updates]

    for i in range(0, len(updates)):
        update = updates[i]
        was_updated = False
        for j in range(len(update)):
            for k in range(j+1, len(update)):
                if [update[j], update[k]] in pairs:
                    continue
                else:
                    update[j], update[k] = update[k], update[j]
                    was_updated = True
        if was_updated:
            res += update[int((len(update)-1)/2)]

    return res
