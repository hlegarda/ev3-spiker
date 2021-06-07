from Tail import Tail
from Legs import Legs
from Eyes import Eyes
from Lights import Lights
from Voice import Voice
from Screen import Screen

class Actions:
    tail = Tail()
    legs = Legs()
    eyes = Eyes()
    lights = Lights()
    voice = Voice()
    screen = Screen()

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
        self.lights.turn_green()
        self.voice.talk()