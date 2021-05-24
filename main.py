#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop

# Initialize the EV3 Brick.
ev3 = EV3Brick()

def walk():
    legs_motor = Motor(Port.B)
    legs_motor.run_angle(720, 2160, Stop.BRAKE, True)
    legs_motor.run_angle(720, -720, Stop.BRAKE, True)
    legs_motor.run_angle(720, 360, Stop.BRAKE, True)


def shoot():
    tail_motor = Motor(Port.D)
    tail_motor.run_time(1800, 900, Stop.COAST, True)
    tail_motor.run_angle(720, -220, Stop.BRAKE, True)
    tail_motor.run_time(-720, 800, Stop.COAST, True)

walk()
shoot()