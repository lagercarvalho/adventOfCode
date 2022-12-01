def main():
    max = [0,0,0]
    sum = 0
    f = open("inputs/input1.txt")
    for x in f:
        if x == '\n':
            if sum > max[0] or sum > max[1] or sum > max[2]:
                addSum(sum, max)
            sum = 0
        else:
            sum += int(x)
    print(max[0]+max[1]+max[2])
    

def addSum(sum, max):
    minIndex = 0
    min = max[0]
    for x in range(3):
        if max[x] <= min:
            min = max[x]
            minIndex = x
    max[minIndex] = sum

if __name__ == "__main__":
    main()