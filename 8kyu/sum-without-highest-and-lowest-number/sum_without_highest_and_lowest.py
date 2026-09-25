# check first if there is nothing inside the provided array or if there is less than or equal to 2 items inside the array
# if there is, return 0. else, the expected result can be given

def sum_array(arr):
    if arr == None or len(arr) <= 2:
        return 0
    else:
        minimum_value = arr[0]
        maximum_value = arr[0]
        sum = 0
        for i in arr:
            if i > maximum_value:
                maximum_value = i
            elif i < minimum_value:
                minimum_value = i

        for i in arr:
            sum += i

        return sum - (maximum_value + minimum_value)

if __name__ == "__main__":
    print(sum_array([]))                # 0
    print(sum_array([1]))               # 0
    print(sum_array([1, 2]))            # 0
    print(sum_array([6, 2, 1, 8, 10]))  # 16


