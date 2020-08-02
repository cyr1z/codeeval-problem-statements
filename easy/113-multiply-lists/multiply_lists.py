import sys
from numpy import prod

if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename, "r") as read_file:
        for line in read_file:
            line_list = [map(int, i.split()) for i in line.split('|')]
            results = [prod(i) for i in zip(*line_list)]
            print(' '.join(map(str, results)))
            # print(' '.join(map(str, [prod(i) for i in zip(*[map(int, i.split()) for i in line.split('|')])])))
