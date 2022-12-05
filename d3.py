input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

with open('AoC\d3.txt') as f:
    input = f.read()

data = [(x[0:len(x)//2], x[len(x)//2:]) for x in input.splitlines()]

# print(set(data[0][0]))

def score(letter):
    if letter.islower():
        return ord(letter) - 96
    return ord(letter) - 64 + 26

total = 0
for line in data:
    first = set(line[0])
    second = set(line[1])
    intersection = first.intersection(second).pop()
    total += score(intersection)

print(total)
