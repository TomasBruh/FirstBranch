very_important_variable = "Hello"


def get_important_variable():
    global very_important_variable
    very_important_variable = "qqqq"
    print(very_important_variable)


get_important_variable()
print(very_important_variable)


def print_something():
    print("Hello world")


def print_something_with_args(text):
    print(f"Hello {text}")


def double_number(number):
    result = number * number
    return result


def double_number_with_default_value(number=9):
    result = number * number
    return result


def more_arguments(make, model, year, color, engine):
    print(f"Make: {make} | Model: {model} | Year: {year} | Color: {color} | Engine: {engine}")


def unknown_arguments(*args):
    """ Prints arguments """
    print(type(args))
    result = 0
    for numb in args:
        result += numb
    print(result)


def create_car(**kwargs):
    """ Prints key value arguments """
    print(type(kwargs))
    print(kwargs)

    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


def chain_function(*args):
    def inner_function(values):
        print(values)
        # chain_function(values)

    inner_function(args)


print_something()
print_something_with_args("World")
print(double_number(5))
print(double_number_with_default_value(8))
more_arguments("BMW", "5-er", 2020, "red", 3.0)
more_arguments(make="BMW", model="5-er", color="red", engine=3.0, year=2020)
unknown_arguments(5, 2, 3, 5, 6, 7, 8, 3, 5, 1, 5)
create_car(make="BMW", model="5-er", color="red", engine=3.0, year=2020)
chain_function(5, 2, 3, 5, 6, 7, 8, 3, 5, 1, 5)
