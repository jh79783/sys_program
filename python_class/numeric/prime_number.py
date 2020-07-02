def check_prime_number(num):
    if num <= 2:
        return True
    for n in range(2, num):
        mul = num // n
        if mul * n == num:
            return False

    return True

