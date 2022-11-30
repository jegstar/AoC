def addDict(letter, dict):
    if letter in dict.keys():
        dict[letter]+= 1
    else:
        dict[letter]=1

def isNice(st):
    # letters = dict()
    pair = False
    vowels = 0
    for i in range(len(st)-1):
        if st[i:i+2] in ['ab','cd', 'pq', 'xy']:
            return False
        if st[i] == st[i+1]:
            pair = True
        if st[i] in 'aeiou':
            vowels += 1
    if st[-1] in 'aeiou':
        vowels += 1

    return vowels >=3 and pair

# tests = ['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb'] 

# for test in tests:
#     print(isNice(test))



def isNice2(st):
    pair = False
    skipped = False
    i = 0
    while i < len(st) - 2 and not pair:
        a = st[i:i+2]
        for j in range(i+2, len(st)-1):
            if st[j:j+2] == a:
                pair = True
                break
        i+= 1

    for i in range(len(st)-2):
        if st[i] == st[i+2]:
            skipped = True
            break

    return skipped and pair

tests =['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy', 'aaa']

# for test in tests:
#     print(isNice2(test))
    
with open ('2015\d5.txt') as f:
    lines = [x.strip() for x in f.readlines()]

count = 0

for line in lines:
    if isNice2(line):
        count += 1

print(count)