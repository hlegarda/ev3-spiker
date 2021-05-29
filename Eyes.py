from pybricks.ev3devices import InfraredSensor
from pybricks.parameters import Port
from pybricks.tools import wait

class Eyes:
    eyes_sensor = InfraredSensor(Port.S4)

    def process_stimuli(self, func):
        bug_distance = 100

        while bug_distance > 50:
            wait(10)
            bug_distance = self.check_bug_distance()

        func()

    
    def check_bug_distance(self):
        bug_location = self.eyes_sensor.beacon(4)
        bug_distance = bug_location[0]
        # bugAngle = bugLocation[1]
        if bug_distance is None:
            return 100

        return bug_distance