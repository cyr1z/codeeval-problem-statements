import sys

if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    f = open(filename, 'r')
    for line in f:
        line_list = [x.capitalize() for x in list(line.strip().split())]
        print(*line_list)
    f.close()
