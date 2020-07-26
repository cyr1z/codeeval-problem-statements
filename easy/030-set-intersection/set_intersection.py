import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "input.txt"

    f = open(filename, 'r')
    for i in f:
        m = i.strip().split(';')
        a_set = set(m[0].split(','))
        b_set = set(m[1].split(','))
        print(*(a_set & b_set), sep=',')

    f.close()
