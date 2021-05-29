from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop

class Tail:
    tail_motor = Motor(Port.D)

    def shoot(self):
        self.tail_motor.run_time(1800, 900, Stop.COAST, True)
        self.tail_motor.run_angle(720, -220, Stop.BRAKE, True)
        self.tail_motor.run_time(-720, 800, Stop.COAST, True)
