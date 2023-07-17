FILEPATH = 'todos.txt'

# gather items for todo_list
def get_todos(filepath=FILEPATH):
    """ Return todo list """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

# write items to the todo list
def write_todos(todos, filepath=FILEPATH):
    """ Writes todo to todo list """
    with open(filepath, "w") as file:
        file.writelines(todos)

if __name__ == "__main__":
    print('Hello from functions')