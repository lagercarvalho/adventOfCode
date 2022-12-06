import re

str1 = [
"    [D]    ",
"[N] [C]    ",
"[Z] [M] [P]",
" 1   2   3 ",
"",
"move 1 from 2 to 1",
"move 3 from 1 to 3",
"move 2 from 2 to 1",
"move 1 from 1 to 2"
]

def main():
    with open ("inputs/input5.txt", "r") as file:
        str = file.read().splitlines()
    print("Part 1:")
    partOne(str)
    print("Part 2:")
    partTwo(str)

def partOne(str):
    stack = [[] for _ in range(9)]
    for s in str:
        if len(s) == 0:
            for x in range(len(stack)):
                stack[x].reverse()
            continue
        elif len(s) == 35:
            l = [s[i * 4:(i + 1) * 4] for i in range((len(s) + 4 - 1) // 4 )]
            for index, x in enumerate(l):
                if x[0] == '[' :
                    stack[index].append(x[1])
        else:
            num, send, rec = [int(l) for l in s.split() if l.isdigit()] 
            for x in range(num):
                if len(stack[send-1]) != 0:
                    item = stack[send-1].pop()
                    stack[rec-1].append(item)
    for s in stack:
        print(s.pop())

def partTwo(str):
    stack = [[] for _ in range(9)]
    for s in str:
        if len(s) == 0:
            for x in range(len(stack)):
                stack[x].reverse()
            continue
        elif len(s) == 35:
            l = [s[i * 4:(i + 1) * 4] for i in range((len(s) + 4 - 1) // 4 )]
            for index, x in enumerate(l):
                if x[0] == '[' :
                    stack[index].append(x[1])
        else:
            num, send, rec = [int(l) for l in s.split() if l.isdigit()]
            crates = []
            for x in range(num):
                if len(stack[send-1]) != 0:
                    crates.append(stack[send-1].pop())
            crates.reverse()
            for crate in crates:
                stack[rec-1].append(crate)


    for s in stack:
        print(s.pop())

if __name__ == "__main__":
    main()