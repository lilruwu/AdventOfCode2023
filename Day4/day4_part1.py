with open("input.txt") as f:
    lines = f.readlines()
    result = 0
    
    for line in lines:
        times = False
        line_result = 0
        line = line.strip()
        line = line.split(":")
        line = line[1].split("|")
        possible_numbers = line[0].strip().split()
        int_possible_numbers = [int(i) for i in possible_numbers]
        winning_numbers = line[1].strip().split()
        int_winning_numbers = [int(i) for i in winning_numbers]     
        #print(int_possible_numbers)
        #print(int_winning_numbers)
        for number in int_winning_numbers:
            if number in int_possible_numbers:
                if times == False:
                    line_result = 1
                    #print(number)
                    #print("First if: ",line_result)
                    times = True
                else:
                    #print(number)
                    
                    line_result = line_result * 2
                    #print("Second if: ",line_result)
            else:
                continue
        #print(line_result)
        result += line_result

print("The result is: ",result)
        