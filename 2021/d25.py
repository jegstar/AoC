with open('d25.txt') as f:
    lines = f.readlines()

data = []
for line in lines:
    data.append(list(line.strip()))


def pretty(matrix):
    for line in matrix:
        for val in line:
            print(val, end=' ')
        print()

pretty(data)