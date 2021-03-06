from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from Actions import Actions
from RemoteController import RemoteController

class Menu:
    ev3 = EV3Brick()

    def handle_button_press(self):

        actions = Actions(self.ev3)
        remote = RemoteController(self.ev3)

        button = self.wait_for_button()

        if button == Button.LEFT:
            actions.attack()
        elif button == Button.RIGHT:
            actions.walk()
        elif button == Button.UP:
            actions.conversation()
        elif button == Button.DOWN:
            actions.detect_and_shoot_beacon()
        elif button == Button.CENTER:
            remote.remote_control()


    def wait_for_button(self):
        self.ev3.screen.load_image('buttons.png')

        pressed = []
        while len(pressed) != 1:
            pressed = self.ev3.buttons.pressed()
        button = pressed[0]

        while any(self.ev3.buttons.pressed()):
            pass

        return button

