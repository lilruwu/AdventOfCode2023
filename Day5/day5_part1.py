from collections import defaultdict

with open("input.txt") as f:
    lines = f.readlines()
    min_location = -1


    maps = {
        "seed-to-soil map": defaultdict(int),
        "soil-to-fertilizer map": defaultdict(int),
        "fertilizer-to-water map": defaultdict(int),
        "water-to-light map": defaultdict(int),
        "light-to-temperature map": defaultdict(int),
        "temperature-to-humidity map": defaultdict(int),
        "humidity-to-location map": defaultdict(int),
    }

    current_dict = None
# All the numbers of the file are in the dictionary
    for line in lines:
            if line is lines[0]:
                continue
            elif line == "\n":
                continue
            else:
                data=line.split()
                line = line.strip()

                if line == "seed-to-soil map:":
                    current_dict = maps["seed-to-soil map"]
                elif line == "soil-to-fertilizer map:":
                    current_dict = maps["soil-to-fertilizer map"]
                elif line == "fertilizer-to-water map:":
                    current_dict = maps["fertilizer-to-water map"]
                elif line == "water-to-light map:":
                    current_dict = maps["water-to-light map"]
                elif line == "light-to-temperature map:":
                    current_dict = maps["light-to-temperature map"]
                elif line == "temperature-to-humidity map:":
                    current_dict = maps["temperature-to-humidity map"]
                elif line == "humidity-to-location map:":
                    current_dict = maps["humidity-to-location map"]
                else:                                
                    for i in range(int(data[2])):
                         current_dict[int(data[1])+i] = int(data[0])+i
    
    seeds = lines[0].split(":")[1].strip().split()

    for seed in seeds:
        if int(seed) in maps["seed-to-soil map"]:
            
            soil = int(maps["seed-to-soil map"][int(seed)])
        else:
            soil = int(seed)
        
        if soil in maps["soil-to-fertilizer map"]:
            fertilizer = int(maps["soil-to-fertilizer map"][soil])
        else:
            fertilizer = soil
        if fertilizer in maps["fertilizer-to-water map"]:
            
            water = int(maps["fertilizer-to-water map"][fertilizer])
        else:
            water = fertilizer
        if water in maps["water-to-light map"]:
            light = int(maps["water-to-light map"][water])
        else:
            light = water
        if light in maps["light-to-temperature map"]:
            temperature = int(maps["light-to-temperature map"][light])
        else:
            temperature = light
        if temperature in maps["temperature-to-humidity map"]:
            humidity = int(maps["temperature-to-humidity map"][temperature])
        else:
            humidity = temperature
        if humidity in maps["humidity-to-location map"]:
            location = int(maps["humidity-to-location map"][humidity])
        else:
            location = humidity

        if location < min_location or min_location == -1:
            min_location = location
    print("The result is: ", min_location)
                



    
                
    