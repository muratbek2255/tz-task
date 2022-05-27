# SECURITY WARNING: keep the secret key used in production secret!
from pathlib import Path

SECRET_KEY = 'django-insecure-67nbebd#1vz(w6g3&d%k#yr7(f%l8hmikgu$n(1k4i5+o1ws&g'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}