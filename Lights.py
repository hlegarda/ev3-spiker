from pybricks.parameters import Color

class Lights:

    def __init__(self, ev3):
        self.ev3 = ev3

    def turn_green(self):
        self.ev3.light.on(Color.GREEN)

    def turn_yellow(self):
        self.ev3.light.on(Color.YELLOW)

    def turn_red(self):
        self.ev3.light.on(Color.RED)