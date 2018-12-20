from decouple import config
import dj_database_url
from mywebsite.settings.common import *

DEBUG = config('DEBUG', default=False, cast=bool)

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
