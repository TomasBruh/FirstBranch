def function_1(number):
    new_number = number*number

    def function_2(number_2):
        new_number_2 = number_2 + 1
        return new_number_2
    new_number = function_2(new_number)
    return new_number


a_number = 3
print(function_1())
