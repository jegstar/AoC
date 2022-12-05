input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

with open('AoC\d3.txt') as f:
    input = f.read()

# data = [(x[0:len(x)//2], x[len(x)//2:]) for x in input.splitlines()]
data = input.splitlines()

# print(set(data[0][0]))

def score(letter):
    if letter.islower():
        return ord(letter) - 96
    return ord(letter) - 64 + 26

def pt1(data):
    total = 0
    for line in data:
        first = set(line[0])
        second = set(line[1])
        intersection = first.intersection(second).pop()
        total += score(intersection)

    print(total)

def pt2(data):
    total = 0
    for i in range(0,len(data), 3):
        total += score(set(data[i]).intersection(set(data[i+1])).intersection(set(data[i+2])).pop())
    print(total)

pt2(data)