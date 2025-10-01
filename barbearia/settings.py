# barbearia/settings.py

import os
from pathlib import Path
import dj_database_url

# -----------------------
# Caminho base do projeto
# -----------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------
# Segurança
# -----------------------
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")  # Render injeta automaticamente
DEBUG = os.getenv("DEBUG", "False") == "True"

# -----------------------
# Hosts permitidos
# -----------------------
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "agendabarbearia-web2.onrender.com,agendabarbearia.onrender.com,localhost,127.0.0.1"
).split(",")

# -----------------------
# Aplicativos instalados
# -----------------------
INSTALLED_APPS = [
    # Apps padrão do Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps do sistema de agendamento
    'agenda',
    'django_crispy_forms',  # Forms bonitos e responsivos
]

# -----------------------
# Middleware
# -----------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # servir estáticos no Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------
# Configuração de URLs
# -----------------------
ROOT_URLCONF = 'barbearia.urls'

# -----------------------
# Templates
# -----------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# -----------------------
# WSGI
# -----------------------
WSGI_APPLICATION = 'barbearia.wsgi.application'

# -----------------------
# Banco de dados
# -----------------------
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",  # fallback local
        conn_max_age=600,
        ssl_require=True  # obrigatório no Render com Postgres
    )
}

# -----------------------
# Validação de senhas
# -----------------------
AUTH_PASSWORD_VALIDATORS = [
    # {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    # {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    # {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    # {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -----------------------
# Internacionalização
# -----------------------
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# -----------------------
# Arquivos estáticos
# -----------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -----------------------
# Arquivos de mídia
# -----------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -----------------------
# Tipo padrão para campos AutoField
# -----------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------
# Usuário customizado
# -----------------------
AUTH_USER_MODEL = "agenda.Usuario"

# -----------------------
# URLs de login/logout
# -----------------------
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/agenda/'
LOGOUT_REDIRECT_URL = '/'

# -----------------------
# Email (apenas console no dev)
# -----------------------
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# -----------------------
# Logging básico
# -----------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
