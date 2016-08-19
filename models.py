#!/usr/bin/python
# -*- coding: utf-8 -*-

from .enums import LocationType
from .states import GoHomeAndSleepTilRested

# the amount of gold a miner must have before he feels comfortable
COMFORTLEVEL = 5

# the amount of nuggets a miner can carry
MAXNUGGETS = 3

# above this value a miner is thirsty
THIRSTLEVEL = 5

# above this value a miner is sleepy
TIREDNESSTHRESHOLD = 5


class Entity(object):
    """Entity
    """

    def __init__(self, id):
        self._id = id
        self._location = None
        self._current_state = None

    @property
    def id(self):
        return self._id

    @property
    def current_state(self):
        return self._current_state

    @current_state.setter
    def current_state(self, new_state):
        self._current_state = new_state

    @property
    def location(self):
        return self._location

    def change_location(self, new_loc):
        self._location = new_loc


class Miner(Entity):
    """Docstring for Miner.
    """

    def __init__(self, id):
        super(Miner, self).__init__(id)
        self._location = LocationType.shack
        self._gold_carried = 0
        self._money_in_bank = 0
        self._thirst = 0
        self._fatigue = 0
        self._current_state = GoHomeAndSleepTilRested()

    def update(self):
        self._thirst += 1
        if (self._current_state is not None):
            self._current_state.execute(self)

    def change_state(self, new_state):
        assert self.current_state is not None and new_state is not None

        self.current_state.exit(self)
        self.current_state = new_state
        self.current_state.enter(self)

    def add_to_gold_carried(self, val):
        self._gold_carried += val

    def increase_fatigue(self, val=None):
        self._fatigue += 1 if val is None else val

    @property
    def thirsty(self):
        if (self._thirst >= THIRSTLEVEL):
            return True
        else:
            return False

    @property
    def pockets_is_full(self):
        if (self._gold_carried >= MAXNUGGETS):
            return True
        else:
            return False

    @property
    def wealth(self):
        return self._money_in_bank

    @wealth.setter
    def wealth(self, val):
        self._money_in_bank = val

    def add_to_wealth(self, val):
        self._money_in_bank += val
        if (self._money_in_bank < 0):
            self._money_in_bank = 0

    @property
    def gold_carried(self):
        return self._gold_carried

    @gold_carried.setter
    def gold_carried(self, val):
        self._gold_carried = val

    def buy_and_drink_whiskey(self):
        self._thirst = 0
        self._money_in_bank -= 2

    def decrease_fatigue(self):
        self._fatigue -= 1

    @property
    def fatigued(self):
        print self._fatigue
        if self._fatigue > TIREDNESSTHRESHOLD:
            return True
        else:
            return False
