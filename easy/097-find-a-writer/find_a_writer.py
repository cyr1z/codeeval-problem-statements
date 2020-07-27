import sys

if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    f = open(filename, 'r')
    for line in f:
        line_list = list(line.strip().split('|'))
        letters = list(line_list[0])
        keys = list(map(int, list(line_list[1].strip().split())))
        res = [letters[key - 1] for key in keys]
        print(''.join(res))
    f.close()
