from otree.api import *

import os
import datetime
import base64
import glob
import pathlib


doc = """座席位置調整 """


## 写真を保存するためのディレクトリを作成
photopath = "_static/photo.neutral"
os.makedirs(photopath, exist_ok=True)




class C(BaseConstants):
    NAME_IN_URL = 'webcam'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    blackphoto = models.IntegerField()
    


# class MyModel(ExtraModel):
#     player = models.Link(Player)
#     photostr = models.LongStringField()
#     timestamp = models.StringField()



# PAGES
class MyPage(Page):
    def live_method(player: Player, data):
        photostr = data["photostr"]
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
        

        # os.path.getsize()でファイルのサイズ取得

        ## 受け取ったBASE64形式の写真データからプレフィックスを取り除いてから，バイナリに変換する
        prefixstr = "data:image/jpeg;base64,"
        img = base64.b64decode(photostr.replace(prefixstr, "").encode())
        

        ## バイナリをjpgファイルに書き出す
        with open("{}/{}_{}.jpg".format(photopath, player.participant.code, timestamp), mode='bw') as f:
            f.write(img)
        photosize = os.path.getsize("{}/{}_{}.jpg".format(photopath, player.participant.code, timestamp))
        if photosize < 204800:
            player.blackphoto = 1
        else :
            player.blackphoto = 0

        
        # ExtraModelにBASE64形式の写真データを記録する（しなくても良い）
        # MyModel.create(
        #     player = player,
        #     photostr = photostr,
        #     timestamp = timestamp
        # )



    @staticmethod
    def error_message(player: Player, values):
        if player.blackphoto == 1:
            return "通信エラーが発生しました。もう一度写真を撮ってください。"




class Results(Page):
    pass

page_sequence = [MyPage]


def vars_for_admin_report(subsession: Subsession):
    files = {}
    for p in subsession.get_players():
        code = p.participant.code
        pnumber = p.participant.id_in_session
        tmplist = ["{}/{}".format(pathlib.Path(x).parents[0].name, pathlib.Path(x).name) for x in glob.glob("{}/{}_*.jpg".format(photopath, code))]
        files[pnumber] = tmplist

    return dict(
        files = files
    )

# def custom_export(players: list[Player]):
#     yield ["session.code", "player.id_in_subsession", "timestamp", "photostr"]

#     for p in players:
#         records_list: list[MyModel] = MyModel.filter(player = p)
#         for record in records_list:
#             yield [p.session.code, p.id_in_subsession, record.timestamp, record.photostr]
