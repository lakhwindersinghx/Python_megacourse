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
    # elif ask=="complete":
    #     completed_task=
    #     to_do_list.pop()
        case "exit":
            break
        case wrong_prompt:
            print("Invalid prompt")



