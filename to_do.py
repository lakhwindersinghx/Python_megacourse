to_do_list=[]
while True:
    ask = input("Type add, show, edit, complete or exit: ")

    match ask:
        case "add":
            task = input("Add: ") + "\n"
            task_title = task.title()
            to_do_list.append(task_title)
            with open('to_do_list.txt', 'w') as file:
                file.writelines(to_do_list)

        case "show":
            with open('to_do_list.txt', 'r') as file:
                to_do_list = file.readlines()
            for index, item in enumerate(to_do_list):
                item = item.strip("\n")
                print(f"{index + 1}-{item.capitalize()}")

        case "edit":
            edit_number = int(input("Which task number do you want to replace?"))
            edit_number = edit_number - 1
            with open('to_do_list.txt', 'r') as file:
                to_do_list = file.readlines()
            new_todo = input("Please add new task: ") + "\n"
            to_do_list[edit_number] = new_todo
            with open('to_do_list.txt', 'w') as file:
                file.writelines(to_do_list)

        case "complete":
            complete_number = int(input("Which task number have you completed? "))
            complete_number = complete_number - 1

            with open('to_do_list.txt', 'r') as file:
                to_do_list = file.readlines()
                removed_task=to_do_list[complete_number]
            print(f"Task number:{to_do_list.index(removed_task)}-{removed_task}has been removed from the list")
            completed_task = to_do_list.pop(complete_number)
            with open('to_do_list.txt', 'w') as file:
                file.writelines(to_do_list)
        case "exit":
            break

        case _:
            print("Invalid prompt")