import sys


def get_clean_string(my_string):
    # return ''.join(filter(lambda x: x.isidentifier() or x.isspace(), my_string))
    return ''.join(filter(lambda x: x.isidentifier(), my_string))


if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    f = open(filename, 'r')
    for line in f:
        line = line.lower()
        line = get_clean_string(line)
        line_list = list(line)
        line_set = set(line_list)
        d = [line_list.count(i) for i in line_set]
        d.sort(reverse=True)
        print(sum(x[0]*x[1] for x in list(zip(d, range(26, 0, -1)))))
    f.close()
