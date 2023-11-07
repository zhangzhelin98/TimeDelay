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
        "field": models.FloatField,
        "items": { 
            "crt1": {
                "question": """
                    バットとボールは合計で 1.10 ドルです。 バットはボールより1ドル高い。ボールの値段はいくらですか？

                """,
                "unit": "セント",
                "correct": 5.0
            },
            "crt2": {
                "question": """
                   5 台の機械で 5 個の部品を 5 分間で作成する場合、100 台の機械で 100 個の部品を作成するのにかかる時間は?

                """,
                "unit": "分",
                "correct": 5.0
            },
            "crt3": {
                "question": """
                    湖には、スイレンの畑があります。 毎日、畑のサイズは 2 倍になります。 スイレンの畑が湖全体を覆いつくすのに48日かかる場合、畑が湖の半分を覆うのにどれくらいかかりますか?

                """,
                "unit": "日",
                "correct": 47
            },
            "crt4": {
                "question": """
                    Johnは６日間で１バレルの水を飲みます。Maryは１２日間で１バレルの水を飲みます。二人が一緒に１バレルの水を飲むのに何日かかりますか？

                """,
                "unit": "日",
                "correct": 4
            },
            "crt5": {
                "question": """
                    Jerryの成績は、クラスで上から１５番目、下からも１５番目です。クラスには何人の生徒がいますか？

                """,
                "unit": "人",
                "correct": 29
            },
            "crt6": {
                "question": """
                    ある男は６０ドルで豚を買い、７０ドルでこの豚を売りました。そして、彼は同じ豚を８０ドルで買い戻し、９０ドルで売りました。この男はいくら儲けましたか？

                """,
                "unit": "ドル",
                "correct": 20
            },
            "crt7": {
                "question": """
                    

                """,
                "unit": "ここで半角数字の1、2また3を入力してください。",
                "correct": 3
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
     


class CRT5(Page):
    form_model = "player"
    form_fields = ["crt5"]
    # is_displayed = is_displayed1
    # get_timeout_seconds = get_timeout_seconds1 
    # timer_text = C.TIMER_TEXT


class CRT6(Page):
    form_model = "player"
    form_fields = ["crt6"]
    # is_displayed = is_displayed1
    # get_timeout_seconds = get_timeout_seconds1 
    # timer_text = C.TIMER_TEXT
    

class CRT7(Page):
    form_model = "player"
    form_fields = ["crt7"]
    # is_displayed = is_displayed1
    # get_timeout_seconds = get_timeout_seconds1 
    # timer_text = C.TIMER_TEXT
    

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        
        my_before_next_page1(player, timeout_happened)
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
    
page_sequence = [Introduction, CRT1, CRT2, CRT3, CRT4, CRT5, CRT6, CRT7, Results1]

