import re

game_id = 0
file = open("day2/input.txt", "r")
game_id_regex = "(\\d+(?=:))"
sets_regex = "(?<=:)(.*)"
red_cubes_regex = "(\\d+)(?=\\sred)"
green_cubes_regex = "(\\d+)(?=\\sgreen)"
blue_cubes_regex = "(\\d+)(?=\\sblue)"
sum_of_powers = 0


for line in file:
    game_id = int(re.search(game_id_regex, line).group(0))
    sets = re.search(sets_regex, line).group(0)
    sets = re.split(";", sets)
    biggest_red_cube = 0
    biggest_green_cube = 0
    biggest_blue_cube = 0
    power_of_cubes = 0

    for set in sets:
        current_red_cube = re.search(red_cubes_regex, set)
        if current_red_cube:
            current_red_cube = int(current_red_cube.group(0))
            if current_red_cube > biggest_red_cube:
                biggest_red_cube = current_red_cube

        current_green_cube = re.search(green_cubes_regex, set)
        if current_green_cube:
            current_green_cube = int(current_green_cube.group(0))
            if current_green_cube > biggest_green_cube:
                biggest_green_cube = current_green_cube

        current_blue_cube = re.search(blue_cubes_regex, set)
        if current_blue_cube:
            current_blue_cube = int(current_blue_cube.group(0))
            if current_blue_cube > biggest_blue_cube:
                biggest_blue_cube = current_blue_cube

    power_of_cubes = biggest_red_cube * biggest_green_cube * biggest_blue_cube
    sum_of_powers += power_of_cubes

print(sum_of_powers)
file.close()
