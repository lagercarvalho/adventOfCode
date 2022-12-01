max = 0
sum = 0
f = open("inputs/input1.txt")
for x in f:
    if x == '\n':
        if sum > max:
            max = sum
        sum = 0
    else:
        sum += int(x)
print(max)