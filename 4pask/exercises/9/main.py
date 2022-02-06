def number_is_prime(given_number):
    for i in range(2, int(given_number / 2 + 1)):
        if given_number % i == 0:
            return False
    return True


number = 12
print(number_is_prime(number))
