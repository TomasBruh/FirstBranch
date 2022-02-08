from human import Human


class Student(Human):
    """ Initialize Student class while extending human class """

    def __init__(self, name, surname, age, grade):
        super().__init__(name, surname, age)  # iškviečiam šitam konstruktoriuje human konstruktorių
        self.grade = grade

    def get_student_info(self):
        """ Show all student info """
        self.get_human_info()
        print(f"Grade: \t\t{self.grade}")
