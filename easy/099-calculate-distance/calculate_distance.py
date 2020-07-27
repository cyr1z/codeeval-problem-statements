import sys
from math import sqrt

if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    f = open(filename, 'r')
    for line in f:
        line_list = list(line.strip().split(') ('))
        line_list[0] = line_list[0].replace('(', '')
        line_list[1] = line_list[1].replace(')', '')
        a_point = list(map(int, line_list[0].strip().split(',')))
        b_point = list(map(int, line_list[1].strip().split(',')))

        print(int(sqrt((a_point[0] - b_point[0])**2 + (a_point[1] - b_point[1])**2)))
    f.close()
