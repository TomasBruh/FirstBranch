

def sum_of_list(a_list):
    the_sum = 0
    for number in a_list:
        the_sum += number
    return the_sum


sample_list = [2, 7, 10, 322]
sum_of_sample_list = sum_of_list(sample_list)
print(sum_of_sample_list)
