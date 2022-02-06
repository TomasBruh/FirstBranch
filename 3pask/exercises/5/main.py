inserted_string = input("Insert the string: ")
good_str = ""
if inserted_string.__contains__("Is"):
    if not inserted_string.startswith("Is"):
        is_count = inserted_string.split("Is")
        for i in range(len(is_count) - 1):
            is_count.insert(0, "Is ")
        return_string = ""
        for x in range(len(is_count)):
            return_string += (" " + is_count.pop(0))
        print(return_string)
