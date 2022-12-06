str1 = ["2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8"]

def main():
    sum1 = 0
    sum2 = 0
    with open ("inputs/input4.txt", "r") as file:
        str = file.read().splitlines()
    for s in str:    
        elve1, elve2 = [x.split("-") for x in s.split(",")]
        sum1 += partOne(elve1,elve2)
        sum2 += partTwo(elve1,elve2)
    print(sum1)
    print(sum2)

def partOne(elve1, elve2):
    if (isFullyIn(elve1, elve2) or isFullyIn(elve2,elve1)):
        return 1
    return 0

def isFullyIn(x, y):
    return int(x[0]) >= int(y[0]) and int(x[1]) <= int(y[1])

def partTwo(elve1, elve2):
    if (isIn(elve1, elve2) or isIn(elve2, elve1)):
        return 1
    return 0

def isIn(x, y):
    return int(x[0]) <= int(y[0]) and int(x[1]) >= int(y[0])


if __name__ == "__main__":
    main()