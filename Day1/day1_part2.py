digits = ('zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine')

def findNumbers(line):
    numbers = []
    for i, c in enumerate(line):
        if c.isdigit():
            numbers.append(int(c))
            continue
        for n, name in enumerate(digits):
            if line[i:].startswith(name):
                numbers.append(n)
                break
    return numbers[0] * 10 + numbers[-1]

def main():
    total_sum = 0
    file_name = "input2.txt"  # Reemplaza con el nombre de tu archivo

    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            total_sum += findNumbers(line)

    print("The sum of all calibration values is:", total_sum)

if __name__ == "__main__":
    main()
