#!/usr/bin/python
# -*- coding: utf-8 -*-


class UnknownCurrentStateError(UnboundLocalError):
    """State machine's current state is none
    """
    pass


class PackageMissingError(Exception):
    """Try import missing package
    """
    pass
