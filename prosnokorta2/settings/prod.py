from prosnokorta2.settings.dev import SECRET_KEY
from .common import *
import os

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['prosnokorta.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        
        # 'NAME': 'freedb_prosnokorta4',
        # 'HOST': 'sql.freedb.tech',
        # 'USER': 'freedb_abulkuddus343',
        # 'PASSWORD': 'S2e6@aK$Rt$x3Du',

        'NAME': 'prosnokorta2',
        'HOST': 'mysql-91149-0.cloudclusters.net',
        'USER': 'sakdfj45934jfjs',
        'PASSWORD': 'skdjf*&*$Wskdjf',

        # 'OPTIONS': {
        #     'init_command': 'SET default_storage_engine=INNODB',
        #     # 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        # }
    }
}