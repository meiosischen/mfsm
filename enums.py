#!/usr/bin/python
# -*- coding: utf-8 -*-

from .exceptions import PackageMissingError

try:
    from flufl.enum import Enum
except ImportError:
    raise PackageMissingError("Missing flufl.enum")


class LocationType(Enum):
    shack = 1
    gold_mine = 2
    tank = 3
    saloon = 4


class EntityNames(Enum):
    Miner_Bob = 1
    Elsa = 2
