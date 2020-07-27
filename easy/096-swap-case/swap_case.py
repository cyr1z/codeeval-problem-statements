import sys


def swap_case(my_string):
    if my_string.isupper():
        return my_string.lower()
    return my_string.upper()


if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    f = open(filename, 'r')
    for line in f:
        line_list = list(map(swap_case, list(line.strip())))
        print(''.join(line_list))
    f.close()
