"""
Django settings for demo1 project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^)tahd$ia7=ui+06yo%oi9bm6w%smg&!1u^5!d6*e5@(b2f$w_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
# DEBUG = False
# ALLOWED_HOSTS = ['*']

# Application definition
#注册项目应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    #这个是启用sessions的时候要用到的
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booktest',
    'votetest'
]
#中间件：提供默认自带功能。
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #note:这个dirs就是templates的绝对路径。
        'DIRS': [os.path.join(BASE_DIR,'templates')], #note:这个路径文件就是G:\奇酷实训\文件三阶段\lichu\demo1+templates
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

WSGI_APPLICATION = 'demo1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
#数据库配置
#Django默认使用sqlite3数据库，sqlite3是一个文件型的数据库，是一个轻量级的数据库。
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

STATIC_PATH = os.path.join(os.path.join(BASE_DIR,'static'))
STATICFILES_DIRS = (
    STATIC_PATH,
)
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR,'static/media')

#使用redis存储session 如果不想使用redis存储可以注释掉这些配置。  note：（一些大型的项目一般都是用redis存储的）
SESSION_ENGINE = 'redis_sessions.session' #指定session的存储方式为redis存储
SESSION_ENDIS_HOST = 'localhost' #指定要连接的哪个电脑上的redis
SESSION_REDIS_PORT = 6379 #端口号
SESSION_REDIS_DB = 0 #指定数据库0
SESSION_REDIS_PASSWORD = '' #授权密码
SESSION_REDIS_PREFIX= 'session' #前缀
#Django使用redis(我们配的另一个是cookie存储使用redis)
CACHES = {
    'default' : {
        'BACKEND':'redis_cache.cache.RedisCache',
        'LOCATION':'localhost:6379',
        'TIMEOUT':100, #默认存储时间 以秒为单位
    }
}



