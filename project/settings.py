import os
import sys
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-ti-prtjm(d_p7ve!r(g&4&(=+*_vn*x+*3z^ge567i72tr-5)1')
DEBUG = True
ALLOWED_HOSTS = ["*"]

# 💡 마이크로서비스 경로 추가 (Runtime 에러 방지)
sys.path.append(os.path.join(BASE_DIR, "user-service"))
sys.path.append(os.path.join(BASE_DIR, "story-service"))
sys.path.append(os.path.join(BASE_DIR, "activity-service"))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'corsheaders',
    'subway',   
    'stories',
    'library',
    'pages',
    'rest_framework',
    'storages',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'

# 💡 DB_HOST가 없을 때를 대비한 방어적 설정 (부팅 지연 해결)
DB_HOST_ENV = os.getenv("DB_HOST", "localhost")
if ":" in DB_HOST_ENV:
    DB_HOST, DB_PORT = DB_HOST_ENV.split(":")
else:
    DB_HOST = DB_HOST_ENV
    DB_PORT = os.getenv("DB_PORT", "3306")

print(f"DEBUG: DB_HOST={DB_HOST}, DB_PORT={DB_PORT}")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "hisubtory_db",
        "USER": os.getenv("DB_USER", "admin"),
        "PASSWORD": os.getenv("DB_PASSWORD", "hisadmin"),
        "HOST": DB_HOST,
        "PORT": DB_PORT,
        "OPTIONS": {
            "connect_timeout": 5,
        },
    }
}

# 💡 Redis를 로컬 메모리 캐시로 임시 대체하여 부팅 실패 방지 (연결 확인 후 Redis로 전환)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.db"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.User'
