from otree.api import *
import math

doc = """
アンケート
"""


class C(BaseConstants):
    NAME_IN_URL = 'Survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField()
    gender = models.IntegerField()
    payoff_end = models.IntegerField()
   
# PAGES

class Gotosurvey(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        
        participant = player.participant
        player.payoff_end = participant.money + 1000
        participant.payoff_end1 = player.payoff_end
        participant.payoff_end = math.ceil(player.payoff_end / 10) * 10

class Survey(Page):
   form_model = 'player'
   form_fields = ['age','gender']



class ResultsWaitPage(WaitPage):
    pass


class Introduction(Page):
    pass

class Results(Page):
    pass


page_sequence = [Gotosurvey,Introduction, Survey, Results]
