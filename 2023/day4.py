def main():
  with open ("inputs/input4.txt", "r") as file:
    input = file.read().splitlines()
  test1 = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 
           "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", 
           "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", 
           "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", 
           "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", 
           "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

  part1(input)
  part2(input)

def part1(input):
  point_sum = 0
  for card in input:
    points = 0
    card_num, win_nums, owned_nums = splitCard(card)
    for number in owned_nums:
      if number in win_nums:
          if points == 0:
            points += 1
          else:
            points *= 2
    point_sum += points
  print("Part1 Sum:", point_sum)

def splitCard(line):
  card_split = line.split(':')
  card_num = int(card_split[0].split()[-1])
  numbers = card_split[-1].split('|')
  return (card_num, numbers[0].split(), numbers[1].split())
  
def part2(input):
  cards = dict((index,1) for index in range(1, len(input) + 1))
  
  for card in input:
    card_num, win_nums, owned_nums = splitCard(card)
    wins = numOfWins(win_nums, owned_nums)
    instances = cards[card_num]
    for index in range(card_num + 1, card_num + wins + 1):
      cards[index] += instances 
  
  sum = 0
  for instances in cards.values():
    sum += instances
  print("Part2 Sum:", sum)

def numOfWins(win_nums, owned_nums):
  wins = 0
  for number in owned_nums:
    if number in win_nums:
      wins += 1
  return wins



if __name__ == "__main__":
    main()