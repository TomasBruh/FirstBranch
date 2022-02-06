def does_fall_into_rage(range_start, range_finish, number):
    if number >= range_start:
        if number <= range_finish:
            return True


nr = 10
print(does_fall_into_rage(10, 100, nr))
