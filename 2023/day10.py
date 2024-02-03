from time import sleep


def main():
    part1()
    # part2()


left = {"L": (-1, 0), "F": (1, 0), "-": (0, -1)}
right = {"-": (0, 1), "J": (-1, 0), "7": (1, 0)}
down = {"|": (1, 0), "L": (0, 1), "J": (0, -1)}
up = {"|": (-1, 0), "F": (0, 1), "7": (0, -1)}

direction = {(1, 0): down, (-1, 0): up, (0, 1): right, (0, -1): left}


def part1():
    input = [list(line) for line in open("inputs/input10.txt", "r").read().splitlines()]
    length = input
    start = next(
        (
            (row_index, col_index)
            for row_index, row in enumerate(input)
            for col_index, column in enumerate(row)
            if column == "S"
        )
    )
    print("Start location at", start)
    pipeA, pipeB = checkStart(input, start)
    checkPipes(pipeA, pipeB, input, 1)


def checkStart(input, start):
    pipes = []
    row, col = start

    if row > 0:
        if input[row - 1][col] in up.keys():
            pipes.append([(row - 1, col), up[input[row - 1][col]]])
    if row < len(input) - 1:
        if input[row + 1][col] in down.keys():
            pipes.append([(row + 1, col), down[input[row + 1][col]]])
    if col > 0:
        if input[row][col - 1] in left.keys():
            pipes.append([(row, col - 1), left[input[row][col - 1]]])
    if col < len(input[row]) - 1:
        if input[row][col + 1] in right.keys():
            pipes.append([(row, col + 1), right[input[row][col + 1]]])

    return pipes[0], pipes[1]


def checkPipes(pipeA, pipeB, input, counter):
    while pipeA[0] != pipeB[0]:
        rowA, colA = [sum(x) for x in zip(pipeA[0], pipeA[1])]
        pipeA = [(rowA, colA), direction[pipeA[1]][input[rowA][colA]]]
        rowB, colB = [sum(x) for x in zip(pipeB[0], pipeB[1])]
        pipeB = [(rowB, colB), direction[pipeB[1]][input[rowB][colB]]]
        counter += 1
    print(counter)


if __name__ == "__main__":
    main()
