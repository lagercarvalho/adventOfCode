ls = []
sum = 0
f = open("inputs/input1.txt")
for x in f:
    if x == '\n':
        ls.append(sum)
        sum = 0
    else:
        sum += int(x)
ls = sorted(ls)

print(ls[-1])
print(ls[-1]+ls[-2]+ls[-3])
