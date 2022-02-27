def add_task(command: str, data: dict):
    command.replace("add ", "")


def circle_trough(command: str, data):
    if command.startswith("add"):
        add_task(command, data)
