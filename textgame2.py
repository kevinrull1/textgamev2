char_location = [1,2]

while True:
    print(char_location)
    move = ""
    while move not in ["n", "e", "s", "w"]:
        move = input("n/e/s/w")
        if move == "n" and char_location[0] != 0:
            char_location[0] -= 1
        elif move == "s" and char_location[0] != 3:
            char_location[0] += 1
        elif move == "w" and char_location[1] != 0:
            char_location[0] -= 1
        elif move == "e" and char_location[1] != 3:
            char_location[0] += 1 