import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-hahha'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # MAIL_SERVER = 'localhost'
    # MAIL_PORT = 8025

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '975713384@qq.com'
    MAIL_PASSWORD = 'aglkdfaevuglbeia'  # 2020年05月09日
    ADMINS = ['975713384@qq.com']

    POSTS_PER_PAGE = 2

    LANGUAGES = ['zh', 'en', 'es']

    TRANSLATOR_APPID = 20200517000459357
    TRANSLATOR_KEY = 'wHmHeGsnxCkettyrBq5U'

    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')

    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
