def main():
  #seeds, *blocks = open("inputs/test5.txt", "r").read().split("\n\n")
  seeds, *blocks = open("inputs/input5.txt", "r").read().split("\n\n")
  seeds = list(map(int, seeds.split(':')[1].split()))

  part1(seeds,blocks)
  part2(seeds, blocks)

def part1(seeds, blocks):
  for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
      ranges.append(list(map(int,line.split())))
    new = []
    for x in seeds:
      for a,b,c in ranges:
        if b <= x < b + c:
          new.append(x - b + a)
          break
      else:
        new.append(x)
    seeds = new

  print("Part1:",min(seeds))

def part2(inputs, blocks):
  seeds = []

  for i in range(0,len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i+1]))

  for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
      ranges.append(list(map(int,line.split())))
    new = []
    while len(seeds) > 0:
      s, e = seeds.pop()
      for a,b,c in ranges:
        overlap_start = max(s, b)
        overlap_end = min(e, b + c)
        if overlap_start < overlap_end:
          new.append((overlap_start - b + a, overlap_end - b + a))
          if overlap_start > s:
            seeds.append((s,overlap_start))
          if e > overlap_end:
            seeds.append((overlap_end, e))
          break
      else:
        new.append((s,e))
    seeds = new
  print(min(seeds))

if __name__ == "__main__":
  main()