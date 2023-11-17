from otree.api import urlpatterns
from .views import SaveVideo

urlpatterns.append(SaveVideo.as_view(), name='save_video')

from otree.api import Page

class test1(Page):
    def vars_for_template(self):
        return {
            'participant_code': self.player.participant.code,
        }

class test2(Page):
    def vars_for_template(self):
        return {
            'participant_code': self.player.participant.code,
        }

class Page3(Page):
    def vars_for_template(self):
        return {
            'participant_code': self.player.participant.code,
        }
