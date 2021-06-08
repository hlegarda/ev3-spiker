class Voice:
    def __init__(self, ev3):
        self.ev3 = ev3

    def talk(self):
        voice = self.ev3.speaker
        voice.set_volume(100)
        voice.set_speech_options("en", "f1", 110, 80)
        voice.say("Saying things")