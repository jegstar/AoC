with open('2015\d2.txt') as f:
    data = [[int(x) for x in line.split('x')] for line in f.readlines()]


total = 0
for line in data:
    wl = line[0]*line[1]
    lh = line[1]*line[2]
    wh = line[0]*line[2]

    # part 1
    # total += 2 * (wl+lh+wh) + min(wl, lh, wh)

    # part 2
    wrap = (sum(line) - max(line)) * 2
    bow = line[0] * line[1] * line[2]
    total += wrap + bow

print(total)