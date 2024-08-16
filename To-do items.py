tasks = []

def addTask():
        task = input("Please enter a task: " )
        tasks.append(task)
        print(f"Task'{task}' added to the list. ")

def listTasks():
    if not tasks:
        print("There are no tasks currently. ")
    else: 
        print("Current Tasks: ")
        for index, task in enumerate(tasks):
             print(f"Task #{index}. {task}")


def deletetask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the * to delete:"))
        if taskToDelete >= 0 and taskToDelete < len(task):
             task.pop (taskToDelete)
             print(f"task{ taskToDelete} has been removed.")
 
    except: 
     print(" Invalid input ")

if __name__ == "__main__":

    print("Welcome to do list app :) ")

    while True:
            print("/n")
            print("Please one select onne to the following option")
            print("***********")
            print("1. Add new task")
            print("2. Delete a the task")
            print("3. List this task")
            print("4. Quit")

            choice = input("Enter your choice: ")
            
            if (choice == "1"):
                 addTask()
            elif (choice == "2"):   
                 deletetask()
            elif (choice == "3"):
                 listTasks()
            elif (choice == "4"):
                break
            else:
                print(" Invalid input. Please try again. ")
    print( " GOOD BYE *_- ")       





