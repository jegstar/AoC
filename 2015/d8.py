import regex as re

with open('2015\d8.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    print(lines)


literals = 0
memory = 0
for line in lines:
    print(line)
    literals += len(line)
    line = line[1:-1]
    line = re.sub('\\\\x..','a',line)
    line = line.replace('\\"', '"')
    line = line.replace('\\\\', '\\')
    memory += len(line)
    print(line)
    print()

print(literals - memory)