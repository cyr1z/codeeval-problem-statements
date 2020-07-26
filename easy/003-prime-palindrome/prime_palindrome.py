def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if not n % f:
            return False
        if not n % (f+2):
            return False
        f += 6
    return True


if __name__ == '__main__':
    max_count = 1000
    for x in range(max_count, 2, -1):
        if is_palindrome(x) and is_prime(x):
            print(x)
            break
