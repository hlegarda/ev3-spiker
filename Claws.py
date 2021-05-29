from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop

class Claws:
    claws_motor = Motor(Port.A)

    def move_claws(self):
        #TODO calibrate
        #claswMotor.run_angle(720, 90, Stop.BRAKE, True)
        #claswMotor.run_angle(720, -90, Stop.BRAKE, True)
        self.claws_motor.run_until_stalled(720, Stop.BRAKE, 50)
        self.claws_motor.run_until_stalled(-720, Stop.BRAKE, 50)