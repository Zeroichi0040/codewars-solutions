# iterate through each item(pair) in the array, subtract the first character by the second character of that pair and add it to people

def number(bus_stops):
    people = 0
    for pair in bus_stops:
        sum = pair[0] - pair[1]
        people += sum
    return people

if __name__ == "__main__":
    print(number([[10,0],[3,5],[5,8]]))                         # 5
    print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))     # 17
