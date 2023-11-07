from otree.api import *


doc = """
実験の流れ、謝金についての説明
"""


class C(BaseConstants):
    NAME_IN_URL = 'introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Intorduction(Page):
    pass


class Wait(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Intorduction]
