from otree.db import models

class Player(models.BasePlayer):
    video_file_path = models.StringField()
