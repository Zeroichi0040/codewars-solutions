# compare the first and last index of the array, if they are the same then neither is the odd number and the constant is found
# if they are not equal, it means either has the odd number and we can safely assume the second index is the constant
# using a for loop to check if the looped index is not the same as constant to find the odd number, then immediately return to not loop through the rest of the array

def stray(arr):
    if arr[0] == arr[-1]:
        constant = arr[0]
    else:
        constant = arr[1]
        
    for i in arr:
        if i != constant:
            return i

if __name__ == "__main__":
    print(stray([1, 1, 2]))                     # 2
    print(stray([17, 17, 13, 17, 17, 17, 17]))  # 13