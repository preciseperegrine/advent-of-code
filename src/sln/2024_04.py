#       -------Part 1--------   --------Part 2--------
# Day       Time  Rank  Score       Time   Rank  Score
#   4   00:32:46  6682      0   01:02:52   7963      0

WORD = "XMAS"

def check_letter1(grid, index, x, y, dir_x, dir_y):
    if (index >= len(WORD)):
        return True
    xpos = x + dir_x
    ypos = y + dir_y

    if not (0 <= xpos < len(grid[0])):
        return False
    if not (0 <= ypos < len(grid)):
        return False

    if (grid[ypos][xpos] != WORD[index]):
        return False

    return check_letter1(grid, index+1, xpos, ypos, dir_x, dir_y)


def p1(f):
    res = 0
    grid = [list(line) for line in f.splitlines()]

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == WORD[0]:
                for dir_y in range(-1, 2):
                    for dir_x in range(-1, 2):
                        res += check_letter1(grid, 1, x, y, dir_x, dir_y)
    return res

def p2(f):
    res = 0
    grid = [list(line) for line in f.splitlines()]

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == 'A':
                m_pos = []
                s_pos = []
                for dir_y in range(-1, 2, 2):
                    for dir_x in range(-1, 2, 2):
                        xpos = x + dir_x
                        ypos = y + dir_y
                        if not (0 <= xpos < len(grid[0])):
                            continue
                        if not (0 <= ypos < len(grid)):
                            continue
                        if grid[ypos][xpos] == 'M':
                            m_pos.append([ypos, xpos])
                        if grid[ypos][xpos] == 'S':
                            s_pos.append([ypos, xpos])
                if len(m_pos) == 2 and len(s_pos) == 2:
                    if m_pos[0][0] == m_pos[1][0] or m_pos[0][1] == m_pos[1][1]:
                        res += 1

    return res
