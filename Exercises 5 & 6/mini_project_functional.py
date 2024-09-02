task_name = []
task_status = []
task_duration = []
all_tasks_minutes = 0
Done_tasks = 0
Undone_tasks = 0

print(f"Hello...this is the task management app!!!")

def display_menu():
    return input(
        "----------\n"
        "Choose a number: \n"
        " 1 - Add task\n"
        " 2 - Display all tasks\n"
        " 3 - Remove task\n"
        " 4 - Edit task\n"
        " 5 - Search\n"
        " 6 - Mark done\n"
        " 7 - Display details\n"
        " 8 - Help\n"
        "----------\n"
    ).strip()

def add_task():
    print("- Adding task: ")
    task = input("Please enter your task: ")
    
    if task in task_name:
        print("Repetitive task name! Try again.")
        task = input("Please enter a new task: ")
    
    task_name.append(task)
    task_status.append("Undone")
    task_duration.append(None)

def display_all_tasks():
    print("- Displaying all tasks: \n")
    for i in range(len(task_name)):
        status = "Done" if task_status[i] == "Done" else "Undone"
        duration = task_duration[i] if task_duration[i] else "Not set"
        print(f"{task_name[i]} status is {status} and Duration is {duration}")

def remove_task():
    print("- Removing task: ")
    remove_name = input("Please enter the task name to remove: ")
    
    if remove_name in task_name:
        i = task_name.index(remove_name)
        task_name.pop(i)
        task_status.pop(i)
        task_duration.pop(i)
        print(f"{remove_name} removed!")
    else:
        print("Task does not exist.")

def edit_task():
    print("Editing task...\n")
    task_name_for_edit = input("What is the name of the task you want to edit? ")
    
    if task_name_for_edit in task_name:
        i = task_name.index(task_name_for_edit)
        task_new_name = input(f"Enter the new name for the task {task_name_for_edit}: ")
        
        if task_new_name in task_name:
            print("Task name already exists. Enter a new name.")
        else:
            task_name[i] = task_new_name
            print(f"Name of task {task_name_for_edit} changed to {task_new_name}")
    else:
        print("Task does not exist.")

def search():
    print("Searching: \n")
    search = input("What is the name of the task: \n")
    
    if search in task_name:
        i = task_name.index(search)
        print(f"{task_name[i]} information: \n"
              f"{task_name[i]} status is {task_status[i]} and Duration is {task_duration[i]}")
    else:
        print("Task does not exist.")

def mark_task():
    print("Marking done: \n")
    task_to_mark = input("Please enter the name of the task you want to mark done: ")
   
    if task_to_mark in task_name:
        task_to_mark_index = task_name.index(task_to_mark)
        check_mark = input("Please enter 'Done' or 'Undone' to mark: ")
        
        if check_mark in ["Done", "Undone"]:
            calculate_time(task_to_mark_index)            
            task_status[task_to_mark_index] = check_mark
            print(f"The status of task {task_to_mark} changed to {check_mark} and Duration is {task_duration[task_to_mark_index]}")
        else:
            print("Invalid input. Please enter 'Done' or 'Undone'.")
    else:
        print("Task does not exist.")

def calculate_time(task_index):
    global duration, work_hour, all_tasks_minutes

    print(f"Let's calculate the duration of task {task_name[task_index]}")
    start_time = input("When is the start of the task (HH:MM): ") 
    end_time = input("When is the end of the task (HH:MM): ")   
    hour_start = int(start_time.split(":")[0])
    minute_start = int(start_time.split(":")[1])
    hour_end = int(end_time.split(":")[0])
    minute_end = int(end_time.split(":")[1])
    
    total_minute1 = hour_start * 60 + minute_start
    total_minute2 = hour_end * 60 + minute_end
    
    time_difference = total_minute2 - total_minute1
    
    difference_hour = time_difference // 60
    difference_minute = time_difference % 60
    duration = f"{difference_hour}:{difference_minute}"
 
    task_duration[task_index] = duration
    all_tasks_minutes += time_difference
    all_tasks_hour = all_tasks_minutes // 60
    all_tasks_minute = all_tasks_minutes % 60
    work_hour = f"{all_tasks_hour}:{all_tasks_minute}"

def display_details():
    global Done_tasks, Undone_tasks, work_hour
    
    Done_tasks = 0
    Undone_tasks = 0
    num_of_tasks = len(task_name)
    
    for status in task_status:
        if status == "Done":
            Done_tasks += 1
        elif status == "Undone":
            Undone_tasks += 1
    
    print(f"Report... \n"
          f" - Number of Total tasks: {num_of_tasks}\n"
          f" - Total time worked on tasks: {work_hour}\n"
          f" - Number of completed tasks: {Done_tasks}\n"
          f" - Number of incomplete tasks: {Undone_tasks}\n")

def help_():
    print("""INSTRUCTIONS:
    - To choose each option, enter the corresponding number.
    - Follow the instructions displayed on your screen for each option.
    """)

# Main part
for _ in range(1, 201):
    choose = display_menu()
    
    if choose == "1":
        add_task()
    elif choose == "2":
        display_all_tasks()
    elif choose == "3":
        remove_task()
    elif choose == "4":
        edit_task()
    elif choose == "5":
        search()
    elif choose == "6":
        mark_task()
    elif choose == "7":
        display_details()
    elif choose == "8":
        help_()
