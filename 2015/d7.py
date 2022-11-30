line = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i'''

lines = line.split('\n')

for line in lines:
    line = line.split(' -> ')
    print(line)
    