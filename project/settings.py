"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


ON_PAAS = 'SUNORTH_IN_PRODUCTION' in os.environ

if ON_PAAS:
    SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']
else:
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = ')_7av^!cy(wfx=k#3*7x+(=j^fzv+ot^1@sh9s9t=8$bu@r(z$'

# SECURITY WARNING: don't run with debug turned on in production!
# adjust to turn off when on Openshift, but allow an environment variable to override on PAAS
DEBUG = not ON_PAAS
DEBUG = DEBUG or os.getenv("debug","false").lower() == "true"

if ON_PAAS and DEBUG:
    print("*** Warning - Debug mode is on ***")

# DEBUG=False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',  
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'django_select2',
    'ckeditor',
    'ckeditor_uploader',
    'sorl.thumbnail',
    'rest_framework',
    'avatar',
    'userprofile',
    'blog',
    'activity',
    'gallery',
    'book',
    'club',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',

)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # 'social.apps.django_app.context_processors.backends',
                # 'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# if ON_PAAS:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':     os.environ['MYSQL_DB'],
        'USER':     os.environ['MYSQL_DB_USERNAME'],
        'PASSWORD': os.environ['MYSQL_DB_PASSWORD'],
        'HOST':     os.environ['MYSQL_DB_HOST']
    }
}


        
# else:
#     # stock django, local development.
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         }
#     }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'America/Vancouver'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
LANGUAGES = (
    ('en-us', _('English')),
    ('zh-cn', _('Simple Chinese')), # instead of 'zh-CN'
    ('zh-tw', _('Traditional Chinese')), # instead of 'zh-TW'
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'wsgi','static')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR,"static"),
)
if ON_PAAS:
    MEDIA_ROOT = os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), 'media')
    MEDIA_URL = '/static/media/'
else: 
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
    MEDIA_URL = '/media/'


CRISPY_TEMPLATE_PACK = 'bootstrap3'

SITE_ID=1
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/signin/'

CKEDITOR_UPLOAD_PATH='uploads/'
CKEDITOR_IMAGE_BACKEND='pillow'
CKEDITOR_RESTRICT_BY_USER=True
CKEDITOR_CONFIGS = {
    'default': {
        'height':'300',
        'width':'100%',
        'selectMultiple':'true',
        'toolbar': 'sun',
        'toolbar_sun': [
              {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote',  '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink']},
            {'name': 'insert',
             'items': ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
        ], 
        'extraPlugins': ','.join(
            [
                # you extra plugins here
                # 'div',
                # 'autolink',
                # 'autoembed',
                # 'embedsemantic',
                # 'autogrow',
                # # 'devtools',
                # 'widget',
                # 'lineutils',
                # 'clipboard',
                # 'dialog',
                # 'dialogui',
                # 'elementspath'
            ]),        
     },
}
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

