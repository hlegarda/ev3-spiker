class Screen:
    
    def __init__(self, ev3):
        self.ev3 = ev3

    def output(self, text):
        self.ev3.screen.draw_text(2, 100, text)

    def clear(self):
        self.ev3.screen.clear()