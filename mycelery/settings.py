"""
Django settings for mycelery project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!0nl$sxp@73vm!4jml^+f&qx1tol9p_sp_ioz=n1ivlns&lws^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'cacheback',
    'main',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mycelery.urls'

WSGI_APPLICATION = 'mycelery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Chongqing'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] [pid:%(process)d] [%(name)s] %(levelname)s %(message)s [%(pathname)s:%(lineno)s]",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/all.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'cacheback': {
            'handlers': ['file'],
            'propagate': False,
            'level': 'INFO',
        },
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },

    }
}

import djcelery
djcelery.setup_loader()
BROKER_URL = 'redis://127.0.0.1:6379/2'
# CELERY_RESULT_BACKEND = None
CELERYD_CONCURRENCY = 3
# CELERY_MONGODB_BACKEND_SETTINGS = None
CELERY_IGNORE_RESULT = True
# CELERY_CACHE_BACKEND = 'memory'

from kombu import Exchange, Queue

CELERY_DEFAULT_QUEUE = 'mycelery'
CELERY_QUEUES = (
    Queue('mycelery', Exchange('mycelery'), routing_key='mycelery'),
)

CELERY_DEFAULT_EXCHANGE = 'mycelery'
# CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_ROUTING_KEY = 'mycelery'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


CELERYD_LOG_FILE = "ss.log"
CELERYD_HIJACK_ROOT_LOGGER = False
CELERYD_LOG_FORMAT = "[%(asctime)s] [pid:%(process)d] [%(name)s] %(levelname)s %(message)s [%(pathname)s:%(lineno)s]"
CELERYD_TASK_LOG_FORMAT = CELERYD_LOG_FORMAT
