import re

input = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

with open('AoC/d4.txt') as f:
    input = f.read()

total = 0
pairs = 0
p2 = 0
lines = input.splitlines()
for line in lines:
    l = re.split(r'[,-]', line)
    l = [int(x) for x in l]
    t = total
    if l[0] <= l[2] and l[1] >= l[3]:
        total += 1
    if l[0] >= l[2] and l[1] <= l[3]:
        total += 1
    if l[0] == l[2] and l[1] == l[3]:
        pairs += 1
    
    if l[1] < l[2] or l[3] < l[0]:
        print(l)
        p2 += 1
print(total, pairs, total - pairs)
print(len(lines)-p2)