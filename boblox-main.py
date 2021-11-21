from pyautogui import sleep
from pynput.mouse import Controller, Button
mouse = Controller()
while True:
    #abre teclado tactil
    mouse.position = 1227, 751
    mouse.click(Button.left, 1)
    sleep(1)

     #abre teclado tactil
    mouse.position = 1227, 751
    mouse.click(Button.left, 1)
    sleep(1)

     #abre teclado tactil
    mouse.position = 1227, 751
    mouse.click(Button.left, 1)
    sleep(1)

    #presiona 2 veces "w"
    mouse.position = 290, 524
    mouse.click(Button.left, 2)
    sleep(1)

    #presiona 2 veces "a"
    mouse.position = 295, 580
    mouse.click(Button.left, 2)
    sleep(1)

    #presiona 2 veces "s"
    mouse.position = 344, 596
    mouse.click(Button.left, 2)
    sleep(1)

    #presiona 2 veces "d"
    mouse.position = 420, 594
    mouse.click(Button.left, 2)
    sleep(1)

    #Cierra el teclado
    mouse.position = 1098, 475
    mouse.click(Button.left, 1)
    sleep(30)