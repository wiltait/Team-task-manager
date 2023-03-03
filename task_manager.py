from datetime import date, datetime

# ------------------------------------------------------------------
# Store logins and passwords in a dictionary
accounts = {}

# Open file 'user.txt' to read 
user_read = open("user.txt", "r")
user_data = user_read.readlines()
for line in user_data:
    user_lines = line.strip()
    user_lines = user_lines.split(", ")
    # Append login and password to the dictionary 'accounts'
    accounts[user_lines[0]] = user_lines[1]

# ------------------------------------------------------------------
# Store username and tasks info in another dictionary
tasks = {}

tasks_read = open("tasks.txt", "r")
tasks_data = tasks_read.readlines()
for info in tasks_data:
    task_lines = info.strip()
    task_lines = task_lines.split(", ")
    
    username = task_lines[0]
    task = task_lines[2]
    date_assigned = task_lines[3]
    due_date = task_lines[4]
    completion = task_lines[5]

    tasks[username] = [task, date_assigned, due_date, completion]

# ------------------------------------------------------------------
# Function that will get task based on the logged user
def get_task_by_user(logged_user):
    
    list_of_tasks = []
        
    with open("tasks.txt", "r") as tasks:
        tasks_data = tasks.readlines()
        for task in tasks_data:
            task_lines = task.strip()
            task_lines = task_lines.split(", ")

            if logged_user == task_lines[0]:
                list_of_tasks.append(task_lines[1])
            else:
                pass
    
    return list_of_tasks

# ------------------------------------------------------------------
# Function that will return whether or not the task has been completed based on the logged user
def get_completion_by_user(logged_user):
    
    list_of_completion = []
        
    with open("tasks.txt", "r") as tasks:
        tasks_data = tasks.readlines()
        for task in tasks_data:
            task_lines = task.strip()
            task_lines = task_lines.split(", ")

            if logged_user == task_lines[0]:
                list_of_completion.append(task_lines[-1])
            else:
                pass
    
    return list_of_completion

# ------------------------------------------------------------------
# Function that will return the number of overdue and uncomplete tasks depending on the logged user (admin or else)
def get_overdue_by_user(logged_user):
    
    count_overdue = 0

    with open("tasks.txt", "r") as tasks:
        tasks_data = tasks.readlines()
        for task in tasks_data:
            task_lines = task.strip()
            task_lines = task_lines.split(", ")

            due_date = datetime.strptime(task_lines[4], '%d %b %Y')

            if logged_user == task_lines[0]:
                if (task_lines[-1] == "No") and ((due_date.date()) < date.today()):
                    count_overdue += 1

            else:
                pass
    
    return count_overdue  

# ------------------------------------------------------------------
# Function that will return a specific menu depending on the logged user (admin or else)
def menu(logged_user):
    if logged_user == "admin":
        print("---------------------------------------------")
        print("Select one of the options below:")
        print("r - \tRegistering a user")
        print("a - \tAdding a task")
        print("va - \tView all tasks")
        print("vm - \tView my tasks")
        print("gr - \tGenerate Reports")
        print("ds - \tDisplay Statistics")
        print("e - \tExit")
    
    else:
        print("---------------------------------------------")
        print("Select one of the options below:")
        print("r - \tRegistering a user")
        print("a - \tAdding a task")
        print("va - \tView all tasks")
        print("vm - \tView my tasks")
        print("e - \tExit")

    selected = input(": ")
    return selected

# ------------------------------------------------------------------
# Registering User function
def reg_user():
    while True:
        if logged_user == 'admin':
            new_username = input("Input a new username: ")
            new_password = input("Input a new password: ")
            confirm_pass = input("Please confirm the new password: ")
            if new_password == confirm_pass:
                if new_username != user_lines[0]:
                    with open("user.txt", "a") as new_user:
                        new_user.write(f"\n{new_username}, {new_password}")
                        new_user.close()
                    print("\n---------------------------------------------")
                    print("New user successfully created!")
                    break
                else:
                    print("Sorry. That username already exists. Verify that you've entered the correct information and try again")
            else:
                print("Passwords don't match. Verify that you've entered the correct information and try again.")
        else:
            print("Sorry. You're not authorised to register a new user.")
            break
    

# Adding a Task function
def add_task():
    task_user = input("Insert username of the person whom task is assigned to: ")
    task_title = input("Insert the title of the task: ")
    description = input("Insert a description of the task: ")
    due_date = input("Insert the due date (DD Mmm YYYY): ")
    today = date.today().strftime('%d %b %Y')
    not_complete = "No"
    
    with open("tasks.txt", "a") as new_task:
        new_task.write(f"\n{task_user}, {task_title}, {description}, {due_date}, {today}, {not_complete}")
        new_task.close()

    print("Task added successfully")

# View all tasks function
def view_all():
    with open("tasks.txt", "r") as tasks:
        tasks_data = tasks.readlines()
        
        for task in tasks_data:
            task_lines = task.strip()
            task_lines = task_lines.split(", ")
          
            all_tasks = "---------------------------------------\n"
            all_tasks += f"Task: \t\t\t{task_lines[1]}\n"
            all_tasks += f"Assigned to: \t\t{task_lines[0]}\n"
            all_tasks += f"Date Assigned: \t\t{task_lines[3]}\n"
            all_tasks += f"Due Date: \t\t{task_lines[4]}\n"
            all_tasks += f"Task Complete: \t\t{task_lines[5]}\n"
            all_tasks += f"Task Description: \t{task_lines[2]}\n"
            print(all_tasks)
            tasks.close()

# View my tasks function
def view_mine():
    # Read tasks
    tasks_read = open("tasks.txt", "r")
    data = tasks_read.readlines()

    # Enumerate them
    for pos, line in enumerate(data, start=1):
        task_lines = line.split(", ")

        # Display tasks related to the logged_user with a number
        if logged_user == task_lines[0]:           
            all_tasks = f"-------------Task number: {[pos]}-------------\n"
            all_tasks += f"Task: \t\t\t{task_lines[1]}\n"
            all_tasks += f"Assigned to: \t\t{task_lines[0]}\n"
            all_tasks += f"Date Assigned: \t\t{task_lines[3]}\n"
            all_tasks += f"Due Date: \t\t{task_lines[4]}\n"
            all_tasks += f"Task Complete: \t\t{task_lines[5]}\n"
            all_tasks += f"Task Description: \t{task_lines[2]}\n"
            print(all_tasks)
    
    # Start first loop for the user to select a specific task by its number
    while True:
        task_choice = int(input("Please select a task number or type '-1' to go back to the main menu: ")) - 1

        # If input = -1, then task_choice = -2
        if task_choice == -2:
            break
        
        # Throw error message if invalid number is given
        elif task_choice == 0 or task_choice < -2 or task_choice > len(data):
            print("You have selected an invalid option. Try again.")
            continue

        edit_data = data[task_choice]
        
        # Start second loop that will print another menu and prompt the user to select an action
        while True:
            all_tasks = f"\n-------------[SELECT AN OPTION]--------------\n"
            all_tasks += f"1 - Edit username\n"
            all_tasks += f"2 - Edit due date\n"
            all_tasks += f"3 - Mark as completed\n"
            all_tasks += f"4 - Choose another task\n"
            
            choice = int(input(all_tasks))

            # Check if the user is already registered and change the user to which this task is assinged to
            if choice == 1:
                edited_username = input("Enter username of a person to which this task is assigned to: ")
                if edited_username in accounts.keys():
                    task_lines = edit_data.split(", ")
                    task_lines[0] = edited_username
                    new_data = ", ".join(task_lines)
                    data[task_choice] = new_data
                    print("Task user changed successfully\n")
                # Throw error message otherwise
                else:
                    print("This user is not registered yet. Please add the user first.")

            # Edit new due date
            elif choice == 2:
                edited_due_date = input("Insert a new due date (DD Mmm YYYY): ")
                task_lines = edit_data.split(", ")
                task_lines[-2] = edited_due_date
                new_data = ", ".join(task_lines)
                data[task_choice] = new_data
                print("Due date successfully changed.\n")

            # Mark the task selected as completed
            elif choice == 3:
                task_lines = edit_data.split(", ")
                task_lines[-1] = "Yes\n"
                new_data = ", ".join(task_lines)
                data[task_choice] = new_data

            # Break and return to previous menu
            elif choice == 4:
                break
            
            else:
                print("You have selected an invalid option. Try again.")

            tasks_write = open("tasks.txt", "w")    
            for line in data:
                tasks_write.write(line)
            
            break
        tasks_read.close()
        tasks_write.close()
            

# Generate reports function
def gen_reports():

    # Set counts to zero
    count_complete = 0
    count_uncomplete = 0
    count_overdue = 0

    # open file 'tasks.txt' and prepare data for usage
    with open("tasks.txt", "r") as tasks:
        tasks_data = tasks.readlines()
        for task in tasks_data:
            task_lines = task.strip()
            task_lines = task_lines.split(", ")
            
            # Total number of tasks
            num_tasks = len(tasks_data)
                        
            # Total number of completed and uncompleted tasks
            if task_lines[-1] == "No":
                count_uncomplete += 1
            else:
                count_complete += 1
        
            # Total number of uncomplete and overdue tasks
            due_date = datetime.strptime(task_lines[4], '%d %b %Y')

            if (task_lines[-1] == "No") and ((due_date.date()) < date.today()):
                count_overdue += 1

    # Generate task_overview file
    with open("task_overview.txt", "w") as task_overview:
        task_overview.write(f"Number of tasks: {num_tasks}\n")
        task_overview.write(f"Number of complete tasks: {count_complete}\n")
        task_overview.write(f"Number of uncomplete tasks: {count_uncomplete}\n")
        task_overview.write(f"Number of uncomplete and overdue: {count_overdue}\n")
        task_overview.write(f"Percentage overdue: {round((count_overdue/num_tasks)*100, 2)}%\n")
        task_overview.write(f"Percentage uncomplete: {round((count_uncomplete/num_tasks)*100, 2)}%\n")

    # -----------------------------------------------------------------------------------------------
    # Open file 'user.txt' and prepare data for usage           
    with open("user.txt", "r") as users:
        users_data = users.readlines()
        for user in users_data:
            user_lines = user.strip()
            user_lines = user_lines.split(", ")
            
            num_users = len(users_data)

    # Generate user_overview file
    with open("user_overview.txt", "w+") as user_overview:
        user_overview.write(f"Total number of users registered: {num_users}\n")
        user_overview.write(f"Total number of tasks generated: {num_tasks}\n")
        user_overview.write("----------------------------------------------------------\n")
    
        for key, user in accounts.items():
            user_overview.write(f"User: {key}\n")
            user_overview.write(f"Total number of tasks assigned to this user: {len(get_task_by_user(key))}\n")
            user_overview.write(f"Percentage of tasks assigned to this user: {round(len(get_task_by_user(key)) / (num_tasks) * 100, 2)}%\n")
            
            # ----------------------------------------------------------------
            count_comp = 0
            count_uncomp = 0
            completion = get_completion_by_user(key)

            for i in completion:
                if i == "Yes":
                    count_comp += 1
                else:
                    count_uncomp += 1
            
            total_count = count_comp + count_uncomp
            if total_count == 0:
                user_overview.write(f"Percentage of completed tasks: This user has no tasks assigned to him/her\n")
            else:
                user_overview.write(f"Percentage of completed tasks: {round(((count_comp / total_count) * 100), 2)}%\n")
            
            if total_count == 0:
                user_overview.write(f"Percentage of uncompleted tasks: This user has no tasks assigned to him/her\n")
            else:
                user_overview.write(f"Percentage of uncompleted tasks: {round(((total_count - count_comp) / total_count) * 100, 2)}\n")
            
            # ----------------------------------------------------------------
            overdue = get_overdue_by_user(key)
            if total_count == 0:
                user_overview.write(f"Percentage of uncompleted tasks: This user has no tasks assigned to him/her\n")
            else:
                user_overview.write(f"Percentage of uncompleted and overdue tasks: {round(((overdue/total_count) * 100), 2)}%\n")
            user_overview.write("----------------------------------------------------------\n")

   
# Displaying Statistics function
def display_stats():
    # Display statistics from the new files:
    # task_overview.txt
    # user_overview.txt
    if logged_user == "admin":
        with open("tasks.txt", "r") as task_stats, open("user.txt", "r") as user_stats:
        # Count the length of users and tasks and print them
            num_users = len(user_stats.readlines())
            num_tasks = len(task_stats.readlines())
            print(f"Total Number of Users: {num_users}")
            print(f"Total Number of Tasks: {num_tasks}")
            task_stats.close()
            user_stats.close()


# While loop to present menu and user's selection
while True:
    # Prompt user input
    logged_user = input("Enter login: ").lower()
    password_input = input("Enter password: ").lower()     

    # Check login and password inputs
    if logged_user in accounts.keys():
        if password_input == accounts[logged_user]:
            if logged_user == "admin":
                print("\nSuccessful login...")
                print(f"Hi, {logged_user}!")

            else:
                print("\nSuccessful login...")
                print(f"Hi, {logged_user}!")

            while True:
            # Displays menu according to logged user (either admin or else)
                selection = menu(logged_user)
                    
                # Executes the specific function based on the user's menu selection
                if selection == 'r':
                    reg_user()
                elif selection == 'a':
                    add_task()
                elif selection == 'va':
                    view_all()
                elif selection == 'vm':
                    view_mine()               
                elif selection == 'gr':
                    gen_reports()
                elif selection == 'ds':
                    display_stats()
                elif selection == 'e':
                    print("Good Bye!!!")
                    exit()  
                else:
                    print("This option doesn't exist")
            
        # If password doesn't match throw error message
        else:
            print("Password is incorrect")

    # If username doesn't match throw error message
    else: 
        print("Username is incorrect")



