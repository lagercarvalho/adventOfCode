import string

str1 = ["vJrwpWtwJgWrhcsFMMfFFhFp\n",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n",
            "PmmdzqPrVvPwwTWBwg\n",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n",
            "ttgJtRGJQctTZtZT\n",
            "CrZsJsPPZsGzwwsLwLmpwMDw\n"]

def main():
    str = open("inputs/input3.txt")
    letters = dict(zip(string.ascii_letters, range(1, len(string.ascii_letters) + 1)))
    partOne(str, letters)
    partTwo(str, letters)

def partOne(str, letters):
    sum = 0
    for s in str:
        length = len(s)
        s1 = slice(0,length//2)
        s2 = slice(length//2, length)
        common = findCommonTwo(s[s1], s[s2])
        sum += letters[common]
    print(sum)

def findCommonTwo(s1, s2):
    for x in s1:
        for y in s2:
            if x == y:
                return x

def partTwo(str, letters):
    sum = 0
    ls = []
    for index, s in enumerate(str):
        ls.append(s)
        if index % 3 == 2:
            common = findCommonThree(ls)
            sum += letters[common]
            ls = []
        else:
            ls.append(s)
    print(sum)


def findCommonThree(ls):
    for x in ls[0]:
        for y in ls[1]:
            for z in ls[2]:
                if x == y and y == z:
                    print(x)
                    return x

if __name__ == "__main__":
    main()
