import hashlib

def pad(s, count):
    return s + str(count).rjust(6, '0')

print(pad('a', 2))

count = -1
key = 'ckczppom' 
while True:
    count += 1
    m = hashlib.md5()
    term = key + str(count)
    m.update(term.encode('utf-8'))
    if m.hexdigest()[:6] == '000000':
        break

print(key, count, m.hexdigest())