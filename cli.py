import function
import time

now = time.strftime("%d-%m-%y %H:%M:%S")
print("It is", now)
while True:
    a = input("enter add,exit,complete,edit or show:")
    a = a.strip()

    if a.startswith("add"):
        todo = a[4:]

        todos = function.get_todo()

        todos.append(todo + "\n")



        function.write_todo(todos)


    elif a.startswith("show"):
        todos = function.get_todo()

        for index,items in enumerate(todos):
            items = items.strip("\n")
            b = f"{index + 1}-{items}"
            print(b)


    elif  a.startswith("edit"):
        try:
            number = int(a[5:])
            print(number)
            number = number -1
            todos = function.get_todo()

            new_todo = input("enter new todo:")
            todos[number] = new_todo + "\n"

            function.write_todo(todos)

        except ValueError:
            print("command is invalid")
            continue


    elif a.startswith("complete"):
        try:
            number = int(a[9:])
            todos = function.get_todo()


            number = number - 1
            removed_todo = todos[number].strip('\n')
            todos.pop(number)

            function.write_todo(todos)
            message = f"Todo {removed_todo} was removed"
            print(message)

        except IndexError:
            print("there is no item with this number")
            continue

    elif a.startswith("exit"):
        break

    else:
        print("invalid command")

print("bye!!!")