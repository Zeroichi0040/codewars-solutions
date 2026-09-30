# counter will hold the number of letters the passed string has
# first check if the length of the passed string can be divided by 2, if so then there are two middle characters
# sides is the varaible that holds the number of letters starting from the first letter to the middle letter/s
# counter is subtracted by 2 since there are 2 middle characters in this case, then divide by 2(split both sides)
# add the specified index of the given string to an empty string, string sliced by the sides converted to integers

def get_middle(s):
    middle = ""
    counter = 0
    if len(s) % 2 == 0:
        for char in s:
            counter += 1
        sides = (counter - 2) / 2   # 4 letters - 2 middle numbers, then divide by 2 to halve it = 1 character from the start to the first middle character
        middle += s[int(sides):int(sides + 2)]  # test, t[0], e[1] so it starts from e. then sides + 2: t[4], since python is weird its actually on the third index
    else:
        for char in s:
            counter += 1
        sides = (counter - 1) / 2   # only subtract one since there is only one middle character
        middle += s[int(sides):int(sides + 1)]
    return middle

if __name__ == "__main__":
    print(get_middle("test"))       # es
    print(get_middle("testing"))    # t