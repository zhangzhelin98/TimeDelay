import time
from otree.api import models, widgets, BasePlayer

class MyPlayer(BasePlayer):
    button_pressed_time = models.FloatField()

    def record_button_pressed_time(self):
        # 记录按下按钮的时间
        self.button_pressed_time = time.time()