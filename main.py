#!/usr/bin/env pybricks-micropython

from Eyes import Eyes
from Tail import Tail

import itertools

def repeat(f, N):
    for _ in itertools.repeat(None, N): f()

def my_action():
    """
    Example to document methods
    Explanation: this function takes two arguments: `i` and `d`.
    `i` is annotated simply as `int`. `d` is a dictionary with `str` keys
    and values that can be either `str` or `int`.

    The return type is `int`.

    """
    #ev3.light.on(Color.RED)
    spikerTail = Tail()

    spikerEyes = Eyes()
    spikerEyes.process_stimuli(spikerTail.shoot)


repeat(my_action, 2)


while True:
    my_action()