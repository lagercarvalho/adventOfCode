def part1(input):
    total = 0
    for line in input:
        total += isSafe(line)
    print(f"Part1 answer: {total}")
    return 0

def part2(input):
    total = 0
    for line in input:
        total += isMaxUnsafeOnce(line)
    print(f"Part2 answer: {total}")
    return 0

def isSafe(line):
    diff_list = [line[index] - line[index + 1] for index in range(len(line) - 1)]

    if not same_sign(diff_list):
        return 0

    for val in diff_list:
        if abs(val) < 1 or abs(val) > 3:
            return 0
    else:
        return 1
    
def isMaxUnsafeOnce(line):
    if isSafe(line):
        return 1

    for excluded_index in range(len(line)):
        modified_line = line[:excluded_index] + line[excluded_index + 1:]
        if isSafe(modified_line):
            return 1
    else:
        return 0

def same_sign(lst):
    return all(ele > 0 for ele in lst) or all(ele < 0 for ele in lst)

def main():
    input = [[int(ele) for ele in line.split()] for line in open("2024/inputs/input2.txt", "r").readlines()]
    
    part1(input)
    part2(input)
    
if __name__=="__main__":
    main()