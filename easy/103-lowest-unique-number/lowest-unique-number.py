import sys

if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename, "r") as read_file:
        for line in read_file:
            if line.strip():
                line_list = line.strip().split()

                if all(i.isdigit() for i in line_list):
                    line_list = list(map(int, line_list))

                    d = []
                    for i in set(line_list):
                        if line_list.count(i) == 1:
                            d.append(i)
                    if d:
                        d.sort()
                        print(line_list.index(d[0]))
                    else:
                        print(0)
