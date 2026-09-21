# declare two variables to keep track of what to return and how much to increment
# from what i understand, we increase sum by the increment variable until said variable is equal to num variable

def summation(num):
    sum = 0
    increment = 0
    while increment < num:      # while loop will keep running until increment is equal to num
        increment += 1          # if increment variable is still less than num, increase the value by 1
        sum += increment        # then add this value to sum. if i summate the number 8, the process should look like 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36
    return sum
    
if __name__ == "__main__":
    print(summation(1))     # 1
    print(summation(8))     # 36