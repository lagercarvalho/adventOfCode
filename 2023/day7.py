def main():
    input = open("inputs/input7.txt", "r").read().splitlines()
    test = open("inputs/test7.txt", "r").read().splitlines()
    part1(input)
    part2(input)


def part1(input):
    types = {
        "high-card": [],
        "1-pair": [],
        "2-pair": [],
        "3-kind": [],
        "full-house": [],
        "4-kind": [],
        "5-kind": [],
    }
    card_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}

    for round in input:
        hand, bid = round.split()
        num_cards = numOfCards(hand)

        if num_cards[0][1] == 5:
            insert((hand, bid), types["5-kind"], card_values)
        elif num_cards[0][1] == 4:
            insert((hand, bid), types["4-kind"], card_values)
        elif num_cards[0][1] == 3:
            if num_cards[1][1] == 2:
                insert((hand, bid), types["full-house"], card_values)
            else:
                insert((hand, bid), types["3-kind"], card_values)
        elif num_cards[0][1] == 2:
            if num_cards[1][1] == 2:
                insert((hand, bid), types["2-pair"], card_values)
            else:
                insert((hand, bid), types["1-pair"], card_values)
        else:
            insert((hand, bid), types["high-card"], card_values)

    hands = sum(types.values(), [])
    winnings = 0
    for index, hand in enumerate(hands):
        winnings += (index + 1) * int(hand[1])

    print("Part1:", winnings)


def numOfCards(hand):
    card_dict = {}
    for card in hand:
        card_dict[card] = card_dict.get(card, 0) + 1
    return sorted(card_dict.items(), key=lambda x: x[1], reverse=True)


def insert(value, array, card_values):
    array.append(value)
    if len(array) > 1:
        for index in range(len(array) - 1):
            if weakerThan(value[0], array[index][0], card_values):
                j = len(array) - 1
                while j > index:
                    array[j] = array[j - 1]
                    j -= 1
                array[index] = value
                break


def weakerThan(hand1, hand2, card_values):
    for card_index in range(len(hand1)):
        card1 = (
            card_values[hand1[card_index]]
            if not hand1[card_index].isdigit()
            else int(hand1[card_index])
        )
        card2 = (
            card_values[hand2[card_index]]
            if not hand2[card_index].isdigit()
            else int(hand2[card_index])
        )
        if card1 < card2:
            return True
        elif card1 > card2:
            return False
    return False


def part2(input):
    types = {
        "high-card": [],
        "1-pair": [],
        "2-pair": [],
        "3-kind": [],
        "full-house": [],
        "4-kind": [],
        "5-kind": [],
    }
    card_values = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}

    for round in input:
        hand, bid = round.split()
        num_cards = numOfCards(hand)
        # print(num_cards)

        jokers = 0
        for card, num in num_cards:
            if card == "J":
                jokers = num
                break

        if num_cards[0][0] != "J":
            most_frequent = num_cards[0][1] + jokers
        elif len(num_cards) == 1:
            most_frequent = num_cards[0][1]
        else:
            most_frequent = num_cards[1][1] + jokers

        if most_frequent == 5:
            insert((hand, bid), types["5-kind"], card_values)
        elif most_frequent == 4:
            insert((hand, bid), types["4-kind"], card_values)
        elif most_frequent == 3:
            if num_cards[1][1] == 2:
                insert((hand, bid), types["full-house"], card_values)
            else:
                insert((hand, bid), types["3-kind"], card_values)
        elif most_frequent == 2:
            if num_cards[1][1] == 2:
                insert((hand, bid), types["2-pair"], card_values)
            else:
                insert((hand, bid), types["1-pair"], card_values)
        else:
            insert((hand, bid), types["high-card"], card_values)

    print(types)

    hands = sum(types.values(), [])
    winnings = 0
    for index, hand in enumerate(hands):
        winnings += (index + 1) * int(hand[1])

    print("Part2:", winnings)


if __name__ == "__main__":
    main()
