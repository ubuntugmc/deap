import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'dev'
DEBUG = True
INSTALLED_APPS = ['pipeline']
DATABASES = {'default': {'ENGINE':'django.db.backends.sqlite3','NAME': str(BASE_DIR/'data'/'db.sqlite3')}}
