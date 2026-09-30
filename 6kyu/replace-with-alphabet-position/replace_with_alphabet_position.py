# store the positions of each letter in the alphabet in the dictionary
# make sure the string is all lower case with .lower()
# loop through each letter and refer to the dictionary

def alphabet_position(text):
    text = text.lower()
    pos = ""
    dict = {
        'a':1, 'b':2, 'c':3, 'd':4,
        'e':5, 'f':6, 'g':7, 'h':8,
        'i':9, 'j':10, 'k':11, 'l':12,
        'm':13, 'n':14, 'o':15, 'p':16,
        'q':17, 'r':18, 's':19, 't':20,
        'u':21, 'v':22, 'w':23, 'x':24,
        'y':25, 'z':26}
    
    for char in text:
        if char in dict:
            pos += f"{dict[char]} "
            
    return pos[:-1]

if __name__ == "__main__":
    print(alphabet_position("Hello"))   # "8 5 12 12 15"