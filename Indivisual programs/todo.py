import json, sys, os , datetime
from pyperclip import copy
#created 21/10/24
#testing data
"""
[
    {
        "id": 123,
        "description": "some description about task",
        "status": "todo",
        "created at": 2,
        "updated at": 2
    },
    {
        "id": 23,
        "description": "some another description",
        "status": "in progress",
        "created at": 3,
        "updated at": 1
    }
]
"""

copy(f"py '{os.path.realpath(__file__)} '") # copies the abs filepath of this file to clipboard
#loading database
def readdb() -> list:
    if not "todo" in os.listdir(os.getcwd()): os.mkdir("todo")
    if not os.path.exists("todo\\tododb.json"):
        with open("todo\\tododb.json" , mode="w", newline="", encoding="utf-8") as file:
            json.dump([], file)

    with open("todo\\tododb.json", newline="", mode="r") as file:
        return json.load(file)
def updatedb(data : list) -> None:
    with open("todo\\tododb.json", newline="",mode="w") as file:
        json.dump(data, file)

#main functions

"""
general syntax : py <abs/rel filepath> add | list | delete  *[args]
# ~add task -> adds a new task
# ~list all | done | todo | inprogress
# ~update id-[done | todo | inprogress]

-> To use , in cmd -> py <path> <commands>  

"""

#tasks add task
def add(data : list):
    id : str = str(len(data) + 1)
    #name = input("Task name : ")
    description : str = input("Task description : ")
    datecreated : str = str(datetime.datetime.now())
    dateupdated : str = str(datetime.datetime.now())
    data.append({
        "id": id,
        #"name": name,
        "description" : description,
        "status" : "todo", #assuming to-do to be default status
        "created" : datecreated,
        "updated" : dateupdated
    })
    return updatedb(data)

#tasks list all | inprogress | to-do | done
def listt(data : list, arg):
    if arg not in ["all", "done","todo","inprogress"]:
        print("Invalid list arg ", arg)
    else:
        match arg:
            case "all":
                print("All tasks :")
                for i, task in enumerate(data):
                    print(f"""
                                {i}-------------------------
                                id : {task["id"]}
                                description : {task["description"]}
                                status : {task["status"]}
                                created at : {task["created"]}
                                updated at : {task["updated"]}
                                """)
            case "done":
                print("Tasks with DONE status :")
                for i, task in enumerate(data):
                    if task["status"] == "done":
                        print(f"""
                                {i}-------------------------
                                id : {task["id"]}
                                description : {task["description"]}
                                created at : {task["created"]}
                                updated at : {task["updated"]}
                                """)
            case "todo":
                print("Tasks with TODO status :")
                for i, task in enumerate(data):
                    if task["status"] == "todo":
                        print(f"""
                                {i}-------------------------
                                id : {task["id"]}
                                description : {task["description"]}
                                created at : {task["created"]}
                                updated at : {task["updated"]}
                                """)
            case "inprogress":
                print("Tasks with in progress status :")
                for i, task in enumerate(data):
                    if task["status"] == "inprogress":
                        print(f"""
                                {i}-------------------------
                                id : {task["id"]}
                                description : {task["description"]}
                                created at : {task["created"]}
                                updated at : {task["updated"]}
                                """)
            case _:print("Invalid")

#update tasks
#tasks update <id> <status>
def update(data : list, arg : str):
    id , arg = arg.split("-")
    if arg not in ["done","todo","inprogress"]:
        return print("Invalid arg : " , arg)

    for task in data:
        if task["id"]==id:
            task["status"] = arg
            task["updated"] = str(datetime.datetime.now())
            print(f"Updated task w/ id {id}'s status to {arg}")
    return updatedb(data)

#tasks delete <id>
def deletet(data, id):
    for task in data:
        if task["id"]==id:
            print(f"Deleted task {task["description"]}")
            data.pop(data.index(task))
            return updatedb(data)
    return print(f"No task found with id {id}")
def main():
    try :
        cliargs = sys.argv[1:] #skipping the first item of filename
        if len(cliargs) == 2:
            action = cliargs[0]
            arg = cliargs[1]
            tasks = readdb()
            # logic
            match action:
                case "add":
                    add(tasks)
                case "list":
                    listt(tasks, arg)
                case "update":
                    update(tasks, arg)

        elif len(cliargs) < 2:
            print("Missing args \n Use syntax > tasks add | list | delete  [args]")

        else:
            print(f"Extra arguments given {cliargs[2:]} \n #use quotes while passing arguements with spaces ")

    except KeyboardInterrupt:
        exit("bye")
    except TypeError:
        pass #:)

if __name__=="__main__":
    main()


