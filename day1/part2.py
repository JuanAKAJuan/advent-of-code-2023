# Solution source: https://www.tinkerassist.com/blog/advent-of-code-2023-day-1-trebuchet

sum = 0
digit_names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

file = open("input.txt", "r")
input_data = file.read()
input_list = input_data.split('\n')

for input in input_list:
    numbers = []
    for index_of_letter, letter in enumerate(input):
        for index_of_name, name in enumerate(digit_names):
            if name in input[index_of_letter:index_of_letter+len(name)]:
                numbers.append(str(index_of_name))
        
        if ord(letter) <= 57:
            numbers.append(letter)

    sum += int(numbers[0] + numbers[-1])