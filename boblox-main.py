from pynput.mouse import Controller, Button
mouse = Controller()

mouse.position  = 290, 524
mouse.click(Button.left, 2)