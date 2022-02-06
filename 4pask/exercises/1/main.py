nr1 = 3
nr2 = 9
nr3 = 123


def find_max(nr_1, nr_2, nr_3):
    """ Finds the max of three numbers """
    max_nr = nr_1
    if nr_2 > max_nr:
        max_nr = nr_2
    if nr_3 > max_nr:
        max_nr = nr_3
    return max_nr
