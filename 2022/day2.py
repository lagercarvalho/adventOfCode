def main():
    partOne()
    partTwo()

def partOne():
    score = 0
    scoreboard = {
        "X": 1,
        "Y": 2,
        "Z": 3,
        "A Y": 6,
        "A Z": 0,
        "B X": 0,
        "B Z": 6,
        "C X": 6,
        "C Y": 0,
    }
    convert = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }

    str1 = ["A Y\n","B X\n","C Z\n"]
    str = open("inputs/input2.txt")
    for s in str:
        s = s.split('\n')[0:1]
        s1 = s[0].split(' ')
        score += scoreboard[s1[1]]
        if convert[s1[0]] == s1[1]: #draw
            score += 3
        else:
            score += scoreboard[s[0]]
    print(score)

def partTwo():
    score = 0
    scoreboard = {
        'X': 0,
        'Y': 3,
        'Z': 6,
        'A': 1,
        'B': 2,
        'C': 3,
        "A X": 'C',
        "A Z": 'B',
        "B X": 'A',
        "B Z": 'C',
        "C X": 'B',
        "C Z": 'A',
    }

    str1 = ["A Y\n","B X\n","C Z\n"]
    str = open("inputs/input2.txt")
    for s in str:
        s = s.split('\n')[0:1]
        s1 = s[0].split(' ')
        score += scoreboard[s1[1]]
        if s1[1] == 'Y':
            score += scoreboard[s1[0]]
        else:
            score += scoreboard[scoreboard[s[0]]]

    print(score)


if __name__ == "__main__":
    main()
