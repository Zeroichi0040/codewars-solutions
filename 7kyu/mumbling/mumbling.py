# multiply the first character by counter, add a "-", then capitalize
# remove the - at the end by returning a string sliced string

def accum(st):
    counter = 1
    result = ""

    for i in st:
        result += f"{i * counter}-".capitalize()
        counter += 1

    return result[:-1]
        
if __name__ == "__main__":
    print(accum("hi"))          # H-Ii
    print(accum("abcd"))        # A-Bb-Ccc-Dddd
    print(accum("RqaEzty"))     # R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy