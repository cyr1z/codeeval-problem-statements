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
            b = list(bin(n[0]))[::-1]
            print(str(b[n[1]-1] == b[n[2]-1]).lower())
    f.close()
