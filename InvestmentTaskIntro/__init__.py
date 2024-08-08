from otree.api import *


doc = """
投資タスクの説明
"""


class C(BaseConstants):
    NAME_IN_URL = 'InvestmentTaskIntro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ENDOWMENT = cu(2000)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
      give = models.IntegerField(min=0, max=1000, label="最大希望価格")



# PAGES
class Introduction(Page):
    pass

class price_input(Page):
      pass


class example_price_input(Page):
    form_model = 'player'
    form_fields = ['give']
    @staticmethod
    def js_vars(player: Player):
        return dict(endowment=C.ENDOWMENT)


class price_setting(Page):
      pass

class payoff_intro(Page):
      pass
class example1(Page):
      pass 
class example2(Page):
      pass 
class payment_intro(Page):
      pass 

class loan(Page):
      @staticmethod
      def js_vars(player: Player):
           participant = player.participant
           participant.loan = participant.reward_cal + 10000
      

      


class possible_10min(Page):
    pass

class pose(Page):
     pass

class myWaitPage(WaitPage):
    pass


# delay treatment
# page_sequence = [Introduction, price_input, example_price_input, price_setting, payoff_intro, 
#                  example1, example2, payment_intro, loan,possible_10min, pose, myWaitPage
#                 ]

# no delay treatment
page_sequence = [Introduction, price_input, example_price_input, price_setting, payoff_intro, 
                 example1, example2, payment_intro, loan, pose, myWaitPage
                ]
