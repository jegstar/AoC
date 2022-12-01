with open("d1.txt") as f:
    data = [x.strip() for x in f.readlines()]

cal_list = []
cals = 0

for item in data:
    if item == "":
        cal_list.append(cals)
        cals = 0
    else:
        cals += int(item)

print(max(cal_list))

total = 0
for i in range(3):
    total += max(cal_list)
    cal_list.remove(max(cal_list))

print(total)