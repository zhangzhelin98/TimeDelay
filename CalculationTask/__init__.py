from otree.api import *
import random
import json


doc = """
計算問題
"""


class C(BaseConstants):
    NAME_IN_URL = 'CalculationTask'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TIMER_TEXT = "計算タスクの残り時間は:"
    materials_calculation = {
        "field": models.FloatField,
        "items": {
            "q1": {
                "question": """
                    82+24+82+86=

                """,
                "correct": 274.0

            },
            "q2": {
                "question": """
                    84+88+11+80=

                """,
                "correct": 263.0

            },
            "q3": {
                "question": """
                    5+97+16+37=

                """,
                "correct": 155.0

            },
            "q4": {
                "question": """
                    4+4+3+47=


                """,
                "correct": 58.0

            },
            "q5": {
                "question": """
                    56+63+24+21=

                """,
                "correct": 164.0


            },
            "q6": {
                "question": """
                    91+27+45+85=


                """,
                "correct": 248.0


            },
            "q7": {
                "question": """
                    74+77+71+35=


                """,
                "correct": 257.0

            },
            "q8": {
                "question": """
                    61+87+55+1=


                """,
                "correct": 204.0

            },
            "q9": {
                "question": """
                    32+34+80+54=

                """,
                "correct": 200.0


            },
            "q10": {
                "question": """
                    98+49+16+4=


                """,
                "correct": 167.0


            },
            "q11": {
                "question": """
                    60+54+31+5=


                """,
                "correct": 150.0


            },
            "q12": {
                "question": """
                    22+59+2+4=


                """,
                "correct": 87.0


            },
            "q13": {
                "question": """
                    3+1+91+19=


                """,
                "correct": 114.0


            },
            "q14": {
                "question": """
                    92+78+72+36=


                """,
                "correct": 278.0

            },
            "q15": {
                "question": """
                    81+93+42+77=


                """,
                "correct": 293.0

            },"q16": {
                "question": """
                    31+97+37+63=


                """,
                "correct": 228.0

            },
            "q17": {
                "question": """
                    44+45+45+66=


                """,
                "correct": 200.0

            },
            "q18": {
                "question": """
                    19+31+12+44=


                """,
                "correct": 106.0

            },
            "q19": {
                "question": """
                    74+15+59+78=


                """,
                "correct": 226.0


            },"q20": {
                "question": """
                    83+29+82+11=


                """,
                "correct": 205.0


            },"q21": {
                "question": """
                    4+28+17+20=


                """,
                "correct": 69.0


            },"q22": {
                "question": """
                    23+77+26+48=


                """,
                "correct": 174.0

            },"q23": {
                "question": """
                    52+85+71+24=


                """,
                "correct": 232.0


            },"q24": {
                "question": """
                    46+50+19+68=


                """,
                "correct": 183.0


            },"q25": {
                "question": """
                    49+86+14+29=


                """,
                "correct": 178.0


            },"q26": {
                "question": """
                    36+69+6+91=


                """,
                "correct": 202.0


            },"q27": {
                "question": """
                    26+49+6+2=


                """,
                "correct": 83.0


            },"q28": {
                "question": """
                    85+87+87+72=


                """,
                "correct": 331.0


            },"q29": {
                "question": """
                    77+20+20+11=


                """,
                "correct": 128.0


            },
            "q30": {
                "question": """
                    41+4+66+42=

                """,
                "correct": 153.0
            },
            "q31": {
                "question": """
                    90+25+98+79=

                """,
                "correct": 292.0

            },
            "q32": {
                "question": """
                    97+91+92+96=

                """,
                "correct": 376.0

            },
            "q33": {
                "question": """
                    92+21+42+27=

                """,
                "correct": 182.0

            },
            "q34": {
                "question": """
                    72+93+90+28=

                """,
                "correct": 283.0

            },
            "q35": {
                "question": """
                    60+44+79+92=

                """,
                "correct": 275.0

            },
            "q36": {
                "question": """
                    25+85+51+60=

                """,
                "correct": 221.0

            },
            "q37": {
                "question": """
                    69+94+68+68=

                """,
                "correct": 299.0

            },
            "q38": {
                "question": """
                    25+76+87+20=

                """,
                "correct": 208.0

            },
            "q39": {
                "question": """
                    75+77+21+47=

                """,
                "correct": 220.0

            },
            "q40": {
                "question": """
                    1+18+77+45=

                """,
                "correct": 141.0

            },


            "q41": {
                "question": """
                    31+63+36+32=

                """,
                "correct": 162.0

            },
            "q42": {
                "question": """
                    78+44+1+16=

                """,
                "correct": 139.0

            },
            "q43": {
                "question": """
                    3+46+46+47=

                """,
                "correct": 142.0

            },
            "q44": {
                "question": """
                    4+53+62+68=

                """,
                "correct": 187.0

            },
            "q45": {
                "question": """
                    95+6+96+26=

                """,
                "correct": 223.0

            },
            "q46": {
                "question": """
                    54+6+82+95=

                """,
                "correct": 237.0

            },
            "q47": {
                "question": """
                    73+15+83+73=

                """,
                "correct": 244.0

            },
            "q48": {
                "question": """
                    70+80+79+19=

                """,
                "correct": 248.0

            },
            "q49": {
                "question": """
                    53+11+13+67=

                """,
                "correct": 144.0

            },

                      
        }
    }

class Subsession(BaseSubsession):
    pass






class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # order_calculation = models.LongStringField()
    score_calculation = models.IntegerField(initial=0)
    payoff_cal = models.CurrencyField()



for k, v in C.materials_calculation["items"].items():
    setattr(
        Player,
        k,
        C.materials_calculation["field"](
            label = v["question"]    
        )
    )
#     setattr(
#         Player,
#         k + "_score",
#         models.BooleanField(
#             initial = False
#         )
#     )

# # def creating_session(subsession: Subsession):
# #     list_calculation = [*C.materials_calculation["items"].keys()]

# #     for p in subsession.get_players():
# #         p.order_calculation = json.dumps(
# #             random.sample(list_calculation, len(list_calculation))
# #         )

# def calc_score_calculation(player: Player, timeout_happened):
#     if not timeout_happened:
#         sumscore = 0
#         for k, v in C.materials_calculation["items"].items():
#             answer = getattr(player, k)
#             correct = v["correct"]
#             if answer == correct:
#                 setattr(player, k + "_score", True)
#                 sumscore += 1
#         player.score_calculation =  sumscore
#     else:
#         sumscore = 0
#         for k, v in C.materials_calculation["items"].items():
#             answer = getattr(player, k)
#             correct = v["correct"]
#             if answer == correct:
#                 setattr(player, k + "_score", True)
#                 sumscore += 1
#         player.score_calculation =  sumscore
    
# def my_before_next_page(player: Player, timeout_happened):
#     calc_score_calculation(player, timeout_happened)
   
def set_payoffs(player: Player):
    
    player.payoff_cal = player.score_calculation*50
#  PAGES

def get_timeout_seconds1(player: Player):
    participant = player.participant
    import time
    return participant.expiry - time.time()


def is_displayed1(player: Player):
    """only returns True if there is time left."""
    return get_timeout_seconds1(player) > 0


class Introduction(Page):
    
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time

        participant.expiry = time.time() + 300

class Q1(Page):
    form_model="player"
    form_fields=["q1"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q1 ==274.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0    
#获得初期保有1200元
# このようにパフォーマンスに関係ない固定謝金を入れると、わざわざreal effortタスクで初期保有を決める意味がないように思います。
# 計算タスクで、全員が達成できるような水準の正解数を決めておいて、それを達成したら、それ以上の追加報酬はない。。
# ただ、それを達成するためには、ある程度の努力が必要というのではだめでしょうか？    
# 13問にすると  
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

        


        

class Q2(Page):
    form_model="player"
    form_fields=["q2"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q2==263.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

       

class Q3(Page):
    form_model="player"
    form_fields=["q3"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q3==155.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

       

class Q4(Page):
    form_model="player"
    form_fields=["q4"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q4==58.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

       

class Q5(Page):
    form_model="player"
    form_fields=["q5"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q5==164.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

       

class Q6(Page):
    form_model="player"
    form_fields=["q6"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q6==248.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

       
class Q7(Page):
    form_model="player"
    form_fields=["q7"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q7==257.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

       

class Q8(Page):
    form_model="player"
    form_fields=["q8"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q8==204.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

class Q9(Page):
    form_model="player"
    form_fields=["q9"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q9==200.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q10(Page):
    form_model="player"
    form_fields=["q10"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q10==167.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q11(Page):
    form_model="player"
    form_fields=["q11"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q11==150.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q12(Page):
    form_model="player"
    form_fields=["q12"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q12==87.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q13(Page):
    form_model="player"
    form_fields=["q13"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q13==114.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q14(Page):
    form_model="player"
    form_fields=["q14"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q14==278.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q15(Page):
    form_model="player"
    form_fields=["q15"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q15==293.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q16(Page):
    form_model="player"
    form_fields=["q16"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q16==228.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q17(Page):
    form_model="player"
    form_fields=["q17"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q17==200.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q18(Page):
    form_model="player"
    form_fields=["q18"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q18==106.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q19(Page):
    form_model="player"
    form_fields=["q19"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q19==226.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q20(Page):
    form_model="player"
    form_fields=["q20"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q20==205.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q21(Page):
    form_model="player"
    form_fields=["q21"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q21==69.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q22(Page):
    form_model="player"
    form_fields=["q22"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q22==174.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q23(Page):
    form_model="player"
    form_fields=["q23"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q23==232.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q24(Page):
    form_model="player"
    form_fields=["q24"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q24==183.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q25(Page):
    form_model="player"
    form_fields=["q25"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q25==178.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q26(Page):
    form_model="player"
    form_fields=["q26"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q26==202.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q27(Page):
    form_model="player"
    form_fields=["q27"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q27==83.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q28(Page):
    form_model="player"
    form_fields=["q28"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q28==331.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q29(Page):
    form_model="player"
    form_fields=["q29"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q29==128.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q30(Page):
    form_model="player"
    form_fields=["q30"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q30==153.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q31(Page):
    form_model="player"
    form_fields=["q31"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q31==292.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q32(Page):
    form_model="player"
    form_fields=["q32"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q2==376.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q33(Page):
    form_model="player"
    form_fields=["q33"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q33==182.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal


class Q34(Page):
    form_model="player"
    form_fields=["q34"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q34==283.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

class Q34(Page):
    form_model="player"
    form_fields=["q34"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q34==283.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

class Q35(Page):
    form_model="player"
    form_fields=["q35"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q35==275.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

class Q36(Page):
    form_model="player"
    form_fields=["q36"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q36==221.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

class Q37(Page):
    form_model="player"
    form_fields=["q37"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q37==299.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

class Q38(Page):
    form_model="player"
    form_fields=["q38"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q38==208.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal
class Q39(Page):
    form_model="player"
    form_fields=["q39"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q39==220.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal
class Q40(Page):
    form_model="player"
    form_fields=["q40"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q40==141.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal
class Q41(Page):
    form_model="player"
    form_fields=["q41"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q41==162.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal
class Q42(Page):
    form_model="player"
    form_fields=["q42"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q42==139.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal
class Q43(Page):
    form_model="player"
    form_fields=["q43"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q43==142.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal
class Q44(Page):
    form_model="player"
    form_fields=["q44"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q44==187.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal
class Q45(Page):
    form_model="player"
    form_fields=["q45"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q45==223.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

class Q46(Page):
    form_model="player"
    form_fields=["q46"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q46==237.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

class Q47(Page):
    form_model="player"
    form_fields=["q47"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q47==244.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

class Q48(Page):
    form_model="player"
    form_fields=["q48"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q48==248.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

class Q49(Page):
    form_model="player"
    form_fields=["q49"]
    template_name = __name__+ "/question_template.html"
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT   
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.q49==144.0:
           player.score_calculation += 1
        else:
           player.score_calculation += 0  
        
        set_payoffs(player) 
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal








class Question(Page):
    form_model = "player"
    timeout_seconds = 300
    timer_text= '計算タスクの残り時間は:'

    @staticmethod
    def get_form_fields(player: Player):
        return json.loads(player.order_calculation)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        my_before_next_page(player, timeout_happened)    #没有这一句就没法显示score
        set_payoffs(player)    
        participant = player.participant
        if player.score_calculation >=13:
            participant.reward_cal = 1200
        else:
            participant.reward_cal = player.payoff_cal

     

       
# class ResultsWaitPage(WaitPage):
#     after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [Introduction, Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,
                  Q11,Q12,Q13,Q14,Q15,Q16,Q17,Q18,Q19,Q20,Q21,
                  Q22,Q23,Q24,Q25,Q26,Q27,Q28,Q29,Q30,Q31,Q32,
                  Q33,Q34,Q35,Q36,Q37,Q38,Q39,Q40,Q41,Q42,Q43,
                  Q44,Q45,Q46,Q47,Q48,Q49,Results]
