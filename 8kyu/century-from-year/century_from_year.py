# i am sure there is a simpler way to do this, but this is what i came up with instead
# we check if the year is less than increment, and if it is return century, else increment the variable increment by 100 and century by 1

def century(year):
    century = 1
    increment = 101
    while True:
        if year < increment:
            return century
        else:
            increment += 100
            century += 1
        
if __name__ == "__main__":
    print(century(50))      # 1
    print(century(2742))    # 28
