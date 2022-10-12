from prosnokorta2.settings.dev import SECRET_KEY
from .common import *
import os

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['prosnokorta.herokuapp.com']