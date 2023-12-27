with open("day3/input.txt", "r") as file:
    data = file.read()
    lines = data.strip().split('\n')

n = len(lines)
m = len(lines[0])

grid = [[[] for _ in range(m)] for _ in range(n)] # A list, inside of a list, inside of a list

def is_symbol(rows, columns, num):
    if not (0 <= rows < n and 0 <= columns < m):
        return False
    
    # If a gear is adjacent to the found number, store the number in the grid
    if lines[rows][columns] == "*":
        grid[rows][columns].append(num) # The numbers will be stored in the same location in the grid
                                        # if coordinates of the gear they are adjacent to is the same.

    return lines[rows][columns] != "." and not lines[rows][columns].isdigit()

answer = 0

for i, line in enumerate(lines):
    start = 0

    j = 0

    # Look for a number and store it temporarily
    while j < m:
        start = j
        number = ""
        while j < m and line[j].isdigit():
            number+= line[j]
            j += 1

        if number == "":
            j += 1
            continue

        number = int(number)

        # Number has been identified, look to left and right of it for a gear.
        is_symbol(i, start - 1, number) or is_symbol(i, j, number)

        # Check above and below the number for a gear
        for k in range(start - 1, j + 1):
            is_symbol(i - 1, k, number) or is_symbol(i + 1, k, number)

for i in range(n):
    for j in range(m):
        numbers = grid[i][j]
        if lines[i][j] == "*" and len(numbers) == 2: # If there are two numbers in the list, then
                                                     # both of those numbers have to be adjacent 
                                                     # to a gear.
            print(numbers)
            answer += numbers[0] * numbers[1]

print(answer)

