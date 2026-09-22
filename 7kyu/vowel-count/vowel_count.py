# loop through each character of the string and compare in one if statement if its either of all the 5 vowels

def get_count(sentence):
    sum = 0
    for i in sentence:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            sum += 1
    return sum

if __name__ == "__main__":
    print(get_count("aeiou"))                                           # 5
    print(get_count("The quick brown fox jumps over the lazy dog"))     # 11