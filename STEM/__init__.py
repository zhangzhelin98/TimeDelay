from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'STEM'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()
    q11 = models.IntegerField()
    q12 = models.IntegerField()
    q13 = models.IntegerField()
    q14 = models.IntegerField()
    q15 = models.IntegerField()
    q16 = models.IntegerField()
    q17 = models.IntegerField()
    
    q18 = models.IntegerField()




# PAGES
    
class intro(Page):
    pass

class Q1(Page):
   form_model = 'player'
   form_fields = ['q1']
   

class Q2(Page):
   form_model = 'player'
   form_fields = ['q2']

class Q2(Page):
   form_model = 'player'
   form_fields = ['q2']

class Q3(Page):
   form_model = 'player'
   form_fields = ['q3']

class Q4(Page):
   form_model = 'player'
   form_fields = ['q4']

class Q5(Page):
   form_model = 'player'
   form_fields = ['q5']

class Q6(Page):
   form_model = 'player'
   form_fields = ['q6']

class Q7(Page):
   form_model = 'player'
   form_fields = ['q7']

class Q8(Page):
   form_model = 'player'
   form_fields = ['q8']

class Q9(Page):
   form_model = 'player'
   form_fields = ['q9']

class Q10(Page):
   form_model = 'player'
   form_fields = ['q10']

class Q11(Page):
   form_model = 'player'
   form_fields = ['q11']

class Q12(Page):
   form_model = 'player'
   form_fields = ['q12']

class Q13(Page):
   form_model = 'player'
   form_fields = ['q13']

class Q14(Page):
   form_model = 'player'
   form_fields = ['q14']

class Q15(Page):
   form_model = 'player'
   form_fields = ['q15']

class Q16(Page):
   form_model = 'player'
   form_fields = ['q16']

class Q17(Page):
   form_model = 'player'
   form_fields = ['q17']

class Q18(Page):
   form_model = 'player'
   form_fields = ['q18']

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [intro, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Results]
