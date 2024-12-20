import FreeSimpleGUI as si

label = si.Text("Type a to-do")
input_box = si.InputText(tooltip="Enter todo")
add_button = si.Button("Add")

window = si.Window('My To-Do App', layout=[[label], [input_box,add_button ]])
window.read()
window.close()
