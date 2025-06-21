def read_task():
    try:
        with open('task.txt', 'r') as file:
            tasks = [] # list to append data from file
            for i in file:
                tasks.append(i.strip()) # removing whitespace
            
        count = 1
        print('****  Tasks found the file  **** ')
        for task in tasks:
            print(count,'\t',end='')
            for i in task.split():
                print(i+'\t',end='')
            print('')
            count = count + 1
    except:
        print(" No tasks to read.")

def edit_task():
    read_task() # printing list
    try:
        with open('task.txt', 'r') as file:
            tasks = []
            for i in file:
                tasks.append(i.strip())

        edit_lst = int(input("Enter the task number to edit: "))
        new_task = input("Enter the new content: ").strip()
        tasks[edit_lst - 1] = new_task

        # writing changes into file
        with open('task.txt', 'w') as file:
            for task in tasks:
                file.write(task + '\n')
            print("Task updated successfully.")
        read_task() # printing updated list
    except Exception as e:
        print('Error : ',e)

edit_task()
