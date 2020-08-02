import sys

morse_code = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}

morse_code_revert = dict((val, key.upper()) for key, val in morse_code.items())


def morse_word(x):
    """
    convert an alphabet word to space separated word in morse code
    :param x: str word
    :return: str space separated word in morse code
    """
    d = [x.lower() for x in list(x)]
    return ' '.join(morse_code[i] for i in d)


def morse_string(x):
    """
    convert an alphabet string to double space separated word in morse code
    :param x: str string
    :return: str double space separated string in morse code
    """
    words_list = [x for x in x.strip().split()]
    words = list(map(morse_word, words_list))
    return '  '.join(words).strip()


def de_morse_word(x):
    """
    convert a space separated word in morse code to alphabet word
    :param x: str each letter separated by space char
    :return: str word
    """
    return ''.join(morse_code_revert[i] for i in x.split())


def de_morse_string(x):
    """
    convert a double space separated string in morse code to alphabet string
    :param x: str each word separated by 2 space chars.
    :return: str text string
    """
    words_list = [x for x in x.strip().split('  ')]
    words = list(map(de_morse_word, words_list))
    return ' '.join(words).strip()


if __name__ == '__main__':
    filename = "input.txt"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename, "r") as read_file:
        for line in read_file:
            print(de_morse_string(line))
            # print(morse_string(de_morse_string(line)) == line.strip())
