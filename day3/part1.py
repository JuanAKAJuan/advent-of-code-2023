with open("day3/input.txt", "r") as file:
    data = file.read()
    lines = data.strip().split('\n')

n = len(lines)
m = len(lines[0])

def is_symbol(rows, columns):
    if not (0 <= rows < n and 0 <= columns < m):
        return False

    return lines[rows][columns] != "." and not lines[rows][columns].isdigit()

answer = 0

for i, line in enumerate(lines):
    start = 0

    j = 0

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

        # Number has been identified, look to left and right of it for a symbol
        if is_symbol(i, start - 1) or is_symbol(i, j):
            answer += number
            continue

        # Check above and below the number for a symbol
        for k in range(start - 1, j + 1):
            if is_symbol(i - 1, k) or is_symbol(i + 1, k):
                answer += number
                break

print(answer)
