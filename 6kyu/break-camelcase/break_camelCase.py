# loop through the given string, add every looped index to a new variable after checking if the character is capitalized or not
# when a capitalized letter is found, it runs the if block to add a space, then it adds the capitalized letter
# order of execution is important here

def solution(s):
    sentence = ""
    for char in s:
        if char == char.upper():
            sentence += " "
        sentence += char
    return sentence

print(solution("helloWorld"))   # hello World