from pybricks.hubs import EV3Brick

class Voice:
    ev3 = EV3Brick()

    def talk(self):
        voice = self.ev3.speaker
        voice.set_volume(100)
        voice.set_speech_options("en", "f1", 110, 80)
        voice.say("Saying things")