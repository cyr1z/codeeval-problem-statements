import sys


def sum_of_digit_sq(number):
    return sum([x ** 2 for x in list(map(int, (list(str(number)))))])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "input.txt"

    f = open(filename, 'r')
    for i in f:
        m = int(i.strip())
        values = []
        while m != 1:
            if m in values:
                m = 0
                break
            values.append(m)
            m = sum_of_digit_sq(m)
        print(m)
    f.close()
