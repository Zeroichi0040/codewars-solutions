# initialize minimum and maximum value by the first index of the array, not hardcoded to 0
# loop through the integers in the array and update both variables accordingly

def min_max(lst):
    min_value = lst[0]
    max_value = lst[0]
    for i in lst:
        if i > max_value:
            max_value = i
        elif i < min_value:
            min_value = i
    return [min_value, max_value]

if __name__ == "__main__":
    print(min_max([1, 2, 3, 4, 5]))           # [1, 5]
    print(min_max([-1, -2, -3, -4, -5]))      # [-5, -1]