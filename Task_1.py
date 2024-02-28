tasks=[]

def addlist():
    task = input ("Please enter a task: ")
    tasks.append(task)

def listAll():
    if not tasks:
        print ("There are no tasks.")
    else:
        print ("Here are the tasks:")
        for index, task in enumerate(tasks):
            print (f"Task #{index}. {task}")

def deletelist():
    listTasks()
    try:
        tasktodelete = int (input ("Please enter the number to delete:"))
        if tasktodelete > len (tasks):
            tasks.pop(tasktodelete)
        else:
            print("Task not found")
    except:
        print("Invalid input")

if __name__=="__main__":
    print ("Welcome to the app")
    while True:
        print ("/n")
        print ("Please select one option")
        print ("1. Add a new task")
        print ("2. Delete a task")
        print ("3. List all the tasks")
        print ("4. Close")

        choice = input ("Enter your choice:")

        if (choice == "1"):
            addlist()
        elif (choice == "2"):
            deletelist()
        elif (choice == "3"):
            listAll()
        elif (choice == "4"):
            break
        else:
            print ("Invalid input")