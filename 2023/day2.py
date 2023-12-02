import re

def main():
  f = open("inputs\input2.txt") 
  
  test1 = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

  #part1(f)
  part2(f)

def part1(input):
  max_cubes = {
      "red": 12, "green": 13, "blue": 14
  }
  possible_games = 0

  for game in input:
    cubes = {
        "red": 0, "green": 0, "blue": 0
    }

    game_id, cube_values = game.split(': ')
    game_id = int(game_id.split(' ')[1])
    cube_values = re.split('; |, ', cube_values)

    for value in cube_values:
      for cube_color in cubes.keys():
        if cube_color in value:
          number = int(value.split(' ')[0])
          if cubes[cube_color] < number:
            cubes[cube_color] = number

    possible = [max_cubes[key] >= cubes[key] for key in cubes]

    if all(possible):
      possible_games += game_id
    
  print(possible_games)
    
def part2(input):
  power_sum = 0

  for game in input:
    cubes = {
        "red": 0, "green": 0, "blue": 0
    }

    game_id, cube_values = game.split(': ')
    game_id = int(game_id.split(' ')[1])
    cube_values = re.split('; |, ', cube_values)

    for value in cube_values:
      for cube_color in cubes.keys():
        if cube_color in value:
          number = int(value.split(' ')[0])
          if cubes[cube_color] < number:
            cubes[cube_color] = number

    power = 1
    for cube_value in cubes.values():
      power *= cube_value

    power_sum += power

  print("Sum: " + str(power_sum))

if __name__ == "__main__":
    main()
