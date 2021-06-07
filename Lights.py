from pybricks.hubs import EV3Brick
from pybricks.parameters import Color

class Lights:
    ev3 = EV3Brick()

    def turn_green(self):
        self.ev3.light.on(Color.GREEN)

    def turn_yellow(self):
        self.ev3.light.on(Color.YELLOW)

    def turn_red(self):
        self.ev3.light.on(Color.RED)