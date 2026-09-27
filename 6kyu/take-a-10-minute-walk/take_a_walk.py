# a 2 dimensional map is represented by variables x and y, which adds or subtracts depending on the direction

def is_valid_walk(walk):
    x = 0
    y = 0
    minutes = 0
    for direction in walk:
        if direction == "n":
            x += 1
        elif direction == "s":
            x -= 1
        elif direction == "w":
            y += 1
        elif direction == "e":
            y -= 1
        minutes += 1
        
    if minutes == 10 and x == 0 and y == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))             # True
    print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))     # False, walk takes too long
    print(is_valid_walk(['w', 's']))                                            # False, walk takes too short