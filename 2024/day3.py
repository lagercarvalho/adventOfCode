import re

def part1(input):
    total = 0
    for line in input:
        matches = [int(val1) * int(val2) for (val1, val2) in re.findall(r"mul\(([\d]+),([\d]+)\)", line)]
        total += sum(matches)
    
    print(f"Part1 answer: {total}")
    return 0

def part2(input):
    total = 0
    enabled_beginning = True
    for line in input:      
        line_split = line.split("don't()")
        final_string = ""

        for index, value in enumerate(line_split):
            if index == 0 and enabled_beginning:
                final_string += value
                continue

            if "do()" in value:
                final_string += value.split("do()", 1)[1]

        enabled_beginning = "do()" in line_split[-1]

        matches = [int(val1) * int(val2) for (val1, val2) in re.findall(r"mul\(([\d]+),([\d]+)\)", final_string)]
        total += sum(matches)
    
    print(f"Part2 answer: {total}")
    return 0

def main():
    input = [line for line in open("2024/inputs/input3.txt", "r").readlines()]
    
    part1(input)
    part2(input)
    
if __name__=="__main__":
    main()