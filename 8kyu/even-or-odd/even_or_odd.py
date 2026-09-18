# takes an integer and returns "Even" if it's divisible by 2, otherwise returns "Odd"

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    print(even_or_odd(4))   # Even
    print(even_or_odd(7))   # Odd