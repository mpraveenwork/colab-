import PySimpleGUI as sg

# From here we are creating number of columns for our GUI
layout = [
    [sg.Text('text')],
    [sg.Button('Button')],
    [sg.Input()]
]
# From hear tha GUI is running
sg.Window("title",layout).read()

