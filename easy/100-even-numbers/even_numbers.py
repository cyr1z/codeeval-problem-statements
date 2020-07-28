import sys

if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    f = open(filename, 'r')
    for line in f:
        if line.strip().isdigit():
            if int(line.strip()) % 2:
                print(0)
                continue
            print(1)
    f.close()
