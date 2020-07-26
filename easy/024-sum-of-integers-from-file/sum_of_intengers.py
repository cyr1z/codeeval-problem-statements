import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "input.txt"

    res = []

    f = open(filename, 'r')
    for i in f:
        if i.strip().isdigit():
            res.append(int(i))
    print(sum(res))
    f.close()
