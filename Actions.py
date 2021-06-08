from Tail import Tail
from Legs import Legs
from Claws import Claws
from Eyes import Eyes
from Lights import Lights
from Voice import Voice
from Screen import Screen

class Actions:

    def __init__(self, ev3):
        self.ev3 = ev3
        self.tail = Tail()
        self.legs = Legs()
        self.eyes = Eyes()
        self.claws = Claws()
        self.lights = Lights(self.ev3)
        self.voice = Voice(self.ev3)
        self.screen = Screen(self.ev3)


    def attack(self):
        self.screen.clear()
        self.screen.output("ATTACK")
        self.lights.turn_red()
        self.tail.shoot()

    def walk(self):
        self.screen.clear()
        self.screen.output("WALK")
        self.lights.turn_yellow()
        self.legs.walk()

    def detect_and_shoot_beacon(self):
        self.screen.clear()
        self.screen.output("DETECT")
        self.eyes.process_stimuli(self.tail.shoot)

    def walk_and_shoot(self):
        self.screen.clear()
        self.screen.output("WALK AND ATTACK")
        self.legs.walk()
        self.tail.shoot()

    def conversation(self):
        self.screen.clear()
        self.screen.output("CONVERSATION")
        self.claws.move_claws()
        self.lights.turn_green()
        self.voice.talk()