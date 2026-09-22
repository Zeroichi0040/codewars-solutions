# initialize sum with value of 1, iterate through each integer in the array and multiply sum by it

def grow(arr):
    sum = 1
    for i in arr:
        sum *= i
    return sum

if __name__ == "__main__":
    print(grow([1, 2, 3, 4]))       # 24
