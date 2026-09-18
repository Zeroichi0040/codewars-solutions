# takes an array, returns the sum of all values as if all were numbers

def sum_mix(arr):
    sum = 0
    for i in arr:
        sum += int(i)
    return sum
        

if __name__ == "__main__":
    print(sum_mix([2, '1', "4"]))     # 7
