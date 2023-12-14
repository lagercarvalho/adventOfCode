def main():
  with open ("inputs/input5.txt", "r") as file:
    input = file.read().splitlines()

  with open ("inputs/test5.txt", "r") as file:
    test = file.read().splitlines()
  
  part1(input) #510109797
  part2(input) #9622622

def createMaps(input):
  maps = {'seed':[], 'soil':[], 'fertilizer':[], 'water':[], 'light':[], 'temperature':[], 'humidity':[], 'location':[]}
  maps['seed'] = list(map(int, input[0].split(':')[-1].split()))
  index = 3
  
  for mapping in maps.keys():
    if mapping == 'seed': continue
    while (index < len(input) and input[index] != ''):
      maps[mapping] += [[int(x) for x in input[index].split()]]
      index += 1
    index += 2

  return maps

def getConversion(maps, map, value):
  for map_values in maps[map]:
    value_diff = value - map_values[1]
    if 0 <= value_diff < map_values[2]:
      return map_values[0] + value_diff
  return value

def mapSeedtoLocation(maps):
  location_values = []
  last_value = 0
  for seed in maps['seed']:
    last_value = seed
    for map in maps.keys():
      if map != 'seed':
        last_value = getConversion(maps, map, last_value)
    location_values += [last_value]
  return location_values

def part1(input):
  maps = createMaps(input)
  location_values = mapSeedtoLocation(maps)
  print("Part1 Min Location:",min(location_values))

def extractMaxSeedRange(seeds):
  max_seed = 0
  for seed_index in range(0,len(seeds),2):
    if seeds[seed_index] + seeds[seed_index+1] - 1 > max_seed:
      max_seed = seeds[seed_index] + seeds[seed_index+1] - 1
  return(max_seed)

def mapLocationToSeed(maps, location):
  last_value = location
  for map in reversed(maps.keys()):
    if map != 'seed':
      last_value = getReverseConversion(maps, map, last_value)
  return last_value

def getReverseConversion(maps, map, value):
  for map_values in maps[map]:
    value_diff = value - map_values[0]
    if 0 <= value_diff < map_values[2]:
      return map_values[1] + value_diff
  return value

def inRange(seed_ranges, seed_value):
  for seed_index in range(0,len(seed_ranges),2):
    if seed_ranges[seed_index] < seed_value < seed_ranges[seed_index] + seed_ranges[seed_index+1]:
      return True
  return False

def part2(input):
  maps = createMaps(input)
  max_location = extractMaxSeedRange(maps['seed'])
  final_location = 0
  for location in range(0,max_location+1):
    seed = mapLocationToSeed(maps,location)
    if inRange(maps['seed'], seed):
      final_location = location
      break
  print("Part2 Min location:",final_location)
    

if __name__ == "__main__":
    main()