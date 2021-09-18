from .base import *  # noqa: F401


# Project Artitecture Constants
DEBUG = True
ALLOWED_HOSTS = ['*']

# Business Logic Constants
BANK_IP = '20.98.98.0'
MIN_TNBC_ALLOWED = 5  # In TNBC
MAAKAY_TOURNAMENT_CHANNEL_ID = 888647452499009536
MAAKAY_MINIMUM_TOURNAMENT_AMOUNT = 1000000000

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
