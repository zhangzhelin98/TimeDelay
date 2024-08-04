from os import environ
import os


# 获取项目的根目录
# settings.py

# 导入 os 模块
import os

# 获取项目的根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SESSION_CONFIGS = [
#     dict(
#         name="TimeDelay",
#         app_sequence=[
#             "introduction",
#             "CalculationTask",
#             "InvestmentTaskIntro",
#             "ComprehensionTest",
#             "webcam",
#             "InvestmentTask",
#             "Survey",
#             "CRT",
#             "STEM",
#             "Result",
#         ],
#         num_demo_participants=1,
#     ),
# ]

SESSION_CONFIGS = [
    dict(
        name='TimeDelay',
        app_sequence=["CalculationTask","InvestmentTaskIntro","ComprehensionTest","InvestmentTask"],
        num_demo_participants=1,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    "expiry",
    "reward_effort",
    "reward_cal",
    "reward_plus1000",
    "profit",
    "overdraft",
    "keep_end",
    "money",
    "money1",
    "payoff_end",
    "initial",
    "payoff_end1",
]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = "ja"

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = "JPY"
USE_POINTS = False

ROOMS = [
    dict(name="pclab", display_name="pclab", participant_label_file="_rooms/pclab.txt")
]


ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = "4500948767192"
# 设置 STATIC_ROOT 为视频文件的保存路径
STATIC_ROOT = os.path.join(BASE_DIR, "_static", "video")
