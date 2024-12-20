import FreeSimpleGUI as si
import function


label = si.Text("Type a to-do")
input_box = si.InputText(tooltip="Enter todo", key='todo')
add_button = si.Button("Add")


window = si.Window('My To-Do App', layout=[[label], [input_box,add_button ]], font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = function.get_todo()
            new_todo1 = values['todo'] + "\n"
            todos.append(new_todo1)
            function.write_todo(todos)
        case si.WINDOW_CLOSED:
            break

window.close()
