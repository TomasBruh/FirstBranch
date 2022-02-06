def multiplications_of_list(a_list):
    number = 1
    for nr in a_list:
        number = nr * number
    return number


the_list = [2, 8, -3]
answer = multiplications_of_list(the_list)
print(answer)
