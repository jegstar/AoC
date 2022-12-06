with open('AoC/d6.txt') as f:
    data = f.read().strip()

def findMarker(text, length):
    i = length
    while len(set(text[i-length:i])) != length and i < len(text):
        print()
        i += 1
    return i

# for line in data:
print(findMarker(data, 4))

        