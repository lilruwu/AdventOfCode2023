result = 0
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        numbers = [char for char in line if char.isdigit()]

        combined_numbers = int(numbers[0] + numbers[-1])
        #print (combined_numbers)
        result += combined_numbers
    print ("The result is: " + str(result))