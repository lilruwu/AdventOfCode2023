result = 1
counter = 0

with open("input.txt") as f:
    lines = f.read().split("\n")


    times = lines[0].split(":")[1].split()
    distances = lines[1].split(":")[1].split()
    time = int(''.join(times))
    distance = int(''.join(distances))

    partial_result = 0       
    for i in range(time):
        i = i+1
        #print(i)
        resto = int(time) - i
        #print(resto)
        real_distance = resto*i
        #print(real_distance)
        if real_distance > int(distance):
            partial_result += 1
            #print("VALUE IS: ", i)
                    
        else:
            continue
    #print(partial_result)
    counter +=1
    result = result * partial_result
print("The result is: ",result)
            
            
                