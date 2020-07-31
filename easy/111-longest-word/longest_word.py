import sys

if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename, "r") as read_file:
        for line in read_file:
            line = line.strip()
            line_list = list(line.split())
            line_list.sort(key=lambda s: len(s), reverse=True)
            print(line_list[0])
