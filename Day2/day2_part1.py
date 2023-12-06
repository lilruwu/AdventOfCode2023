with open("input.txt", "r") as f:
    lines = f.readlines()
    max_red = 12
    max_green = 13
    max_blue = 14
    result = 0

    
    for game in lines:
        red_score = 1
        green_score = 1
        blue_score = 1
        game_info = game.split(":")
        #print(game_info)
        game_number = game_info[0].split(" ")[1]
        #print(game_number)

        sets = game_info[1].split(";")
        #print(sets)
        #print(i)
        for set in sets:
            
             
            set.split(",")
            #print(set)
            
            
            for colors in set:
                colors = set.split(", ")
                #print(colors)
                
                for color_quantity in colors:
                    quatity,color = color_quantity.split()
                    #print(quatity)
                    #print(color)
                    if color == "red":
                        if int(quatity) > max_red:
                            red_score = 0
                    elif color == "green":
                        if int(quatity) > max_green:
                            green_score = 0
                    elif color == "blue":
                        if int(quatity) > max_blue:
                            blue_score = 0
        if red_score == 0 or green_score == 0 or blue_score == 0:
            continue
        else:
            result += int(game_number)    
                    
print("The sum of the valid games is: ", result)
                    
