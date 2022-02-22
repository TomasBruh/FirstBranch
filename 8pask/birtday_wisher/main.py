PLACEHOLDER = "[NAME]"

with open("./names/names.txt") as name_file:
    names = name_file.readlines()

with open("./letters/letter.txt") as letter_file:
    letter_content = letter_file.read()

    for name in names:
        stripped_name = name.strip()  # nuima tarpus
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)

        with open(f"./output/letters={stripped_name.lower()}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

