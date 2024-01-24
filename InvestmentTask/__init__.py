from otree.api import *
import random


doc = """
投資タスク
"""
# photopath = "_static/photo"
# os.makedirs(photopath, exist_ok=True)


class C(BaseConstants):
    NAME_IN_URL = "InvestmentTask"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10
    ENDOWMENT = cu(20000)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    computer_price = models.IntegerField()
    reward = models.IntegerField()


class Player(BasePlayer):
    price = models.IntegerField(initial="0", min=0, max=500, label="最大希望価格")
    computer_price = models.IntegerField()
    reward = models.IntegerField()
    profit = models.IntegerField()
    total_profit = models.IntegerField()
    keep = models.IntegerField()
    tail = models.IntegerField()
    tail_total = models.IntegerField()
    overdraft = models.BooleanField()
    keep_end = models.IntegerField()
    blackphoto = models.IntegerField(initial=0)
    time_distance_from_start = models.StringField(initial="")


def computer_price(group: Group):
    group.computer_price = random.randint(1, 500)


# 发生损失的概率，从里面抽选
def reward(group: Group):
    group.reward = random.choice(
        [
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            1000,
            1000,
            1000,
            1000,
            1000,
            1000,
            1000,
            1000,
            1000,
            -10000,
        ]
    )


# 前5轮不会发生重大损失 practice rounds
def reward_5(group: Group):
    group.reward = random.choice(
        [
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            200,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            300,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            400,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            500,
            1000,
            1000,
            1000,
            1000,
            1000,
            1000,
            1000,
            1000,
            1000,
        ]
    )


def profit(player: Player):
    group = player.group
    if player.price >= group.computer_price:
        player.profit = group.reward - group.computer_price

    else:
        player.profit = 0


def tail_event(player: Player):
    group = player.group
    Occurrence = 0
    if group.reward == -10000:
        Occurrence += 1
    if group.reward != -10000:
        Occurrence += 0
    player.tail = Occurrence


# PAGES
class test1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        player.participant.vars["videoframe"] = []

    @staticmethod
    def js_vars(player: Player):
        player.participant.vars["pagecount"] = 1
        # print(player.participant.vars["pagecount"])
        return dict(cnt=player.participant.vars["pagecount"])

    @staticmethod
    def live_method(player: Player, data):
        if data:
            try:
                start_time = data["starttime"]
            except Exception:
                print("invalid message received:", data)
                return
            player.participant.vars["start_time"] = start_time


class Investment1(Page):
    timeout_seconds = 300
    timer_text = "最大購入希望価格を決めるまでの残り時間は:"
    form_model = "player"
    form_fields = ["price"]

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'player_id_in_subsession': player.id_in_subsession,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number <= 5

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.price = random.randint(0, 500)

    @staticmethod
    def js_vars(player: Player):
        player.participant.vars["pagecount"] += 1
        # print(player.participant.vars["pagecount"])
        return dict(cnt=player.participant.vars["pagecount"])

    @staticmethod
    def live_method(player: Player, data):
        if data:
            try:
                decidetime = data["decidetime"]
            except Exception:
                print("invalid message received:", data)
                return
            if player.time_distance_from_start == "":
                player.time_distance_from_start = "invest 1:" + str(
                    decidetime - player.participant.vars["start_time"]
                )
            else:
                player.time_distance_from_start += (
                    ","
                    + "invest 1:"
                    + str(decidetime - player.participant.vars["start_time"])
                )


class Investment2(Page):
    timeout_seconds = 150
    timer_text = "最大購入希望価格を決めるまでの残り時間は:"
    form_model = "player"
    form_fields = ["price"]

    template_name = "InvestmentTask/Investment1.html"

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number > 5

    @staticmethod
    def js_vars(player: Player):
        player.participant.vars["pagecount"] += 1
        # print(player.participant.vars["pagecount"])
        return dict(cnt=player.participant.vars["pagecount"])

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.price = random.randint(0, 500)

    @staticmethod
    def live_method(player: Player, data):
        if data:
            try:
                decidetime = data["decidetime"]
            except Exception:
                print("invalid message received:", data)
                return
            if player.time_distance_from_start == "":
                player.time_distance_from_start = "invest 2:" + str(
                    decidetime - player.participant.vars["start_time"]
                )
            else:
                player.time_distance_from_start += (
                    ","
                    + "invest 2:"
                    + str(decidetime - player.participant.vars["start_time"])
                )


class WaitPage1(WaitPage):
    template_name = "InvestmentTask/WaitPage_w_cam.html"

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number <= 5

    @staticmethod
    def js_vars(player: Player):
        player.participant.vars["pagecount"] += 1
        print("XXXXXXXXXX", player.participant.vars["pagecount"])
        return dict(cnt=player.participant.vars["pagecount"])

    @staticmethod
    def after_all_players_arrive(group: Group):
        computer_price(group)
        reward_5(group)
        for player in group.get_players():
            profit(player)
            tail_event(player)
            player_in_all_rounds = player.in_all_rounds()
            player.tail_total = sum([p.tail for p in player_in_all_rounds])
            player.total_profit = sum([p.profit for p in player_in_all_rounds])
            participant = player.participant
            player.keep = participant.initial + player.total_profit
            if player.keep <= 0:
                player.overdraft = True
            else:
                player.overdraft = False
            if player.keep >= 10000:
                player.keep_end = player.keep - 10000
            if player.keep < 10000:
                player.keep_end = 0

            participant.keep_end = player.keep_end
            participant.money1 = participant.keep_end / 50
            participant.money = round(participant.money1)


class WaitPage2(WaitPage):
    template_name = "InvestmentTask/WaitPage_w_cam.html"

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number > 5

    @staticmethod
    def js_vars(player: Player):
        player.participant.vars["pagecount"] += 1
        # print(player.participant.vars["pagecount"])
        return dict(cnt=player.participant.vars["pagecount"])

    @staticmethod
    def after_all_players_arrive(group: Group):
        computer_price(group)
        reward(group)
        for player in group.get_players():
            profit(player)
            tail_event(player)
            player_in_all_rounds = player.in_all_rounds()
            player.tail_total = sum([p.tail for p in player_in_all_rounds])
            player.total_profit = sum([p.profit for p in player_in_all_rounds])
            participant = player.participant
            player.keep = participant.initial + player.total_profit
            if player.keep <= 0:
                player.overdraft = True
            else:
                player.overdraft = False
            if player.keep >= 10000:
                player.keep_end = player.keep - 10000
            if player.keep < 10000:
                player.keep_end = 0

            participant.keep_end = player.keep_end
            participant.money1 = participant.keep_end / 50
            participant.money = round(participant.money1)


class can_buy(Page):
    timeout_seconds = 10

    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.price >= group.computer_price

    @staticmethod
    def js_vars(player: Player):
        player.participant.vars["pagecount"] += 1
        # print(player.participant.vars["pagecount"])
        return dict(cnt=player.participant.vars["pagecount"])


class cannot_buy(Page):
    timeout_seconds = 10

    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.price < group.computer_price

    @staticmethod
    def js_vars(player: Player):
        player.participant.vars["pagecount"] += 1
        # print(player.participant.vars["pagecount"])
        return dict(cnt=player.participant.vars["pagecount"])


class Feedback_buy(Page):
    timeout_seconds = 15

    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.price >= group.computer_price and group.reward != -10000

    @staticmethod
    def js_vars(player: Player):
        player.participant.vars["pagecount"] += 1
        # print(player.participant.vars["pagecount"])
        return dict(cnt=player.participant.vars["pagecount"])

    # @staticmethod
    # def before_next_page(player: Player, timeout_happened):
    #     print(player.time_distance_from_start)

    @staticmethod
    def live_method(player: Player, data):
        if data:
            try:
                finishtime = data["finishtime"]
            except Exception:
                print("invalid message received:", data)
                return
            if player.time_distance_from_start == "":
                player.time_distance_from_start = "feedback buy:" + str(
                    finishtime - player.participant.vars["start_time"]
                )
            else:
                player.time_distance_from_start += (
                    ","
                    + "feedback buy:"
                    + str(finishtime - player.participant.vars["start_time"])
                )


class Feedback_buy_bigloss(Page):
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.price >= group.computer_price and group.reward == -10000

    @staticmethod
    def js_vars(player: Player):
        player.participant.vars["pagecount"] += 1
        # print(player.participant.vars["pagecount"])
        return dict(cnt=player.participant.vars["pagecount"])

    # @staticmethod
    # def before_next_page(player: Player, timeout_happened):
    #     print(player.time_distance_from_start)

    @staticmethod
    def live_method(player: Player, data):
        if data:
            try:
                finishtime = data["finishtime"]
            except Exception:
                print("invalid message received:", data)
                return
            if player.time_distance_from_start == "":
                player.time_distance_from_start = "feedback buy big loss:" + str(
                    finishtime - player.participant.vars["start_time"]
                )
            else:
                player.time_distance_from_start += (
                    ","
                    + "feedback buy big loss:"
                    + str(finishtime - player.participant.vars["start_time"])
                )


class Feedback_notbuy(Page):
    timeout_seconds = 15

    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.price < group.computer_price and group.reward != -10000

    @staticmethod
    def js_vars(player: Player):
        player.participant.vars["pagecount"] += 1
        # print(player.participant.vars["pagecount"])
        return dict(cnt=player.participant.vars["pagecount"])

    # @staticmethod
    # def before_next_page(player: Player, timeout_happened):
    #     print(player.time_distance_from_start)

    @staticmethod
    def live_method(player: Player, data):
        if data:
            try:
                finishtime = data["finishtime"]
            except Exception:
                print("invalid message received:", data)
                return
            if player.time_distance_from_start == "":
                player.time_distance_from_start = "feedback not buy:" + str(
                    finishtime - player.participant.vars["start_time"]
                )
            else:
                player.time_distance_from_start += (
                    ","
                    + "feedback not buy:"
                    + str(finishtime - player.participant.vars["start_time"])
                )


class Feedback_notbuy_bigloss(Page):
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.price < group.computer_price and group.reward == -10000

    @staticmethod
    def js_vars(player: Player):
        player.participant.vars["pagecount"] += 1
        # print(player.participant.vars["pagecount"])
        return dict(cnt=player.participant.vars["pagecount"])

    # @staticmethod
    # def before_next_page(player: Player, timeout_happened):
    #     print(player.time_distance_from_start)

    @staticmethod
    def live_method(player: Player, data):
        if data:
            try:
                finishtime = data["finishtime"]
            except Exception:
                print("invalid message received:", data)
                return
            if player.time_distance_from_start == "":
                player.time_distance_from_start = "feedback not buy big loss:" + str(
                    finishtime - player.participant.vars["start_time"]
                )
            else:
                player.time_distance_from_start += (
                    ","
                    + "feedback not buy big loss:"
                    + str(finishtime - player.participant.vars["start_time"])
                )


class Delay(Page):
    timer_text = "休憩の残り時間は:"

    timeout_seconds = 600

    @staticmethod
    def is_displayed(player):
        group = player.group
        return group.reward == -10000 and player.tail_total == 1

    @staticmethod
    def js_vars(player: Player):
        player.participant.vars["pagecount"] += 1
        # print(player.participant.vars["pagecount"])
        return dict(cnt=player.participant.vars["pagecount"])


# class Adjustment(Page):
#     @staticmethod
#     def is_displayed(player):
#         group = player.group
#         return group.reward == -10000 and player.tail_total == 1

#     @staticmethod
#     def js_vars(player: Player):
#         player.participant.vars["pagecount"] += 1
#         print(player.participant.vars["pagecount"])
#         return dict(cnt=player.participant.vars["pagecount"])


class OverdraftHappened(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.overdraft

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            download_name="timedelay_player_" + str(player.id_in_subsession),
        )

    @staticmethod
    def js_vars(player: Player):
        player.participant.vars["pagecount"] += 1
        # print(player.participant.vars["pagecount"])
        # print([x + 1 for x in range(player.participant.vars["pagecount"])])
        return dict(
            cnt=player.participant.vars["pagecount"],
            list=[x + 1 for x in range(player.participant.vars["pagecount"])],
            download_name="timedelay_player_" + str(player.id_in_subsession),
        )

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        # print("upcoming_apps is", upcoming_apps)
        if player.overdraft is True:
            return "Survey"


class Result(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number >= 10

    @staticmethod
    def js_vars(player: Player):
        player.participant.vars["pagecount"] += 1
        # print(player.participant.vars["pagecount"])
        return dict(cnt=player.participant.vars["pagecount"])


class temptest4(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number >= 10

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            download_name="timedelay_player_" + str(player.id_in_subsession),
        )

    @staticmethod
    def js_vars(player: Player):
        player.participant.vars["pagecount"] += 1
        # print(player.participant.vars["pagecount"])
        # print([x + 1 for x in range(player.participant.vars["pagecount"])])
        return dict(
            cnt=player.participant.vars["pagecount"],
            list=[x + 1 for x in range(player.participant.vars["pagecount"])],
        )


class WaitPage(WaitPage):
    pass


page_sequence = [
    test1,
    Investment1,
    Investment2,
    WaitPage1,
    WaitPage2,
    can_buy,
    cannot_buy,
    Feedback_buy,
    Feedback_buy_bigloss,
    Feedback_notbuy,
    Feedback_notbuy_bigloss,
    Delay,
    OverdraftHappened,
    Result,
    # temptest4,
]
