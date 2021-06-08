from pybricks.ev3devices import InfraredSensor
from pybricks.parameters import Button, Port
from pybricks.tools import wait
from Actions import Actions
from Legs import Legs

class RemoteController:

    def __init__(self, ev3):
        self.ev3 = ev3
        self.legs = Legs()
        self.eyes_sensor = InfraredSensor(Port.S4)


    def remote_control(self):
        self.ev3.screen.print("RC Mode")
        wait(1000)
        last_pressed = None
        actions = Actions(self.ev3)
        while True:
            buttons = self.eyes_sensor.keypad()
            self.ev3.screen.clear()
            self.ev3.screen.print(buttons)
            
            if not buttons:
                self.legs.stop()
                last_pressed = None
            
            for button in buttons:
                if button == Button.BEACON.LEFT_UP and last_pressed != Button.BEACON.LEFT_UP:
                    self.legs.walk_forward()
                    last_pressed = Button.BEACON.LEFT_UP
            
                if button == Button.BEACON.LEFT_DOWN and last_pressed != Button.BEACON.LEFT_DOWN:
                    self.legs.walk_backwards()
                    last_pressed = Button.BEACON.LEFT_DOWN

                if button == Button.BEACON.RIGHT_UP and last_pressed != Button.BEACON.RIGHT_UP:
                    actions.attack()
                    last_pressed = Button.BEACON.RIGHT_UP

            wait(150)
            

