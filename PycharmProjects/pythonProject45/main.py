import PySimpleGUI as sg
import morse as m
import pygame
import time

TIME_BETWEEN = 0.5
PATH = "sounds/"

sg.theme('DarkAmber')

layout = [[sg.Text('Some text on Row 1')],
          [sg.Text('Enter something on Row 2'), sg.InputText()],
          [sg.Text('', key='RESULT')],
          [sg.Text(key='RESULT1')],
          [sg.Button('Encode'), sg.Button('Decode')]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Encode":
        result, flag = m.text_To_Morse(values[0])
    else:
        result, flag = m.morse_To_Text(values[0])

    if not flag:
        break

    window['RESULT'].update(value=result)

    pygame.init()

    if event == "Encode":
        for char in values[0]:
            if char == " ":
                time.sleep(5 * TIME_BETWEEN)
            else:
                pygame.mixer.music.load(PATH + char + '_morse_code.ogg')
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play()
                time.sleep(3 * TIME_BETWEEN)

window.close()
