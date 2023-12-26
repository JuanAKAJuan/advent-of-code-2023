import re

MAX_RED_CUBES = 12 
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14
game_id = 0
game_id_sum = 0
file = open("day2/input.txt", "r")
game_id_regex = "(\\d+(?=:))"
sets_regex = "(?<=:)(.*)"
red_cubes_regex = "(\\d+)(?=\\sred)"
green_cubes_regex = "(\\d+)(?=\\sgreen)"
blue_cubes_regex = "(\\d+)(?=\\sblue)"


for line in file:
    valid = True
    game_id = int(re.search(game_id_regex, line).group(0))
    sets = re.search(sets_regex, line).group(0)
    sets = re.split(";", sets)

    for set in sets:
        current_red_cube = re.search(red_cubes_regex, set)
        if current_red_cube:
            current_red_cube = int(current_red_cube.group(0))
            if current_red_cube > MAX_RED_CUBES:
                valid = False

        current_green_cube = re.search(green_cubes_regex, set)
        if current_green_cube:
            current_green_cube = int(current_green_cube.group(0))
            if current_green_cube > MAX_GREEN_CUBES:
                valid = False

        current_blue_cube = re.search(blue_cubes_regex, set)
        if current_blue_cube:
            current_blue_cube = int(current_blue_cube.group(0))
            if current_blue_cube > MAX_BLUE_CUBES:
                valid = False
    
    if valid:
        game_id_sum += game_id
        print(game_id)

print (game_id_sum)
file.close()
