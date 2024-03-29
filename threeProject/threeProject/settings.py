"""
Django settings for threeProject project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os,sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR,'extract_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd_sve5d48e2y2f4hl)i2y4x))a_@cmj#r_f=zqdcs=kw8m$-1d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sadia',
    'haystack',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'threeProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'threeProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
#使用mysql数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sadia',#自己建立的数据库名字,
        'USER':'root',#用户名
        'PASSWORD':'root',#密码
        'HOST':'localhost',
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans' #中文
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai' #上海的时区 （note：改时区很重要）

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
#配置静态资源
# STATIC_URL = '/assets/'
STATIC_URL = '/assets/'
STATICFILES_DIRS=(os.path.join(BASE_DIR,'assets'),)
#配置上传文件路径media
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

HAYSTACK_CONNECTIONS = {
    'default': {
    'ENGINE': 'sadia.whoosh_cn_backend.WhooshEngine',
    'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

#Django发送邮件配置相关参数
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True #是否使用TLS安全传输协议(用于在两个通信应用程序之间提供保密性和数据完整性。)
EMAIL_USE_SSL = False #是否使用SSL加密，qq企业邮箱要求使用  note:这两个只能有一个为True
EMAIL_HOST = 'smtp.163.com' #发送邮件的邮箱 的 SMTP服务器，这里用了163邮箱 （每一个邮箱的运营商服务器地址都不一样，可以自己百度一个）
EMAIL_PORT = 25 #发件箱的SMTP服务器端口
EMAIL_HOST_USER = 'b1278822679@163.com' #发送邮件的邮箱地址
EMAIL_HOST_PASSWORD = 'a1278822679' #邮箱的密码 (note：163邮箱默认客户端授权是关闭的，要在设置中开启，这个是授权码)
DEFAULT_FROM_EMAIL = 'lc0371 <b1278822679@163.com>' #默认显示的谁发的邮件(格式不能乱写，内容可以自己设置)
