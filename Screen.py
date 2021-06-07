
from pybricks.hubs import EV3Brick

class Screen:
    
    ev3 = EV3Brick()

    def output(self, text):
        self.ev3.screen.draw_text(2, 100, text)

    def clear(self):
        self.ev3.screen.clear()