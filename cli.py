prompt = "Type add, show, edit, complete or exit:"
import functions
import time

now = time.strftime('%m/%d/%y %H:%M')
print(f"It is {now}")

while True:
    # get user input
    user_action = input(prompt)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        # add item to todo list
        todo = user_action[4:]

        todo_list = functions.get_todos('todos.txt')

        todo_list.append(todo + '\n')

        functions.write_todos(todo_list)


    elif user_action.startswith("show"):
        # display items in todo list
        todo_list = functions.get_todos('todos.txt')

        for index, i in enumerate(todo_list):
            i = i.strip("\n")
            row = (f"{index + 1}-{i}")
            print(row)

    elif user_action.startswith("edit"):
        # edit items in a the todo list
        try:
            number = int(user_action[5:])
            number -= 1

            todo_list = functions.get_todos('todos.txt')

            todo = input("Enter new todo: ")
            todo_list[number] = todo + '\n'

            functions.write_todos(todo_list)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        # complete an item in the todo list
        try:
            number = int(user_action[9:])

            todo_list = functions.get_todos('todos.txt')

            index = number - 1
            todo_to_remove = todo_list[index].strip('\n')
            todo_list.pop(number - 1)

            functions.write_todos(todo_list)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        # exit the application
        print("Bye")
        break

    else:
        print("Command is not valid")

