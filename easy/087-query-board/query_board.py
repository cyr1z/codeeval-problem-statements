import sys


def set_row(i, x, matrix):
    matrix[i] = [x for _ in range(len(matrix[i]))]


def set_col(j, x, matrix):
    for i in matrix:
        i[j] = x


def query_row(i, matrix):
    print(sum(matrix[i]))


def query_col(j, matrix):
    print(sum(matrix[x][j] for x in range(len(matrix))))


if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    my_matrix = [[0 for _ in range(256)] for x in range(256)]
    functions = {'SetCol': set_col, 'SetRow': set_row, 'QueryCol': query_col, 'QueryRow': query_row}

    f = open(filename, 'r')
    for line in f:
        line_list = list(line.strip().split())
        arguments = list(map(int, line_list[1:]))
        func_s = functions[line_list[0]]
        func_s(*arguments, my_matrix)
    f.close()
