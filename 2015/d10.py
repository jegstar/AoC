nums = '3113322113'

def generate(s):
    pointer = 0
    index = 0
    output = ''
    while pointer < len(s):
        if s[pointer] != s[index]:
            output += str(pointer-index) + str(s[index])
            index = pointer
        pointer += 1
    
    output += str(pointer-index) + str(s[index])
    return output

for i in range(50):
    nums = generate(nums)
print(len(nums))
