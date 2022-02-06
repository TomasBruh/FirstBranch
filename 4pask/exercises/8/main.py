def return_unique_list(a_list):
    unique_set = set(a_list)
    unique_list = []
    for item in unique_set:
        unique_list.append(item)
    return unique_list


my_list = [1, 6, 6, 6, 8]
print(return_unique_list(my_list))
