import math


def main():
    input = open("inputs/input6.txt", "r").read().splitlines()
    test = open("inputs/test6.txt", "r").read().splitlines()
    part1(input)
    part2(input)


def part1(input):
    times = list(map(int, input[0].split(":")[1].split()))
    distances = list(map(int, input[1].split(":")[1].split()))
    wins = []
    for index in range(len(times)):
        win = []
        for hold_time in range(times[index]):
            remaining = times[index] - hold_time
            distance = remaining * hold_time
            if distance > distances[index]:
                win.append(hold_time)
        wins.append(len(win))
    print("Part1:", math.prod(wins))


def part2(input):
    total_time = int("".join(input[0].split(":")[1].split()))
    record_distance = int("".join(input[1].split(":")[1].split()))
    first_match = 0
    for hold_time in range(1, total_time // 2 + total_time % 2):
        remaining = total_time - hold_time
        distance = remaining * hold_time
        if distance > record_distance:
            first_match = hold_time
            break

    win_count = (total_time // 2 - first_match) * 2 + 1 + total_time % 2
    print("Part2:", win_count)


if __name__ == "__main__":
    main()
