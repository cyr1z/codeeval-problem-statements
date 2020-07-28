import sys
import json

if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename, "r") as read_file:
        for line in read_file:
            if line.strip():
                data = json.loads(line.strip())
            items = data['menu']['items']
            ids = [x['id'] for x in items if x and 'label' in x.keys()]
            print(sum(ids))
