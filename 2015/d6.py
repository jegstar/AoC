import numpy

lights = numpy.zeros((1000,1000))

# def setOn(x1,y1,x2,y2, arr):
#     arr[x1:x2+1, y1:y2+1] = numpy.ones((x2-x1+1, y2-y1+1),dtype=bool)

# def setOff(x1,y1,x2,y2, arr):
#     arr[x1:x2+1, y1:y2+1] = numpy.zeros((x2-x1+1, y2-y1+1),dtype=bool)

# def toggle(x1,y1,x2,y2, arr):
#     arr[x1:x2+1, y1:y2+1] = ~ arr[x1:x2+1, y1:y2+1]

def parseInput(s):
    c = 'turn on '
    command = ''
    if s[:len(c)] == c:
        command = 'on'
        s = s[len(c):]
    c = 'turn off '
    if s[:len(c)] == c:
        command = 'off'
        s = s[len(c):]

    c = 'toggle '
    if s[:len(c)] == c:
        command = 'tog'
        s = s[len(c):]
    
    output = [command]
    s = s.split(' through ')
    
    output += [int(x) for x in s[0].split(',')]
    output += [int(x) for x in s[1].split(',')]
    return output
    
with open('2015\d6.txt') as f:
    lines = [x.strip() for x in f.readlines()]

# lines = ['turn on 0,0 through 0,0', 'toggle 0,0 through 999,999']

# for line in lines:
#     command, x1, y1, x2, y2 = parseInput(line) 
#     print(parseInput(line))
#     if command == 'on':
#         setOn(x1, y1, x2, y2, lights)
#     if command == 'off':
#         setOff(x1, y1, x2, y2, lights)
#     if command == 'tog':
#         toggle(x1, y1, x2, y2, lights)

for line in lines:
    command, x1, y1, x2, y2 = parseInput(line) 
    multiplier = 1
    if command == 'off':
        multiplier = -1
    if command == 'tog':
        multiplier = 2

    lights[x1:x2+1,y1:y2+1] += numpy.ones((x2-x1+1,y2-y1+1)) * multiplier
    lights = lights.clip(min=0)

    print(numpy.sum(lights))


