import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "input.txt"

    f = open(filename, 'r')
    for i in f:
        m = list(map(int, (list(i.strip()))))
        self_d = 1
        for idx, val in enumerate(m):
            if not m.count(idx) == val:
                self_d = 0
                break
        print(self_d)
    f.close()
