import sys


def get_roman_notation(x):
    if x[0] < 4:
        return x[1][0] * x[0]
    elif x[0] == 4:
        return x[1][0] + x[1][1]
    elif x[0] < 9:
        return x[1][1] + x[1][0] * (x[0] - 5)
    return x[1][0] + x[1][2]


def get_roman(x):
    roman_registers = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M'], ['M']]
    x = str(x)
    x_register_list = list(map(int, x.strip()))
    pair_registers = list(zip(x_register_list[::-1], roman_registers))
    return ''.join(list(map(get_roman_notation, pair_registers))[::-1])


if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename, "r") as read_file:
        for line in read_file:
            if line.strip().isdigit() and int(line) <= 3999:
                print(get_roman(line))
