from person import Person
import datetime
people = []
with open("people_info.txt") as data_stream:
    people_info = data_stream.readlines()

for person in people_info:
    person_info = person.split(' ')
    new_person = Person(person_info[0], datetime.datetime.strptime(person_info[1], '%Y-%m-%d'), person_info[2])
    print(type(new_person.name))
