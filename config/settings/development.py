from .base import *

DEBUG = True
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # },
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "promag_groupe_dev",
        "USER": "postgres",
        "PASSWORD": 'user',
        "HOST": "localhost",
        "PORT": "",
    }
}
