# part 2
with open('2015\d1.txt') as f:
    text = f.read().strip()

pos = 1
floor = 0
for letter in text:
    print(letter)
    if letter == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(pos)
        break
    pos += 1