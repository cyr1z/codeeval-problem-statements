import sys


def hex_to_decimal(my_hex_string):
    return str(int(my_hex_string, 16))


if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    f = open(filename, 'r')
    for line in f:
        print(hex_to_decimal(line.strip()))
    f.close()
