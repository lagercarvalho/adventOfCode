
def main():
  f = open("inputs\input2.txt") 
  test1 = ["467..114..","...*......","..35..633.","......#...","617*......",".....+.58.","..592.....","......755.","...$.*....",".664.598.."]

  part1(test1)

def part1(input):
  matrix_input = [[char for char in line] for line in input]

  for 
        

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