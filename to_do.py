to_do_list=[]
print(to_do_list)
while True:
    ask = input("Type add,show,edit,complete or exit: ")
    match ask:
        case "add":
            task=input("add " )
            to_do_list.append(task)
        case "show":
            for item in to_do_list:
                print(item.capitalize())
        case "edit":
            number=int(input("Which item number do you want to replace?"))
            number=number-1
            new_todo=input("Please add new task: ")
            to_do_list[number]=new_todo

        case "exit":
            break
        case wrong_prompt:
            print("Invalid prompt")



