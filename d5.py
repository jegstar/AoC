with open('AoC\d5.txt') as f:
    raw = f.readlines()


ind = raw.index('\n')

start = raw[0:ind]
end = raw[ind+1:]

start.reverse()

keys = start.pop(0).strip().split()

print(keys)


config = dict()

for key in keys:
    config[key] = []

for line in start:
    place = 1
    for i in range(0, len(line), 4):
        if line[i+1] != ' ':
            config[str(place)].append(line[i+1])
        place += 1

print(config)
# Part 1
# def mv(dict, fr, to):
#     dict[to].append(dict[fr].pop())

# def move(dict, num, fr, to):
#     for i in range(int(num)):
#         mv(dict, fr, to)

# Part 2
def move(dict, num, fr, to):
    ind = int(num)
    crates = dict[fr][-ind:]
    dict[fr] = dict[fr][:-ind]
    dict[to] += crates

for line in end:
    l = line.strip().split()
    move(config, l[1], l[3], l[5])

for key  in config.keys():
    print(config[key][-1], end="")