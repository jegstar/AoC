input = '''A Y
B X
C Z'''


data = [x.split() for x in input.split('\n')]

score = 0
for i in range(len(data)):
    if ord(data[i][0]) == ord(data[i][1])-24:
        score += 3
    elif (data[i][0] == 'A' and data[i][1] == 'Y') or (data[i][0] == 'B' and data[i][1] == 'Z') or (data[i][0] == 'C' and data[i][1] == 'X'):
        score += 0
    else:
        score += 6
    
    let = data[i][0]

    score += ord(let)-64

    
    print(score)



