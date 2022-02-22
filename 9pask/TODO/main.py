from prettytable import PrettyTable
import json
program_running = True
# try:
#     with open("./stages_of_tasks.txt") as stages_stream:
#         stages = stages_stream.readlines()
# except FileNotFoundError:
#     print("CRITICAL ERROR: File not found.")
#     print("Shutting down.")
#     program_running = False
all_tasks = {}
try:
    with open("tasks/all_tasks.txt") as file_stream:
        all_tasks = json.loads(file_stream.read())
        file_stream.close()
except FileNotFoundError:
    print("There are no completed tasks available for viewing.")
myTable = PrettyTable()
# for item in all_tasks_for:
#     all_tasks_for_name = item.split(':')
#     all_tasks[all_tasks_for_name[0]] = all_tasks_for_name[1]
# myTable = PrettyTable(["Task name", "Status"])
# for item in all_tasks:
#     myTable.add_row(str(all_tasks[item]))
# print(myTable)
# for item in all_tasks:
#     P
collunms1 = []
collunms2 = []
for key, value in all_tasks:
    collunms1.append(key)
    collunms2.append(value)
print(all_tasks.keys())
print(all_tasks)
myTable.add_column("Task name", collunms1)
myTable.add_column("Status", collunms2)

while program_running:
    print(myTable)
    command = input("What?: ")
    if command == "off":
        program_running = False
        
# EXTEND THE TABLE
