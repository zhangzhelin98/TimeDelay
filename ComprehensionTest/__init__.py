from unicodedata import name
from xmlrpc.client import Fault
from otree.api import *


doc = """
理解度テスト
"""


class C(BaseConstants):
    NAME_IN_URL = 'ComprehensionTest'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    FORM_TEMPLATE = __name__ + '/form.html'

def get_test_data():
    return [
        dict(
            name='t1',
            solution=False,
            explanation="あなたが選択した価格はコンピューターが無作為で選択した整数未満なので、くじは購入しません。結果、あなたの今回の収益は、くじの払戻金額にかかわらず、０ポイントになります。",   
        ),
        dict(
            name='t2',
            solution=True,
            explanation="あなたが選択した価格はコンピューターが無作為で選択した整数以上なので、くじを300ポイントで購入することになります。結果、あなたの今回の収益は-50ポイントになります（300-350=-50）。",
        ),
        dict(name="t3",
             solution=True,
             explanation="あなたが選択した価格はコンピューターが無作為で選択した整数以上なので、くじを200ポイントで購入することになります。結果、あなたの今回の収益は100ポイントになります（300-200=100）。",
        ),
        dict(
            name="t4",
            solution=True,
            explanation="あなたが選択した価格はコンピューターが無作為で選択した整数未満なので、くじは購入しません。結果、あなたの今回の収益は、くじの払戻金額にかかわらず、０ポイントになります。"
        ),
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    t1 = models.BooleanField(label="あなたはくじを購入するため、200ポイントを選択したとします。\nコンピューターが無作為に選択した整数は350だったとします。\n無作為抽選によって、今回のくじの払戻金額は300ポイントになったとします。\n結果、今期の収益は-50ポイントになります。", choices=[[True, "正しい"],[False, "正しくない"]])
    t2 = models.BooleanField(label="あなたはくじを購入するため、400ポイントを選択したとします。\nコンピューターが無作為に選択した整数は350だったとします。\n無作為抽選によって、今回のくじの払戻金額は300ポイントになったとします。\n結果、今期の収益は-50ポイントになります。", choices=[[True, "正しい"],[False, "正しくない"]])
    t3 = models.BooleanField(label="あなたはくじを購入するため、350ポイントを選択したとします。\nコンピューターが無作為に選択した整数は200だったとします。\n無作為抽選によって、今回のくじの払戻金額は300ポイントになったとします。\n結果、今期の収益は100ポイントになります。", choices=[[True, "正しい"],[False, "正しくない"]])
    t4 = models.BooleanField(label="あなたはくじを購入するため、150ポイントを選択したとします。\nコンピューターが無作為に選択した整数は400だったとします。\n無作為抽選によって、今回のくじの払戻金額は-10000ポイントになったとします。\n結果、今期の収益は0ポイントになります。", choices=[[True, "正しい"],[False, "正しくない"]])


# PAGES

class comprehension_test(Page):
    pass


class MyPage(Page):
    form_model = 'player'
    form_fields = ['t1', 't2', 't3', 't4']

    @staticmethod
    def vars_for_template(player: Player):
        fields = get_test_data()
        return dict(fields=fields, show_solutions=False)



class Results(Page):
    form_model = 'player'
    form_fields = ['t1', 't2', 't3', 't4']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.initial = participant.reward_cal + 10000

    @staticmethod
    def vars_for_template(player: Player):
        fields = get_test_data()
        # we add an extra entry 'is_correct' (True/False) to each field
        for d in fields:
            d['is_correct'] = getattr(player, d['name']) == d['solution']
        return dict(fields=fields, show_solutions=True)

    @staticmethod
    def error_message(player: Player, values):
        for field in values:
            if getattr(player, field) != values[field]:
                return "選択を変えずに進んでください。"    


class Initial(Page):
    pass
 


page_sequence = [comprehension_test, MyPage, Results, Initial]
