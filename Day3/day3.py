with open("example.txt") as f:
    lines = f.readlines()
i = 0

def is_synmbol(chars):
    for char in chars:
        print("Char is: ",char)
        if char == '#' or char == '*' or char == '$' or char == '+':
            print("Symbol")
        elif char.isdigit():
            print("Digit")
        elif char == '.': 
            print("Dot")

for chars in lines:
    chars = lines[i].split()
    is_synmbol(chars)
    #print("Char is: ",chars)
    i += 1

            