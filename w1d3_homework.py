tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

#Task1
def uncompleted_tasks(list, status):
    var1 = []
    for task in list:
        if task["completed"] == status:
            var1.append(task)
    return var1

var_1 = uncompleted_tasks(tasks,False)
print(var_1)

#Task2
def completed_tasks(list, status):
    var2 = []
    for task in list:
        if task["completed"] == status:
            var2.append(task)
    return var2

var_2 = completed_tasks(tasks, True)
print(var_2)

#Task3
def print_descriptions_list(list):
    var3 = []
    for task in list:
        var3.append(task["description"])
    return var3

var_3 = print_descriptions_list(tasks)
print(var_3)

#Task4
def time_taken(list, task_time):
    var4 =[]
    for task in list:
        if task["time_taken"]>= task_time:
            var4.append(task)
    return var4

var_4 = time_taken(tasks, 15)
print(var_4)

#Task5

def specific_task_description(desc, list):
    for task in list:
        if task["description"] == desc:
            return task
    return "Task not found"


var_5 = specific_task_description("Sing!",tasks)
print(var_5)


#Task6

def make_complete(desc, list):
    for task in list:
        if task["description"] == desc:
            task["completed"] = True
    return tasks

var_6 = make_complete("Feed Cat",tasks)
print(var_6)


#Task7

def add_task(list, description,completed,time_taken):
    new_list ={}
    new_list["description"] = description
    new_list["completed"] = completed
    new_list["time_taken"] = time_taken
    list.append(new_list)
    return list

var_7 = add_task(tasks,"Clean Kitchen",True, 18)


print(var_7)

    
