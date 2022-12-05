# input = '''A Y
# B X
# C Z'''

with open('d2.txt') as f:
    input = f.read()

data = [x.split() for x in input.split('\n')]

score = 0
for i in range(len(data)):
    a = data[i][0]
    b = data[i][1]
    # if (a == 'A' and b == 'X' ) or (a == 'B' and b == 'Y' ) or (a == 'C' and b == 'Z' ):
    #     score += 3
    # elif (data[i][0] == 'A' and data[i][1] == 'Y') or (data[i][0] == 'B' and data[i][1] == 'Z') or (data[i][0] == 'C' and data[i][1] == 'X'):
    #     score += 6
    # else:
    #     score += 0

    if a == 'A' and b == 'X':
        score += 0 + 3
    
    if a == 'A' and b == 'Y':
        score += 3 + 1
    
    if a == 'A' and b == 'Z':
        score += 6 + 2
    
    if a == 'B' and b == 'X':
        score += 0 + 1
    
    if a == 'B' and b == 'Y':
        score += 3 + 2
    
    if a == 'B' and b == 'Z':
        score += 6 + 3
    
    if a == 'C' and b == 'X':
        score += 0 + 2
    
    if a == 'C' and b == 'Y':
        score += 3 + 3
    
    if a == 'C' and b == 'Z':
        score += 6 + 1
    
    # if b == 'X':
    #     score += 1
    # if b == 'Y':
    #     score += 2
    # if b == 'Z':
    #     score += 3

print(score)

    



