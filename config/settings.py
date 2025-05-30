"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$-vjfjw$q28-e43syu^#dovi#+o+hqc=s$mmfkrc^o$-)cvhgx'

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
    
    'djoser',  # 用户模块
    'rest_framework',
    'django_filters',
    'account',
    'movie',
    'trade'
    
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'movies',
        'USER': 'root',
        'PASSWORD':'rsk123456',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
LOCALE_PATHS=[
    Path(BASE_DIR).joinpath('locale')
]

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 设置分页样式
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12 ,

    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        # ...
    ),

    # 配置jwt认证
     'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# 配置jwt

from datetime import timedelta
SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',), # 头部信息
   'ACCESS_TOKEN_LIFETIME':timedelta(minutes=60), # 配置访问令牌的生命周期
   'REFRESH_TOKEN_LIFETIME':timedelta(days=14),   # 刷新令牌的生命周期
}


# 邮箱配置

EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True


EMAIL_HOST_PASSWORD = 'PHTptwr49GLZWb8j'
EMAIL_HOST_USER='rskrongshaokai@163.com'
DEFAULT_FROM_EMAIL='rskrongshaokai@163.com'




# djsoer 配置
DJOSER = {
    'USER_ID_FIELD':'username',
    'USER_ID_FIELD':'email',
    'SEND_ACTIVATION_EMAIL':True,
    'ACTIVATION_URL':'activate/{uid}/{token}',
    'SEND_CONFIRMATION_EMAIL':True,
    'PASSWORD_RESET_CONFIRM_URL':'password_reset/{uid}/{token}',
    'PASSWORD_RESET_CONFIRM_RETYPE':True,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND':True,
    'SET_PASSWORD_RETYPE':True,
    

    'SERIALIZERS':{
        "user_create": "account.serializers.CustomUserCreateSerializer",
        "current_user": "account.serializers.CustomSerializer",
    }
}


# 配置支付宝沙箱环境

# 支付宝网关地址
ALIPAY_SERVER_URL = "https://openapi-sandbox.dl.alipaydev.com/gateway.do"
# appid
ALIPAY_APP_ID = '2021000148606856'
# 私钥
ALIPAY_APP_PRIVATE_KEY='MIIEogIBAAKCAQEAgSnDN5arK6aZsMLBRClaHvu8+n3fIvaoW8RQbisPKAhM57KTEcljb1FB4YlmIREiO/9vEGyhJnN6v97mmKqgMPOWuXtDOE5M9VIe/XX5p6/R9sTpgS+T7hh9ZxoO2pGkorjiv6bkC25Lp0tMFfVO/+SD6lLRzYYccFs/TNm/BeDnPsNCKbSYTtLHSje+toNIWFULBf2+UolgzyFwVkwa2kHOANcZ0ygIaJh/oYw/U7Ipof4UWz9LVufEvOXdXcGMM8KoqoYY2aag8CmFWcqvhTeogEXquXIORX0cqXBCV5W2t8HCbVgb99C2+sibJkjgdruZGiLsXiGNQ2UYAZBzHwIDAQABAoIBACRD9pUID918tJBlzl/2AGDMq93lM56chN7nOvID0wiZdAZmJFcNJYce2JGbw3orVmJkMOn6pjCmoeN3kWVyGvJDoqFHk7MegQssWJkv474KZriTx0BHfJCQfb1SGrORyxkJMlk/Ya439LPvN1i+/MRqhANp55B+REPjyt0oEjNy8SimM39P/zQLDi5P3lwavJ5iLXJdASeAbOy/dU+uM7EglDsnMIFGgFje5o4Km0dz4oB7/8NIjb4rHLmRzxjRKDHUoPyf88HRsW8LMsnHe/abr9/iSWqVwvQbR5+4MrJFdwTzcivC+dnYY9qrErSxfGL+wGblJee6CXO3NjHWyEECgYEAvU1/V9tSTyzv5S4v5xtmc+iC9kNo+6x6sj2huLXWmgRc6dzfhxcDgiZ3Ux9oyKYvu4w6RtX2F/REeMgrLy3QN018ktkn63Uoae0vuSV6m8CRMGOtrckWv2qgl3nvCD1IatGtisJEkoyIXWWDjGw8eIy7l1GT26iWfhqoCZtYOv8CgYEArqvdpNzhb9Jm2iH04mNoDrMlIDruFX1CKlRkC4CF7bHQ1q1YVoCOZvbjc/oBKlOJVMX/rYhJXgfDzBtCQqL3STMO4kFgZeEuvpANLgkuUNBiGPUmrojVNsK7+CD/K0slTvtCy0nlniMPgi2m7N4UIElzR1X7x1Zl2vMjnm64Z+ECgYAZ9XWf+6Bm4ReoitPg0j4TaPAEiyvrTzSoGpGBvdXG2xBOtY4lfT9q6pF0YZtB4KAtDMa1DgQoNsPo+DILzzF9U+/gR00VGcTH+dGQhxYwI5EFXLXlXezzpNCO1Ra1P4ods9EjdQ5oNkNA43nNmM4WDd5vmq028wBoHImsf5PyywKBgCnv+8RUgA/wDV+8HWaphVdaLcTCQV2JeHRfVLHqRr2eHs0cS4RhU09nYY777IG0Etn2u/93JF5eMOV1egAzznmVt7IdDj8HxMheH7v42lTu406otYPcOIzwTl8x1PIZFbkT3KKgeG/ybQvNWDGw1FY4LGRpQY1HsibSj6+/V6khAoGAEC6LoYcb3ECSipqcE0KyOiyOeEhA11N2BL7oD0lqThXZ6AX9yqTrEh37rvOhvT25pSlNNTl2auSIIuUCJCvISui4AqJmRmKHjP8ijQ2c+HXq9HwLkwqTfItuOjEVTtUSVcheGkqVznlseKAgEvgytwD2309h5oA/b73BRsJKr8M='
# 公钥
ALIPAY_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3jtiUX+MOO9yV7ixlxPOpx1+CSJXXzb/hKLLonI+yTvUpLPKPG3E//TFqfg7537s7O25aCot54ViJMTOzIFBX+5MPx4Wi5zMyMtno7P91fLjVsmzO/etZxUk85pJFiGJd8FWjftBSwp/bU1p7dki3VDo+vTYbIaEXtoW4+ZV7Y1/GW2LX9Olh8Bqq+rNhcA8zzZhJPtzdlcybSBDWWA3ZXUEeopovadzDwdr6Yz14eESFiiRmZCkEgKq80bQb5T30+ftCI3tSsnIR1w61Uy9JMoC3kfrJLHxD+NB4Hv7ZK0JQmmptALEMRWnCVgqGG35+X0k9Qw6U+05heGXhtbMkwIDAQAB'

# return url
ALIPAY_RETURN_URL = 'http://3efa2efa.r30.cpolar.top/orders/'

# notify url
ALIPAY_NOTIFY_URL = 'http://3efa2efa.r30.cpolar.top/api/callback/'

#seller_id
ALIPAY_SELLER_ID = '2088721065226131'

