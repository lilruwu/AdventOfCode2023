from collections import defaultdict

with open ("input.txt") as f:
    lines = f.readlines()
    cards_won = defaultdict(lambda:1)
    #cards_won[1] = 1

    for line in lines:

        line_result = 0
        line = line.strip().split(":")
        card = line[0].strip().split()
        card_number = int(card[1])        
        # print(card_number)
        line = line[1].split("|")  
        possible_numbers = line[0].strip().split()
        int_possible_numbers = [int(i) for i in possible_numbers]
        winning_numbers = line[1].strip().split()
        int_winning_numbers = [int(i) for i in winning_numbers]     
        # print(int_possible_numbers)
        # print(int_winning_numbers)
        multiplier = card_number + 1
        pivote = cards_won[card_number]
        for number in int_winning_numbers:
            
            if number in int_possible_numbers:
                        counter = cards_won[card_number]
                #while counter > 0 and card_number < len(lines):
                    #for i in range(counter):                       
                        # print("Card number: ", card_number)
                        # print("Count:", counter)
                        # print("Multi: ", multiplier)
                        cards_won[multiplier] += 1*counter
                        counter -= 1
                        multiplier += 1
                
            
            else:
                continue
    
# print(cards_won)
result = sum(cards_won.values())

print("The result is: ",result)
        #print(line_result)



        