# check first if either n or m is less than 0, if it is return 0
# otherwise return n multiplied by m

def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n * m

if __name__ == "__main__":
    print(paperwork(5, 5))      # 25
    print(paperwork(-3, 3))     # 0
