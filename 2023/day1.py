


def main():
  f = open("inputs\input1.txt") 
  test = ["1abc2","pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
  test2 = ["two1nine","eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
  
  #part1(f)
  part2(f)

def part1(input):
  number = []
  result = []

  for string in input:
    for char in string:
      if char.isnumeric():
        number.append(char)
    result.append(int(number[0] + number[-1]))
    number.clear()
  print(sum(result))

def part2(input):
  number_list = []
  result_list = []

  number_conversion = {
    "one": "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"
  }

  for string in input:
    string = replace(list(string), number_conversion)

    for char in string:
      if char.isnumeric():
        number_list.append(char)
    
    result_list.append(int(number_list[0] + number_list[-1]))
    number_list.clear()
  print(sum(result_list))
  

def replace(string, number_conversion):
  for index, char in enumerate(string):
    st = "".join(string)
    for word, value in number_conversion.items():
      if st.find(word) == index:
        string[index] = value
        break
  return string


if __name__ == "__main__":
  main()
  
