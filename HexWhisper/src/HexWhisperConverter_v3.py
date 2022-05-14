import PySimpleGUI as sg
import pyperclip

NAME = "HexWhisperConverter_v3"
THEME = 'SystemDefaultForReal'

sg.theme(THEME)


def convert():
    val = list("%s" % ({values["-before-"]}))

    for index, item in enumerate(val):
        if 'G' in item:
            val[index] = "6"
        if 'H' in item:
            val[index] = "8"
        if 'I' in item:
            val[index] = "1"
        if 'J' in item:
            val[index] = "7"
        if 'K' in item:
            val[index] = "C"
        if 'L' in item:
            val[index] = "1"
        if 'M' in item:
            val[index] = "3"
        if 'N' in item:
            val[index] = "2"
        if 'O' in item:
            val[index] = "0"
        if 'P' in item:
            val[index] = "10"
        if 'Q' in item:
            val[index] = "9"
        if 'R' in item:
            val[index] = "8"
        if 'S' in item:
            val[index] = "5"
        if 'T' in item:
            val[index] = "7"
        if 'U' in item:
            val[index] = "4"
        if 'V' in item:
            val[index] = "11"
        if 'W' in item:
            val[index] = "3"
        if 'X' in item:
            val[index] = "8"
        if 'Y' in item:
            val[index] = "F"
        if 'Z' in item:
            val[index] = "2"
        if 'a' in item:
            val[index] = "A"
        if 'b' in item:
            val[index] = "B"
        if 'c' in item:
            val[index] = "C"
        if 'd' in item:
            val[index] = "D"
        if 'e' in item:
            val[index] = "E"
        if 'f' in item:
            val[index] = "F"
        if 'g' in item:
            val[index] = "6"
        if 'h' in item:
            val[index] = "8"
        if 'i' in item:
            val[index] = "1"
        if 'j' in item:
            val[index] = "7"
        if 'k' in item:
            val[index] = "C"
        if 'l' in item:
            val[index] = "1"
        if 'm' in item:
            val[index] = "3"
        if 'n' in item:
            val[index] = "2"
        if 'o' in item:
            val[index] = "0"
        if 'p' in item:
            val[index] = "10"
        if 'q' in item:
            val[index] = "9"
        if 'r' in item:
            val[index] = "8"
        if 's' in item:
            val[index] = "5"
        if 't' in item:
            val[index] = "7"
        if 'u' in item:
            val[index] = "4"
        if 'v' in item:
            val[index] = "11"
        if 'w' in item:
            val[index] = "3"
        if 'x' in item:
            val[index] = "8"
        if 'y' in item:
            val[index] = "F"
        if 'z' in item:
            val[index] = "2"
        if "'" in item:
            val[index] = ""
        if "{" in item:
            val[index] = ""
        if "}" in item:
            val[index] = ""

    values["-After-"] = "".join(val)


layout = [[sg.Text("Input"), sg.Input(key="-before-")],
          [sg.Button("Convert"), sg.Checkbox('Copy'), sg.Button("Close")],
          [sg.Text('Output'), sg.Text(key="-After-")]]

window = sg.Window(NAME, layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Close":
        break
    if event == "Convert":
        convert()
        window["-After-"].update(f'0x{values["-After-"]}')
        # print(f'{values}')
        if values[0]:
            pyperclip.copy(values["-After-"])


window.close()
