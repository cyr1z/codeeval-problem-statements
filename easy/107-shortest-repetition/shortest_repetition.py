import sys

if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename, "r") as read_file:
        for line in read_file:
            line = line.strip()
            if line.strip():
                for i in range(1, len(line)+1):
                    if line[0:i] == line[i:2*i] and line.count(line[0:i]) * line[0:i] == line or i == len(line):
                        print(i)
                        break


