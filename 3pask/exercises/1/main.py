numbers = input("Enter a sequence of numbers: ")
print(numbers)

nr_list = numbers.split(",")
nr_tuple = tuple(nr_list)
print(nr_list)
print(nr_tuple)
print(type(nr_tuple))
print(type(nr_list))
