def p1(f):
    lines = f.splitlines()
    res = 0

    vowels = "aeiou"
    disallow = ["ab", "cd", "pq", "zy"]

    for line in lines:
        vowel_count=0
        has_double=False

        if (any(x in line for x in disallow)):
            continue

        for i in range(0, len(line)-1):
            vowel_count += line[i] in vowels
            has_double |= (line[i] == line[i+1])

        # Check final not present in loop
        vowel_count += line[len(line)-1] in vowels

        if (vowel_count >= 3 and has_double):
            res += 1

    return res

def p2(f):
    lines = f.splitlines()
    res = 0

    for line in lines:
        repeat_pair = False
        split_letter = False
        l = len(line)
        found = []
        skipped = False
        previous = ""
        for i in range(0, len(line)-2):
            if line[i] == line[i+2]:
                split_letter = True

            pair = line[i] + line[i+1]
            if previous == pair and not skipped:
                skipped = True
                continue
            skipped = False
            if pair in found:
                repeat_pair = True

            previous = pair
            found.append(pair)
        # Account for the final pair outside of loop.
        pair = line[-2] + line[-1]
        if previous == pair:
            if skipped and pair in found:
                repeat_pair = True
        elif pair in found:
            repeat_pair = True

        if repeat_pair and split_letter:
            res += 1
    return res
