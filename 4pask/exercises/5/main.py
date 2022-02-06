def factorial_of_a_nr(number):
    answer = 1
    while number > 0:
        answer = answer * number
        number = number - 1
    return answer


print(factorial_of_a_nr(7))
