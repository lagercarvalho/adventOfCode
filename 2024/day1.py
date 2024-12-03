def part1(left, right):
    left = sorted(left)
    right = sorted(right)
    
    sum = 0
    for index, value in enumerate(left):
        sum += abs(int(value) - int(right[index]))
        
    print(f"Part 1: SUM = {sum}")
    return 0
    
def part2(left, right):
    right_dict = {}
    for value in right:
        right_dict[value] = right_dict.get(value, 0) + 1
        
    sum = 0
    for value in left:
        sum += int(value) * right_dict.get(value,0)
    
    print(f"Part 2: SUM = {sum}")
    return 0
    
def main():
    input = [(parts[0], parts[-1]) for line in open("2024/inputs/input1.txt", "r").readlines() if (parts := line.split())]
    left, right = zip(*input)
    left = list(left)
    right = list(right)
    
    part1(left, right)
    part2(left, right)
    
if __name__=="__main__":
    main()