"""
This file is for creating classes in python

To run this code, type in main.py
>>> from src.programming.objects_1 import *
where the * is a wild card import.  Then, add under main():
>>> object_script()
"""


import numpy as np


class Dice:
    """
    Create a virtual dice which takes an input of the number of sides N.

      - This dice can be rolled using the "self.roll()" method, after which it
        will display a random integer number between 1 - N.

      - The number showing on the dice can be checked with the "self.check"
        method, which will output the integer between 1 - N currently showing.

      - The dice can be picked up with the "self.pick_up" method, after which
        no number can be read from the dice

    In order to write the self.roll() method, we recommend that you use
    the NumPy command "numpy.random.randint".  Link to the documentation:
    numpy.org/doc/stable/reference/random/generated/numpy.random.randint
    """

    def __init__(self):
        pass

    def roll(self):
        pass

    def check(self) -> int:
        pass

    def pick_up(self):
        pass


def object_script():
    # Use this script to test the objects you create
    dice_instance = Dice()
