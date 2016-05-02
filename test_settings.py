# -*- coding: utf-8 -*-


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 36000,
        'KEY_PREFIX': 'post-office',
    },
    'email': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 36000,
        'KEY_PREFIX': 'post-office',
    }
}

POST_OFFICE = {
    'BACKENDS': {
        'default': 'django.core.mail.backends.dummy.EmailBackend',
        'locmem': 'django.core.mail.backends.locmem.EmailBackend',
        'error': 'email.tests.test_backends.ErrorRaisingBackend',
        'smtp': 'django.core.mail.backends.smtp.EmailBackend',
        'connection_tester': 'email.tests.test_mail.ConnectionTestingBackend',
    }
}


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'email',
)

SECRET_KEY = 'a'

ROOT_URLCONF = 'email.test_urls'

DEFAULT_FROM_EMAIL = 'webmaster@example.com'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)
