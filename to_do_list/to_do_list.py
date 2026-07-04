import json

tasks = []
try:
    with open("abc.json", "r") as f:
        tasks = json.load(f)
except:
    tasks = []
while True:
    user_choice = int(input("1.add\n2.view\n3.markdone\n4.quit\n"))
    match user_choice:
        case 1:
            task1 = input("what is the task:")
            tasks.append(task1)
            with open("abc.json", "w") as f:
                json.dump(tasks, f)
        case 2:
            for i, task in enumerate(tasks, start = 1):
                print(f"{i}.{task}")
        case 3:
            for i, task in enumerate(tasks, start = 1):
                print(f"{i}.{task}")
            try:
                task2 = int(input("which index to mark done?"))
                tasks.pop(task2-1)
                print("done!")
            except:
                print("error!")
            with open("abc.json", "w") as f:
                json.dump(tasks, f)
        case 4:
            print("bye!")
            break
            

