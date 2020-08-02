import sys

if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename, "r") as read_file:
        for line in read_file:
            line_list = line.split(':')
            num_list = line_list[0].strip().split()
            change_list = (tuple(map(int, x.split('-'))) for x in line_list[1].strip().split(','))
            for i in change_list:
                num_list[i[0]], num_list[i[1]] = num_list[i[1]], num_list[i[0]]
            print(' '.join(num_list))
