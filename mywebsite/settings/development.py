from decouple import config
from mywebsite.settings.common import *

DEBUG = config('DEBUG', cast=bool)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + '/db.sqlite3',
    }
}
