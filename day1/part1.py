import re

def calibrate(values):
    return int(values[-1]) + 10 * int(values[0])

def main():
    result = 0
    with open("input.txt", "r") as in_file:
        for line in in_file:
            digits = re.findall(r"\d", line)
            result += calibrate(digits)

    print(result)
    return result

if __name__ == '__main__':
    main()