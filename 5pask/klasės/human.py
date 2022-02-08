class Human:  # Iš didžiosios raidės
    """ Human object """  # aprašymas

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def change_human(self, name, surname, age):
        """ Changes the human """
        self.name = name
        self.surname = surname
        self.age = age

    def get_human_info(self):
        """ Show all human attributes """
        print(f"Name: \t\t{self.name}")
        print(f"Surname: \t{self.surname}")
        print(f"Age: \t\t{self.age}")