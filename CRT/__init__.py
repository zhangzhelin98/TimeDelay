from otree.api import *


doc = """
クイズ
"""


class C(BaseConstants):
    NAME_IN_URL = 'CRT'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # TIMER_TEXT = "Time to complete this section:"
    materials_crt = {
        "field": models.StringField,
        "items": { 
            "crt1": {
                "question": """
                    もしもあなたがレースに参加して、2位の人を抜き去った場合、あなたは何位ですか?

                """,
                "unit": "位",
                "correct": "2"
            },
            "crt2": {
                "question": """
                   農夫が15匹の羊を持っていて、8匹以外は死にました。残りの羊は何匹ですか?

                """,
                "unit": "匹",
                "correct": "8"
            },
            "crt3": {
                "question": """
                    花子の父親は三人の娘がいます。最初の二人の名前は四月と五月です。三番目の娘の名前は何ですか?

                """,
                "unit": "",
                "correct": "花子"
            },
            "crt4": {
                "question": """
                    何立方フィートの土が、深さ3フィート×幅3フィート×長さ3フィートの穴に含まれていますか？

                """,
                "unit": "立方フィート",
                "correct": "0"
            },
            
        }
    }

     

    
            



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    score_crt = models.IntegerField()
    # payoff_crt= models.CurrencyField()
    # fixed_payment = models.CurrencyField()
    

    
   

for k, v in C.materials_crt["items"].items():
    setattr(
        Player,
        k,
        C.materials_crt["field"](
            label = v["question"],
            help_text = v["unit"]
        )
    )
    setattr(
        Player,
        k + "_score",
        models.BooleanField(
            initial = False
        )
    )







def calc_score_crt(player: Player, timeout_happened):
    if not timeout_happened:
        sumscore=0
        for k, v in C.materials_crt["items"].items():
            answer = getattr(player, k)
            correct = v["correct"]
            if answer == correct:
                setattr(player, k + "_score", True)
                sumscore += 1
        player.score_crt =  sumscore
    else:   
        sumscore=0
        for k, v in C.materials_crt["items"].items():
            answer = getattr(player, k)
            correct = v["correct"]
            if answer == correct:
                setattr(player, k + "_score", True)
                sumscore += 1
        player.score_crt =  sumscore 


     

 
    


  

def my_before_next_page1(player: Player, timeout_happened):
    calc_score_crt(player, timeout_happened)

   
   
def set_payoffs(player: Player):
    player.payoff_crt = player.score_crt*10    
    

# PAGES

# def get_timeout_seconds1(player: Player):
#     participant = player.participant
#     import time
#     return participant.expiry - time.time()


# def is_displayed1(player: Player):
#     """only returns True if there is time left."""
#     return get_timeout_seconds1(player) > 0


class Introduction(Page):
    form_model = "player"
    timeout_seconds = 30
    # @staticmethod
    # def before_next_page(player: Player, timeout_happened):
    #     participant = player.participant
    #     import time

    #     participant.expiry = time.time() + 60
 

class CRT1(Page):
    form_model = "player"
    form_fields = ["crt1"]
    # is_displayed = is_displayed1
    # get_timeout_seconds = get_timeout_seconds1
    # timer_text = C.TIMER_TEXT   
    
 



class CRT2(Page):
    form_model = "player"
    form_fields = ["crt2"]    
    # is_displayed = is_displayed1
    # get_timeout_seconds = get_timeout_seconds1
    # timer_text = C.TIMER_TEXT


class CRT3(Page):
    form_model = "player"
    form_fields = ["crt3"] 
    # is_displayed = is_displayed1
    # get_timeout_seconds = get_timeout_seconds1
    # timer_text = C.TIMER_TEXT
    


class CRT4(Page):
    form_model = "player"
    form_fields = ["crt4"] 
    # is_displayed = is_displayed1
    # get_timeout_seconds = get_timeout_seconds1
    # timer_text = C.TIMER_TEXT
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        
        my_before_next_page1(player, timeout_happened)     


# class CRT5(Page):
#     form_model = "player"
#     form_fields = ["crt5"]
#     # is_displayed = is_displayed1
#     # get_timeout_seconds = get_timeout_seconds1 
#     # timer_text = C.TIMER_TEXT


# class CRT6(Page):
#     form_model = "player"
#     form_fields = ["crt6"]
#     # is_displayed = is_displayed1
#     # get_timeout_seconds = get_timeout_seconds1 
#     # timer_text = C.TIMER_TEXT
    

# class CRT7(Page):
#     form_model = "player"
#     form_fields = ["crt7"]
#     # is_displayed = is_displayed1
#     # get_timeout_seconds = get_timeout_seconds1 
#     # timer_text = C.TIMER_TEXT
    

    # @staticmethod
    # def before_next_page(player: Player, timeout_happened):
        
    #     my_before_next_page1(player, timeout_happened)
        # set_payoffs(player)
        # participant = player.participant
        # participant.reward_effort = player.payoff_crt + participant.reward_cal
        # player.fixed_payment = 1000
        # participant.reward_plus1000 = player.payoff_crt + participant.reward_cal + player.fixed_payment
        # participant.reward_effort = participant.reward_cal + participant.reward_crt
        
        


    
    
   
  
        

# class ResultsWaitPage(WaitPage):
#     after_all_players_arrive = 'set_payoffs'

class Results1(Page):
    
    timeout_seconds = 30

class Results2(Page):
    timeout_seconds = 30
    
page_sequence = [Introduction, CRT1, CRT2, CRT3, CRT4, Results1]

