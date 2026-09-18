# takes in base and factor variables, to check if the base is a factor of the factor variable,
# take base and use the mod % operator with factor, if the result is 0 that means it is a factor.

def check_for_factor(base, factor):
    if base % factor == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(check_for_factor(10, 2))      # True
    print(check_for_factor(64, 7))      # False
