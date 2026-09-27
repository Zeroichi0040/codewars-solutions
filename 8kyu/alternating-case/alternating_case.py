# given a string, loop through each letter, compare if the character is uppercase, if it is convert to lower and add to new empty string
# if its not upper case, convert character to uppercase and add to new empty string. after it finishes looping through the original string return the new string

def to_alternating_case(string):
    alternated = ""
    for char in string:
        if char == char.upper():
            alternated += char.lower()
        else:
            alternated += char.upper()
    return alternated

if __name__ == "__main__":
    print(to_alternating_case("hello world"))   # HELLO WORLD
    print(to_alternating_case("AbCd"))          # aBcD