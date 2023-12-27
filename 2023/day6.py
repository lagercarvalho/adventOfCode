import math


def main():
    input = open("inputs/input6.txt", "r").read().splitlines()
    test = open("inputs/test6.txt", "r").read().splitlines()
    part1(input)
    part2(input)


def part1(input):
    times, distances = [list(map(int, line.split(":")[1].split())) for line in input]
    wins = []
    for time, distance in zip(times, distances):
        win = []
        for hold_time in range(time):
            remaining = time - hold_time
            if remaining * hold_time > distance:
                win.append(hold_time)
        wins.append(len(win))
    print("Part1:", math.prod(wins))


def part2(input):
    total_time, record_distance = [
        int("".join(line.split(":")[1].split())) for line in input
    ]
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
