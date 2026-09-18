# takes an array, returns the sum of all positive numbers

def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
    return sum

if __name__ == "__main__":
    print(positive_sum([2, 1]))     # 3
    print(positive_sum([-3, -2]))   # 0
    print(positive_sum([]))         # 0