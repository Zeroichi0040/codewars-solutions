# strings have indexes, i used this info to create this solution

def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

if __name__ == "__main__":
    print(are_you_playing_banjo("Rudeus"))      # Rudeus plays banjo
    print(are_you_playing_banjo("Diddy"))       # Diddy does not play banjo