import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "input.txt"

    f = open(filename, 'r')
    for i in f:
        m = i.strip().split(',')
        if all(j.isdigit() for j in m):
            n = list(map(int, m))
            print(*sorted(list(set(n))), sep=', ')
    f.close()
