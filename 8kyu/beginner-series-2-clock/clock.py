# takes in h(hour), m(minute), and s(second) variables, convert each to milliseconds and return with the sum of all three variables

def past(h, m, s):
    s *= 1000
    m *= 60000
    h *= 3600000
    
    return s + m + h
        
if __name__ == "__main__":
    print(past(1, 1, 1))    # 3661000
    print(past(0, 0, 0))    # 0
    print(past(1, 0, 2))    # 3602000
