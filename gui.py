import FreeSimpleGUI as si
import function
import time




si.theme("black")
time_label = si.Text('', key="clock")
label = si.Text("Type a to-do")
input_box = si.InputText(tooltip="Enter todo", key='todo')
add_button = si.Button("Add")
list_box = si.Listbox(values=function.get_todo(), key='todos', enable_events=True, size=[45, 10])
edit_button = si.Button("Edit")
complete_button = si.Button("Complete")
Exit_button = si.Button("Exit")

window = si.Window('My To-Do App', layout=[[time_label],
                                            [label] ,
                                               [input_box,add_button ],
                                               [list_box, edit_button,complete_button],
                                               [Exit_button]], font=('Helvetica', 17))

while True:
    event, values = window.read(timeout=200)

    if event in (si.WIN_CLOSED, "Exit"):
        break

    window["clock"].update(value= time.strftime("%d-%m-%y %H:%M:%S"))

    match event:
        case "Add":
            todos = function.get_todo()
            new_todo1 = values['todo'] + "\n"
            todos.append(new_todo1)
            function.write_todo(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = function.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function.write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value = '')
            except IndexError:
                si.popup("please select an item" , font=("Helbvetica", 17))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = function.get_todo()
                todos.remove(todo_to_complete)
                function.write_todo(todos)
                window['todos'].update(values = todos)
                window['todo'].update(value = '')

            except IndexError:
                si.popup("please select an item", font=("Helbvetica", 17))


        case 'todos':
            window['todo'].update(value=values['todos'][0])



window.close()
