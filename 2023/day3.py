
def main():
  with open ("inputs/input3.txt", "r") as file:
        input = file.read().splitlines()
  test1 = ["467..114..","...*......","..35..633.","......#...","617*......",".....+.58.","..592.....","......755.","...$.*....",".664.598.."]

  #part1(input) #512794
  part2(input)

def part1(input):
  sum = 0

  for line_index, line in enumerate(input):
    number = []
    index_start = -1
    for char_index, char in enumerate(line):
      if char.isdigit():
        number.append(str(char))
        if index_start == -1:
          index_start = char_index

      if (char_index == len(line) - 1 or not char.isdigit()) and index_start != -1: 
        num = ''.join(digit for digit in number)
        
        if isPartsNum(input, line_index, index_start, char_index - 1):
          sum += int(num)
        
        index_start = -1
        number.clear()
  print('Part1 Sum:', sum)
      

def isPartsNum(input, line_index, index_start, index_end):
  for col in range(index_start - 1, index_end + 2):
    if col < 0 or col >= len(input[line_index]): continue
    for row in range(line_index - 1, line_index + 2):
      if row < 0 or row >= len(input): continue
      if not input[row][col].isdigit() and  input[row][col] != '.':
        return True
  return False


def part2(input):
  part_sum = 0
  for line_index, line in enumerate(input):
    for char_index, char in enumerate(line):
      if char == '*':
        numbers = getSurroundNums(input, line_index, char_index)
        if len(numbers) == 2:
          print(numbers)
          part_sum += numbers[0] * numbers [1]
  print("Part2 Sum:", part_sum)


def getSurroundNums(input, line_index, char_index):
  numbers = []
  lastNum = -1
  for row in range(line_index - 1, line_index + 2):
    if row < 0 or row >= len(input): continue
    for col in range(char_index - 1, char_index + 2):
      if col < 0 or col >= len(input[line_index]): continue
      if input[row][col].isdigit() and lastNum == -1:
        numbers.append(getNum(input,row,col))
        lastNum = col
      elif not input[row][col].isdigit():
        lastNum = -1
    lastNum = -1
  return numbers

def getNum(input, row, col):
  num = []
  num.append(input[row][col])
  num = getDigits(input, row, col, -1) + num
  num = num + getDigits(input, row, col, 1)
  return(int(''.join(num)))

def getDigits(input, row, col, step):
  num = []
  col = col + step
  if col < 0 or col >= len(input[row]): 
    return []
  elif input[row][col].isdigit():
    num.append(input[row][col])
    if step == -1:
      num = getDigits(input, row, col, -1) + num
    else:
      num = num + getDigits(input, row, col, 1)
  return num

  
        

if __name__ == "__main__":
    main()

'''
  for row_index in range(matrix_input):
    findPartNums(matrix_input, row_index, 0)
      
def findPartNums(matrix, row_index, col_index):
  if row_index < 0 or col_index < 0 or row_index >= len(matrix) or col_index >= len(matrix[row_index]):
    return []
  if matrix[row_index][col_index] != '.' or not matrix[row_index][col_index].isdigit():
'''