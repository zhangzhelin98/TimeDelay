from otree.api import *


doc = """
実験の結果
"""


class C(BaseConstants):
    NAME_IN_URL = 'Result'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
    # payoff_end = models.IntegerField()


# PAGES
class Page1(Page):
    pass
    # @staticmethod
    # def before_next_page(player: Player, timeout_happened):
        
    #     participant = player.participant
    #     player.payoff_end = participant.keep_end + participant.reward_cal + 1000
    #     participant.payoff_end = player.payoff_end



class Page2(Page):
    pass

class MyWaitPage(Page):
    pass
   
    # template_name = 'Result/MyWaitPage.html'

class Page3(Page):
    pass


page_sequence = [Page1, Page2, MyWaitPage, Page3]
