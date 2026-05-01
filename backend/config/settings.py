import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔥 Carrega .env
load_dotenv(BASE_DIR / ".env")

# =========================
# 🔐 SEGURANÇA
# =========================

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "unsafe-dev-key")

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS", "127.0.0.1,localhost,ferzion.com.br,www.ferzion.com.br"
).split(",")

# =========================
# 🌐 CORS
# =========================

CORS_ALLOW_ALL_ORIGINS = os.getenv("CORS_ALLOW_ALL", "True").lower() == "true"

# =========================
# 📦 APPS
# =========================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "leads",
]

# =========================
# ⚙️ MIDDLEWARE
# =========================

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# =========================
# 🧠 TEMPLATES
# =========================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",  # 🔥 IMPORTANTE (emails)
        ],
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

# =========================
# 🗄️ DATABASE
# =========================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# =========================
# 🔑 PASSWORDS
# =========================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# =========================
# 🌍 LOCALE
# =========================

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True
USE_TZ = True

# =========================
# 📦 STATIC
# =========================

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# =========================
# 🚀 DRF
# =========================

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

# =========================
# 📧 EMAIL
# =========================

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))

EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True").lower() == "true"
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", "False").lower() == "true"

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)

# Timeout evita travar request
EMAIL_TIMEOUT = 10
