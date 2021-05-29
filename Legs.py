from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop

class Legs:
    legs_motor = Motor(Port.B)

    def walk(self):
        self.legs_motor.run_angle(720, 2160, Stop.BRAKE, True)
        self.legs_motor.run_angle(720, -720, Stop.BRAKE, True)
        self.legs_motor.run_angle(720, 360, Stop.BRAKE, True)