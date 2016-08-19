#!/usr/bin/python
# -*- coding: utf-8 -*-

from .enums import LocationType
from .utils import Singleton


class EnterMineAndDigForNugget(Singleton):
    """In this state the miner will walk to a goldmine and pick up a nugget
    of gold. If the miner already has a nugget of gold he'll change state
    to VisitBankAndDepositGold. If he gets thirsty he'll change state
    to QuenchThirst
    """

    def enter(self, miner):
        if miner.location != LocationType.gold_mine:
            print "{0}: Walkin' to the gold mine".format(miner.id)

            miner.change_location(LocationType.gold_mine)

    def execute(self, miner):
        miner.add_to_gold_carried(1)
        miner.increase_fatigue()

        print "{0}: Pickin' up a nugget".format(miner.id)

        if miner.pockets_is_full:
            miner.change_state(VisitBankAndDepositGold())

        if miner.thirsty:
            miner.change_state(QuenchThirst())

    def exit(self, miner):
        print ("{0}: Ah'm Leavin' the gold mine"
               "with mah pockets full o' sweet gold").format(miner.id)


class QuenchThirst(Singleton):

    def enter(self, miner):
        if miner.location != LocationType.saloon:
            print "{0}: Goin' to the bank. Yes siree".format(miner.id)

            miner.change_location(LocationType.saloon)
            print "{0}: Boy, ah sure is thusty! Walking to the Saloon".format(miner.id)

    def execute(self, miner):
        if miner.thirsty:
            miner.buy_and_drink_whiskey()
            print "{0}: That's mighty fine sippin liquer".format(miner.id)
            miner.change_state(EnterMineAndDigForNugget())
        else:
            print 'ERROR!\nERROR!\nERROR'

    def exit(self, miner):
        print "{0}: Leaving the saloon, feeling good!".format(miner.id)


class VisitBankAndDepositGold(Singleton):

    def enter(self, miner):
        if miner.location != LocationType.gold_mine:
            print "{0}: Goin' to the bank. Yes siree".format(miner.id)

            miner.change_location(LocationType.bank)

    def execute(self, miner):
        miner.add_to_wealth(miner.gold_carried)
        miner.gold_carried = 0

        print "{0}: Depositing Gold, Total savings now:  {1}".format(miner.id, miner.wealth)

        if miner.pockets_is_full:
            miner.change_state(VisitBankAndDepositGold())

        if miner.thirsty:
            miner.change_state(QuenchThirst())

    def exit(self, miner):
        print "{0}: Leavin' the bank".format(miner.id)


class GoHomeAndSleepTilRested(Singleton):

    def enter(self, miner):
        if miner.location != LocationType.shack:
            print "{0}: Walkin Home!".format(miner.id)

            miner.change_location(LocationType.shack)

    def execute(self, miner):
        if not miner.fatigued:
            print ("{0}: What a god darn fantastic nap! "
                   "time to find more gold!").format(miner.id)

            miner.change_state(EnterMineAndDigForNugget())
        else:
            miner.decrease_fatigue()
            print "{0}: ZZzzzzzz...".format(miner.id)

    def exit(self, miner):
        print "{0}: Leaving the House".format(miner.id)
