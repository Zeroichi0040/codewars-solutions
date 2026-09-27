# check first if passed array has anything inside before working with it
# find smalles value if provided array has something inside it
# use a state handler to loop through the given array, compare if the looped index is equal to the smallest value,
# and update state handler to ensure that it only removes the first occurence of the smallest value

def remove_smallest(numbers):
    if numbers == []:
        return numbers
    
    new_numbers = []
    smallest_rating = numbers[0]
    for i in numbers:
        if smallest_rating > i:
            smallest_rating = i
    
    removed = False
    for j in numbers:
        if j == smallest_rating and removed == False:
            removed = True
        else:
            new_numbers.append(j)

    return new_numbers
            
if __name__ == "__main__":
    print(remove_smallest([1, 2, 3, 4, 5]))     # [2, 3, 4, 5]
    print(remove_smallest([2, 1, 2, 1, 1]))     # [2, 2, 1, 1]
    print(remove_smallest([]))                  # []