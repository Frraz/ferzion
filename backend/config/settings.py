import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Segurança
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "unsafe-dev-key")

DEBUG = False  # 🚨 produção

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "ferzion.com.br",
    "www.ferzion.com.br",
]

# 🌐 CORS (frontend pode acessar API)
CORS_ALLOW_ALL_ORIGINS = True  # pode restringir depois

# 📦 Apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "leads",
]

# ⚙️ Middleware
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",  # mantém (admin usa)
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# 🧠 Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# 🗄️ Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 🔑 Passwords
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# 🌍 Locale
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True
USE_TZ = True

# 📦 Static
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# 🚀 DRF (AQUI ESTÁ A CHAVE DO SEU PROBLEMA)
REST_FRAMEWORK = {
    # 🔥 remove CSRF da API (profissional)
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    # API pública (formulário)
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}
