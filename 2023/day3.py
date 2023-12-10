
def main():
  with open ("inputs/input3.txt", "r") as file:
        input = file.read().splitlines()
  test1 = ["467..114..","...*......","..35..633.","......#...","617*......",".....+.58.","..592.....","......755.","...$.*....",".664.598.."]

  part1(input)

def part1(input):
  matrix_input = [[char for char in line] for line in input]
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
        
        if isPartsNum(matrix_input, line_index, index_start, char_index - 1):
          sum += int(num)
        
        index_start = -1
        number.clear()
  print('Sum:', sum)
      

def isPartsNum(matrix, line_index, index_start, index_end):
  for col in range(index_start - 1, index_end + 2):
    if col < 0 or col >= len(matrix[line_index]): continue
    for row in range(line_index - 1, line_index + 2):
      if row < 0 or row >= len(matrix): continue
      if not matrix[row][col].isdigit() and  matrix[row][col] != '.':
        return True
  return False

        

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