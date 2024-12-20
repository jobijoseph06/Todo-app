def get_todo(filepath="todo.txt"):
    with open(filepath, 'r') as todo_locals:
        todo_local = todo_locals.readlines()
    return todo_local

def write_todo(todo_arg, filepath="todo.txt"):
    with open(filepath, "w") as file:
        file.writelines(todo_arg)