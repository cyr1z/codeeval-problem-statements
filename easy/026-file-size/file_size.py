from os import stat
from sys import argv

if __name__ == '__main__':
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = "input.txt"
    print(stat(filename).st_size)
