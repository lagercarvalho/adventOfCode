letters = {'X':'M', 'M':'A', 'A':'S'}

'''

def part1(input):
    total = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == 'X':
                total += isXMAS(input, x, y)
                print("Next X, Total:", total)
    print(total)

def isXMAS(input, x, y):
    print(y, x, input[y][x])
    if input[y][x] == 'S':
        return 1
    
    total = 0
    
    for y_add in range(-1, 2):
        if (y_add==-1 and y==0) or (y_add==1 and y==len(input) - 1):
            continue

        for x_add in range(-1, 2):
            if (x_add==-1 and x==0) or (x_add==1 and x==len(input[y]) - 1) or (x_add==0 and y_add==0):
                continue
            value = input[y + y_add] [x + x_add]
            target = letters[input[y][x]]
            print(y + y_add, x + x_add, value, target)
            if value == target:
                total += isXMAS(input, x + x_add, y + y_add)
                print("Total", total)
                print(y, x, input[y][x])

    return total

'''

def part1(input):
    total = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == 'X':
                print("X at",y,x,"Total:",total)
                total += checkAllDir(input, x, y)
                
    print(total)

def checkAllDir(input, x, y):
    total = 0
    for y_add in range(-1, 2):
        new_y = y + y_add
        if (new_y < 0) or (new_y >= len(input)):
            continue

        for x_add in range(-1, 2):
            new_x = x + x_add
            if (new_x < 0) or (new_x >= len(input[y])):
                continue
            total += isXMAS(input, x, y, x_add, y_add)

    return total

def isXMAS(input, x, y, x_add, y_add):
    new_x = x + x_add
    new_y = y + y_add

    if (new_y < 0) or (new_y >= len(input)) or (new_x < 0) or (new_x >= len(input[new_y])):
        return 0

    next_letter = input[new_y][new_x]
    target_letter = letters[input[y][x]]

    print(y, x, input[y][x],"Next:",next_letter,"Target:", target_letter)

    if next_letter == target_letter:
        if next_letter == 'S':
            return 1
        else:
            return isXMAS(input, new_x, new_y, x_add, y_add)
    else:
        return 0

def main():
    input = [list(line)[:-1] for line in open("2024/inputs/test.txt", "r").readlines()]

    print(input)
    
    part1(input)
    #part2(input)
    
if __name__=="__main__":
    main()
