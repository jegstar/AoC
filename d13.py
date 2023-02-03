def lt(left, right, lp=0, rp=0):
    if left == right:
        return False
    if left == []:
        return True
    if right == []:
        return False
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        else:
            return False

        
    
    if type(left) == int:
        return lt([left], right)
    
    if type(right) == int:
        return lt(left, [right])

    return lt(left[0], right[0]) and lt(left[1:], right[1:])

test = '''[1,1,3,1,1]
[1,1,5,1,1]'''

tests= test.splitlines()
left = eval(tests[0])
right = eval(tests[1])
print(lt(left, right))

