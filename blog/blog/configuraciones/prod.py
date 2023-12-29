from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['leoogonzalezz.pythonanywhere.com']
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'leoogonzalezz$default',
        'USER': 'leoogonzalezz',
        'PASSWORD': 'Fixinit1',
        'HOST': 'leoogonzalezz.mysql.pythonanywhere-services.com',
        'PORT': '',
    }
}