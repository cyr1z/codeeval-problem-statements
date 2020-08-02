import sys


def is_digit(x):
    return str(x).isdigit()


if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename, "r") as read_file:
        for line in read_file:
            line_list = line.strip().split(',')
            digits = ','.join(list(filter(is_digit, line_list)))
            words = ','.join(x for x in line_list if x not in digits)
            separ = ''
            if digits and words:
                separ = ' | '
            print(words, digits, sep=separ)
