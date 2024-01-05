to_do_list=[]
print(to_do_list)
while True:
    ask = input("Type add,show,edit,complete or exit: ")
    match ask:
        case "add":
            task=input("add " )+"\n"
            to_do_list.append(task)
            file=open('to_do_list.txt','a') #file opened in append mode 'a' preserves old data aka doesnt overwrite
            file.writelines(to_do_list)
            file.close()

        case "show":
            file = open('to_do_list.txt', 'r')
            to_do_list=file.readlines()

            for index,item in enumerate(to_do_list):
                print(f"{index+1}-{item.capitalize()}")


        case "edit":
            edit_number=int(input("Which task number do you want to replace?"))
            edit_number=edit_number-1
            new_todo=input("Please add new task: ")
            to_do_list[edit_number]=new_todo

        case "complete":
            complete_number=int(input("Which task number have you completed?"))
            complete_number=complete_number-1
            completed_task=to_do_list.pop(complete_number)

        case "exit":
            break

        case wrong_prompt:
            print("Invalid prompt")



