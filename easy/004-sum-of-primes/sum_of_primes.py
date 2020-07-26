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
    i = 0
    j = 0
    sum_prime = 0
    max_count = 1000
    while i < max_count:
        j += 1
        if is_prime(j):
            i += 1
            sum_prime += j
    print(sum_prime)
