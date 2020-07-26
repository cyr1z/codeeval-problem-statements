def dig_formatter(n, max_len):
    return ' ' * (max_len - len(str(n))) + str(n)


if __name__ == '__main__':
    line_count = 12
    maximal_len = len(str(line_count ** 2))
    for i in range(1, line_count + 1):
        print(' '.join([dig_formatter(j * i, maximal_len) for j in range(1, line_count + 1)]))
