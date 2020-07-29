import sys

wd = {'zero': '0', 'one': '1', 'two': '2','five': '5','seven': '7', 'eight': '8',
      'four': '4', 'three': '3', 'six': '6', 'nine': '9'}

if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename, "r") as read_file:
        for line in read_file:
            if line.strip():
                line_list = line.strip().split(';')
                print(''.join(wd[i] for i in line_list))