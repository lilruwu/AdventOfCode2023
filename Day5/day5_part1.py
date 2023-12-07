from collections import defaultdict

with open("example.txt") as f:
    lines = f.readlines()


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

    for line in lines:
            if line is lines[0]:
                seeds = lines[0].split(":")[1].strip().split()
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
                         current_dict[int(data[0])+i] = int(data[1])+i
                    

                    #print(current_dict)
                



    
                
    