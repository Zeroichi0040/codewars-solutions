# my method converts the number into a list of digits, which i can then loop through to insert in a separte list
# on the first index, 0, for each digit

def digitize(n):
    list = [int(digit) for digit in str(n)]
    m = []
    for i in list:
        m.insert(0, i)
    return m