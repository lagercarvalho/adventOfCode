def main():
    part1()
    part2()


def part1():
    input = [
        list(map(int, line.split()))
        for line in open("inputs/input9.txt", "r").read().splitlines()
    ]

    extra = 0
    for history in input:
        arr = [history]
        getDiff(arr)
        addRightExtra(arr)
        extra += arr[0][-1]
    print("Part1 sum:", extra)


def getDiff(arr):
    row = []
    for index in range(1, len(arr[-1])):
        row.append(arr[-1][index] - arr[-1][index - 1])
    arr.append(row)
    if not all(x == 0 for x in row):
        getDiff(arr)


def addRightExtra(arr):
    arr[-1].append(0)
    for index in reversed(range(len(arr) - 1)):
        arr[index].append(arr[index][-1] + arr[index + 1][-1])


def part2():
    input = [
        list(map(int, line.split()))
        for line in open("inputs/input9.txt", "r").read().splitlines()
    ]

    extra = 0
    for history in input:
        arr = [history]
        getDiff(arr)
        addLeftExtra(arr)
        extra += arr[0][0]
    print("Part2 sum:", extra)


def addLeftExtra(arr):
    arr[-1] = [0] + arr[-1]
    for index in reversed(range(len(arr) - 1)):
        arr[index] = [arr[index][0] - arr[index + 1][0]] + arr[index]


if __name__ == "__main__":
    main()
