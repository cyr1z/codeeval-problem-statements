import sys


def float_formatter(n):
    return str('{:.3f}'.format(n)).replace('.', ',')


if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    f = open(filename, 'r')
    for line in f:
        line_list = list(line.strip().split())
        line_list = list(map(float, line_list))
        line_list.sort()
        line_list = list(map(float_formatter, line_list))
        print(*line_list)
    f.close()
