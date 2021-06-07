#!/usr/bin/env pybricks-micropython

from Menu import Menu

import itertools

def repeat(f, N):
    for _ in itertools.repeat(None, N): f()

def main():
    menu = Menu()
    menu.handle_button_press()


repeat(main, 3)