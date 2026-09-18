# takes an array and returns the array with each value inside it doubled

def maps(a):
    b = []
    for i in a:
        b.append(i * 2)
    return b

if __name__ == "__main__":
    print(maps([2, 4, 6]))      # 4, 8, 12