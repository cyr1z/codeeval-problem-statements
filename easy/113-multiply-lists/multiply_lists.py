import sys

if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename, "r") as read_file:
        for line in read_file:
            line_list = line.split('|')
            left_list = map(int, line_list[0].strip().split())
            right_list = map(int, line_list[1].strip().split())
            results = [i[0] * i[1] for i in zip(left_list, right_list)]
            print(' '.join(map(str, results)))
