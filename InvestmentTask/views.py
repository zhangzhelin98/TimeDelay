from otree.api import Page

class Investment1(Page):
    def vars_for_template(self):
        return {}

    def before_next_page(self):
        # 在页面切换前将按钮按下的时间保存到模型中
        self.player.button_pressed_time = time.time()

    def live_method(self, data):
        # 在接收到实时消息时保存当前时间到模型中
        if 'button_pressed' in data:
            self.player.button_pressed_time = time.time()

    def js_vars(self):
        # 将按钮按下的时间发送到前端
        return {
            'button_pressed_time': self.player.button_pressed_time
        }