#!/usr/bin/python
# -*- coding: utf-8 -*-

import entity
from .exceptions import UnknownCurrentStateError


class StateMachine(object):
    """State machine"""

    def __init__(self, owner):
        self._owner = owner
        self._current_state = None
        self._previous_state = None

    @property
    def owner(self):
        return self._owner

    @property
    def current_state(self):
        return self._current_state

    @current_state.setter
    def current_state(self, val):
        if not isinstance(val, entity.Entity):
            raise TypeError("Parameter is not an entity")

        self._current_state = val

    @property
    def previous_state(self):
        return self._previous_state

    @previous_state.setter
    def previous_state(self, val):
        if not isinstance(val, entity.Entity):
            raise TypeError("Parameter is not an entity")

        self._previous_state = val

    def update(self):
        if self.current_state is not None:
            self.current_state.execute(self.owner)
        else:
            raise UnknownCurrentStateError("Current state is none")

    def change_state(self, new_state):
        self.previous_state = self.current_state
        self.current_state.exit(self.owner)
        self.current_state = new_state
        self.current_state.enter(self.owner)

    def revert_to_prev_state(self):
        self.change_state(self.previous_state)

    def is_in_state(self, state):
        return self.current_state.__class__ == state.__class__.name
