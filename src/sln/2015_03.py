def p1(f):
    x = 0
    y = 0
    locs = set()
    locs.add((x, y))
    for move in f:
        if (move == '<'):
            x -= 1
        elif (move == '>'):
            x += 1
        elif (move == 'v'):
            y -= 1
        elif (move == '^'):
            y += 1
        locs.add((x, y))

    return len(locs)

def p2(f):
    x = 0
    y = 0
    rx = 0
    ry = 0
    locs = set()
    locs.add((x, y))
    for i, move in enumerate(f):
        if (move == '<'):
            x -= 1 if (i % 2) == 0 else 0
            rx -= 1 if (i % 2) == 1 else 0
        elif (move == '>'):
            x += 1 if (i % 2) == 0 else 0
            rx += 1 if (i % 2) == 1 else 0
        elif (move == 'v'):
            y -= 1 if (i % 2) == 0 else 0
            ry -= 1 if (i % 2) == 1 else 0
        elif (move == '^'):
            y += 1 if (i % 2) == 0 else 0
            ry += 1 if (i % 2) == 1 else 0
        locs.add((x, y))
        locs.add((rx, ry))

    return len(locs)
