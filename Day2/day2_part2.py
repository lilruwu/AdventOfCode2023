with open("input.txt", "r") as f:
    lines = f.readlines()
    result = 0

    
    for game in lines:
        max_red = 0
        max_green = 0
        max_blue = 0
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
                            max_red = int(quatity)
                    elif color == "green":
                        if int(quatity) > max_green:
                            max_green = int(quatity)
                    elif color == "blue":
                        if int(quatity) > max_blue:
                            max_blue = int(quatity)
        # print("RED: ",max_red)
        # print("GREEN: ",max_green)
        # print("BLUE: ",max_blue)
        game_power = max_red * max_green * max_blue
        result += game_power
    
print(result)
                                   