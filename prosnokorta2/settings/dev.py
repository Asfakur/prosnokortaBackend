from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--@evii#!zgrggen))n_zd=50@r16insh8!e_ey=0a^^bw52udj'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prosnokorta3',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '',
        # 'NAME': 'freedb_prosnokorta4',
        # 'HOST': 'sql.freedb.tech',
        # 'USER': 'freedb_abulkuddus343',
        # 'PASSWORD': 'S2e6@aK$Rt$x3Du',
        # 'OPTIONS': {
        #     'init_command': 'SET default_storage_engine=INNODB',
        #     # 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        # }
    }
}