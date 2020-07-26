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
            p, g = 0, 1
            n = list(map(int, m))
            while p < n[0]:
                p = n[1] * g
                g += 1
            print(p)
    f.close()
