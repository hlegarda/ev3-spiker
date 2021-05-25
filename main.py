#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.parameters import Port, Stop, Color
from pybricks.tools import wait

import itertools

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

def move_claws():
    claswMotor = Motor(Port.A)
    #TODO calibrate
    #claswMotor.run_angle(720, 90, Stop.BRAKE, True)
    #claswMotor.run_angle(720, -90, Stop.BRAKE, True)
    claswMotor.run_until_stalled(720, Stop.BRAKE, 50)
    claswMotor.run_until_stalled(-720, Stop.BRAKE, 50)

def repeat(f, N):
    for _ in itertools.repeat(None, N): f()

def checkDistance(eyes):
    bugLocation = eyes.beacon(4)
    bugDistance = bugLocation[0]
    # bugAngle = bugLocation[1]
    if bugDistance is None:
        return 100

    return bugDistance

def execute_when_object_is_near(func):
    ev3.light.on(Color.RED)

    eyes = InfraredSensor(Port.S4)
    bugDistance = 100

    while bugDistance > 50:
        wait(10)
        bugDistance = checkDistance(eyes)
        

    #func()
    voice = ev3.speaker
    voice.set_volume(100)
    voice.set_speech_options("es", "f1", 110, 80)
    voice.say("como chingas]")

while True:
    execute_when_object_is_near(shoot)