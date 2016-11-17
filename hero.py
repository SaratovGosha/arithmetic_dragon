# coding: utf-8
# license: GPLv3
from gameunit import *

class Hero(Attacker):
    _name = None
    _health = None
    _experience = None
    _attack = None

    def __init__(self, name):
        self._name = name
        self._health = 100
        self._experience = 0
        self._attack = 50
    def attack(self,target):
        target._health -= self._attack
        self._experience += 1
    def gameOver(self):
        return 'GameOver!'


