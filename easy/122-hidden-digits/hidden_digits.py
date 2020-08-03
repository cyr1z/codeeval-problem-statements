import sys

code_string = 'abcdefghij'

if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    code_list = list(code_string)

    with open(filename, "r") as read_file:
        for line in read_file:
            line_list = list(line.strip())
            digits = [x for x in line_list if x in code_list or x.isdigit()]
            res = []
            for i in digits:
                if i.isdigit():
                    res.append(i)
                    continue
                res.append(str(code_list.index(i)))
            if not res:
                res.append('NONE')

            print(''.join(res))
