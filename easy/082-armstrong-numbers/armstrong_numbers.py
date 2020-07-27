import sys


def is_armstrong(number_string):
    z = len(number_string)
    m = list(map(int, list(number_string)))
    return sum(x ** z for x in m) == int(number_string)


if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    f = open(filename, 'r')
    for line in f:
        print(is_armstrong(line.strip()))
    f.close()
