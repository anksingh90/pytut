def add_task():
    try:
       f=open('tasks.txt','a')
       task = input('Enter your task : ')
       f.write(task+'\n')
       f.close()
    except FileNotFoundError:
        print("No tasks.txt file found !")

def view_task():
    f=open('tasks.txt','r')
    data=f.readlines()
    for i in range(len(data)):
        print(f"{i+1}.{data[i]}")
    f.close()

def edit_task():
    view_task()
    f=open('tasks.txt','a')
    f.read()

def menu():
    print("---TASK MANAGER MENU---")
    while True:
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Edit A Task")
        print("4. Exit")
        ch=input("enter your choice :")
        if ch=='1':
            add_task()
        elif ch=='2':
            view_task()
        elif ch=='3':
            edit_task()
        elif ch=='4':
            print('Exiting your program!')
            break

menu()