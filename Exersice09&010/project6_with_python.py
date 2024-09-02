all_tasks = {}
next_key = 0


def menu():
    return input(
        """----------
Choose a number: 
1.Add task
2.Display all tasks
3.Remove task
4.Edit task
5.Search
6.Mark done
7.Display details
8.Help
9.Exit
----------\n"""
    ).strip()


def add_task():

    print("Adding task...\n")
    task = input("Please enter your task: \n")

    if any(task == value["Task"] for value in all_tasks.values()):
        print("Task already exist,try again...")
    else:
        task_dict = {
            "Task": task,
            "Status": False,
            "Duration": None
        }
        global next_key
        next_key += 1

        all_tasks[next_key] = task_dict
    print(all_tasks)


def display_all_task():
    print("Displaying all tasks...")
    for key, value in all_tasks.items():
        print(f'task {key}: {value["Task"]}')


def remove_task():
    print("Removing task...")
    task_to_remove = input("Please enter task to remove: ")

    found = False
    for key, value in all_tasks.items():
        if value["Task"] == task_to_remove:
            all_tasks.pop(key)
            print(f"{value['Task']} Successfully deleted")
            found = True
            break

    if not found:
        print("Task entered not valid, try again...")


def edit_task():
    print("Editing task...\n")
    task_name_for_edit = input("What is the name of the task you want to edit? ")

    for key, value in all_tasks.items():
        if task_name_for_edit == value["Task"]:
            new_name = input(f"Enter new name of {task_name_for_edit}: ")
            all_tasks[key]["Task"] = new_name
            print(f"{task_name_for_edit} changed to {new_name}")
            break


def search():
    print("Searching...")
    search_name = input("Please enter a name to search: ")

    found = False
    for key, value in all_tasks.items():
        if search_name == value["Task"]:
            print(f"{value['Task']} information: status|{value['Status']}, Duration|{value['Duration']}")
            found = True
            break

    if not found:
        print("name you entered is not valid, try again...")


def mark_done():
    print(f"marking Done...")
    task_to_mark = input("Please enter task to mark done: ")

    found = False
    for key, value in all_tasks.items():
        if task_to_mark == value["Task"]:
            all_tasks[key]["Status"] = "Done"
            duration = cal_duration()
            all_tasks[key]["Duration"] = duration
            print(f"status of {task_to_mark} changed to Done and duration of task is {duration}")
            found = True
            break

    if not found:
        print("task name is not valid, try again...")


def cal_duration():
    start = input("Please enter start of the task (HH:MM): ")
    end = input("Please enter end of the task (HH:MM): ")
    start_first_half, start_second_half = map(int, start.split(":"))
    end_first_half, end_second_half = map(int, end.split(":"))
    start_minutes = (start_first_half * 60) + start_second_half
    end_minutes = (end_first_half * 60) + end_second_half
    difference_in_minutes = end_minutes - start_minutes
    duration_hour = difference_in_minutes // 60
    duration_minute = difference_in_minutes % 60
    duration = f"{duration_hour}:{duration_minute:02d}"
    return duration


def display_details():
    print("Displaying details: ")
    for key, value in all_tasks.items():
        print(f"task number {key} is {value['Task']} whit status {value['Status']} and Duration of {value['Duration']}")

def help_():
    print("""menual:
for each section follow the orders...
with respect ali nezhadjavad
""")


def main():
    for i in range(1, 201):
        select = menu()
        if select == "1":
            add_task()
        elif select == "2":
            display_all_task()
        elif select == "3":
            remove_task()
        elif select == "4":
            edit_task()
        elif select == "5":
            search()
        elif select == "6":
            mark_done()
        elif select == "7":
            display_details()
        elif select == "8":
            help_()
        elif select == "9":
            print("Exiting the program. Goodbye!")
            break


main()
