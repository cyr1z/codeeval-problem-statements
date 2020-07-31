import sys


def get_roman_notation(x):
    """
    returns a Roman notation string for a digit using
    the passed list of case-matching Roman numerals
    :param x: (9, ('I', 'V', 'X'))
    :return: 'IX'
    """
    if x[0] < 4:
        return x[1][0] * x[0]
    elif x[0] == 4:
        return x[1][0] + x[1][1]
    elif x[0] < 9:
        return x[1][1] + x[1][0] * (x[0] - 5)
    return x[1][0] + x[1][2]


def get_roman(x):
    """
    convert decimal number to romanian for 0 - 3999
    :param x: number (159 or '159')
    :return: Roman numeral string('CLIX')
    """
    roman_registers = (('I', 'V', 'X'), ('X', 'L', 'C'), ('C', 'D', 'M'), ('M',))
    x = str(x)
    x_register_list = tuple(map(int, x.strip()))
    pair_registers = tuple(zip(x_register_list[::-1], roman_registers))
    return ''.join(tuple(map(get_roman_notation, pair_registers))[::-1])


if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename, "r") as read_file:
        for line in read_file:
            if line.strip().isdigit() and int(line) <= 3999:
                print(get_roman(line))
