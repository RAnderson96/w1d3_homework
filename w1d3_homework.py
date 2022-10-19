tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

#Task1
var1 = []
for task in tasks:
    if task["completed"] == False:
        var1.append(task)
print(f"#Task 1 is {var1}")

#Task2
var2 = []
for task in tasks:
    if task["completed"] == True:
        var2.append(task)
print(f"#Task2 is {var2}")

#Task3
var3 = []
for task in tasks:
    var3.append(task["description"])
print(f"#Task3 is {var3}")

#Task4 
var4 =[]
time = 15 #time for task
for task in tasks:
    if task["time_taken"]<= time:

        var4.append(task)
print(f"#Task4 the activities that last at least {time} are {var4}")

#Task 5

var_description = "Clean Windows"
var_to_print = None
for task in tasks:
    if task["description"] == var_description:
        var_to_print = task

print(f"#Task5 is {var_to_print}")

#Task 6

var_description = "Clean Windows"
var_to_print = None
for task in tasks:
    if task["description"] == var_description:
        task["completed"] = True

print(f"#Task6 answer has changed result for {var_description} to True, see: {tasks}")

#Task 7

new_task = {
    "description" : "clean kitchen",
    "completed" : True,
    "time_taken" : 20
}

tasks.append(new_task)

print(f"#Task7 The new list is {tasks}")
print(f"#Task7 the new dict is {tasks[-1]}")


