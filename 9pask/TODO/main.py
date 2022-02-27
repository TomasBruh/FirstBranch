from prettytable import PrettyTable
import commands
import json
program_running = True
myTable = PrettyTable()

try:
    with open('./tasks/all_tasks.txt', 'r') as f:
        pure_data = f.read()
        f.close()
        data = json.loads(pure_data)
        myTable.add_column("Task", [*data])
        myTable.add_column("Status", [*data.values()])
except FileNotFoundError:
    myTable.add_column("Task", [])
    myTable.add_column("Status", [])
    with open('./tasks/all_tasks.txt', 'w') as f:
        f.close()

while program_running:
    print(myTable)
    user_input = input()
    if user_input == "off":
        program_running = False
    else:
        commands.circle_trough(user_input, data)
