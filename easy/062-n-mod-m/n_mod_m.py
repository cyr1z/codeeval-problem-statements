import sys


def n_mod_m(n, m):
    while n > m:
        n -= m
    return n


if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    f = open(filename, 'r')
    for line in f:
        line_list = line.strip().split(',')
        line_list = list(map(int, line_list))
        print(n_mod_m(line_list[0], line_list[1]))
    f.close()
