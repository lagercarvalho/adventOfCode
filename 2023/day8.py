import math
import re


def main():
    part1()
    part2()


def part1():
    directions, *instructions = open("inputs/input8.txt", "r").read().splitlines()
    del instructions[0]

    desert_map = {
        source: (left, right)
        for instruction in instructions
        for source, left, right in [re.findall(r"[a-zA-Z]+", instruction)]
    }
    direction_map = {"L": 0, "R": 1}

    current_position = "AAA"
    steps = 0

    while current_position != "ZZZ":
        direction = direction_map[directions[steps % len(directions)]]
        current_position = desert_map[current_position][direction]
        steps += 1

    print("Part1 steps:", steps)


def part2():
    directions, *instructions = open("inputs/input8.txt", "r").read().splitlines()
    del instructions[0]

    desert_map = {
        source: (left, right)
        for instruction in instructions
        for source, left, right in [re.findall(r"[1-9a-zA-Z]+", instruction)]
    }
    direction_map = {"L": 0, "R": 1}

    current_position = [node for node in desert_map.keys() if node[-1] == "A"]
    steps = [0 for node in current_position]

    for index in range(len(current_position)):
        while current_position[index][-1] != "Z":
            direction = direction_map[directions[steps[index] % len(directions)]]
            current_position[index] = desert_map[current_position[index]][direction]
            steps[index] += 1

    print("Part2 steps:", math.lcm(*steps))


if __name__ == "__main__":
    main()
