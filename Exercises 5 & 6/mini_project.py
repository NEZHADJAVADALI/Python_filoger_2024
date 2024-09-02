# We suggest that you use the ToDoList.py file.
# create three empty list for storing information
task_name = []
task_status = []
task_duration = []
all_tasks_minutes = 0
Done_tasks = 0
Undone_tasks = 0
print(f"hello...this is task managment app!!!")

for _ in range(1,201):
    # print menu
    choose = input(
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
    
    # take input
    if choose == "1":       # Add task
        print("- Adding task: ")
        task = input("Pleas Enter your task: ")
        
        # check for repitation of task
        if task in task_name:
            for i in range(200):
                task = print("repetitive task name!!! try again ")
                if task in task_name:
                    break
        
        # update lists
        task_name.append(task)
        task_status.append(False)
        task_duration.append(None)
    elif choose == "2":     # Displaying all tasks
        print("- Displaying all tasks: \n")
       
        #for i in range(len(task_name)):
            #task_status[i] = "Done" if task_status[i] else "Undone"

        for i in range(len(task_name)):
            print(f"{task_name[i]} status is {task_status[i]} and Duration is {task_duration[i]}") 
    elif choose == "3":
        print("- Removing task: ")
        remove_name = input("please Enter task name to remove: ")
        
        if remove_name not in task_name:
            for i in range(200):
                remove_name = input("Task you enterd is not valid, try again: ")
                if remove_name in task_name:
                    break
                
        i = task_name.index(remove_name)
        task_name.pop(i)
        task_status.pop(i)
        task_duration.pop(i)
        
        print(f"{remove_name} removed!!!")
    elif choose == "4":     # edit task
        print("editing task...\n")
        task_name_for_edit = input("what is the name of task you want to edit? ")
        
        # change the name of the task
        if task_name_for_edit not in task_name:
            for i in range(200):
                task_name_for_edit = input("task does't exist, try again...") 
                if task_name_for_edit in task_name:
                    break       
        
        i = task_name.index(task_name_for_edit)
        task_new_name = input(f"say the new name of the {task_name_for_edit}: ")
        task_name[i] = task_new_name
        print(f"name of task {task_name_for_edit} changed to {task_new_name}")
    elif choose == "5":     # search
        print("Searching: \n")
        search = input("what is the name of task: \n")        
        
        if search not in task_name:
            for i in range(200):
                search = input("task does't exist, try again...\n") 
                if search in task_name:
                    break
        i = task_name.index(search)
        print(f"{task_name[i]} information: \n"
             f"{task_name[i]} status is {task_status[i]} and Duration is {task_duration[i]}"
             ) 
    elif choose == "6": # mark task
        print("marking done: \n")
        task_to_mark = input("Please say the name of task you want to mark done: ")
        
        if task_to_mark not in task_name:
            for i in range(200):
                task_to_mark = input("task does't exist, try again...:\n") 
                if task_to_mark in task_name:
                    break
        
        task_to_mark_index = task_name.index(task_to_mark)
        check_mark = input("Please insert Done or Undone to mark: ")
        
        if check_mark != "Done" or check_mark != "Undone":
            for i in range(200):
                check_mark = input("Wrong input...Please try again...\n")
                if check_mark == "Done" or check_mark == "Undone":
                    break
        if check_mark == "Done":
            task_status[task_to_mark_index] = "Done"
            print(f"Let's calculate the duration of task {task_to_mark}")
            # calculate duration
            start_time = input("when is start of task (HH:MM): ") 
            end_time = input("when is end of task (HH:MM): ")   
            hour_start = int(start_time.split(":")[0])
            minut_start = int(start_time.split(":")[1])
            hour_end = int(end_time.split(":")[0])
            minute_end = int(end_time.split(":")[1])
            
            # total minit
            total_minute1 = hour_start * 60 + minut_start
            total_minute2 = hour_end * 60 + minute_end
            
            # calculating new hour and minutes
            time_difference = total_minute2 - total_minute1
            
            difference_hour = time_difference // 60
            difference_minute = time_difference % 60
            duration = str(difference_hour) + ":" + str(difference_minute)
            task_duration[task_to_mark_index] = duration
            
            all_tasks_minutes += time_difference
            all_tasks_hour = all_tasks_minutes // 60
            all_tasks_minute = all_tasks_minutes % 60
            work_hour = str(all_tasks_hour) + ":" + str(all_tasks_minute)
        elif check_mark == "Undone": 
            task_status[task_to_mark_index] = "Undone"
            
        if check_mark == "Done":
            print(f"The statuse of task {task_to_mark} change to Done and  Duration is {duration}")
        elif check_mark == "Undone":
            print(f"the statuse of task {task_to_mark} is Undone")
    elif choose == "7":     #Display details
        num_of_tasks = len(task_name)
        for i in task_status:
            if i == "Done":
                Done_tasks += 1
            elif i == "Undone":
                Undone_tasks += 1
        print("Report... \n"
              f" - Number of Total tasks is: {num_of_tasks}\n"
              f" - Total number worked on tasks is: {work_hour}\n"
              f" - Number of completed tasks is: {Done_tasks}\n"
              f" - Number of Ucompleted tasks is: {Undone_tasks}\n"
              )
    elif choose == "8":
        print("""INTRUCTIONS:
                - To choose each option please insert the number of option
                  after going to ralated option menu follow the instrucions 
                  displayed on your monitor
              """)
       

    
        
        