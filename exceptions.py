#!/usr/bin/python
# -*- coding: utf-8 -*-


class UnknownCurrentStateError(UnboundLocalError):
    """State machine's current state is none
    """
    pass
