from pathlib import Path
import os
from decouple import config, Csv


# ── Chemins ────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent


# ── Sécurité ───────────────────────────────────────────────────────
SECRET_KEY      = config('SECRET_KEY')
DEBUG           = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS   = config('ALLOWED_HOSTS', cast=Csv())


# ── Applications ───────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Bibliothèques tierces
    'ckeditor',
    'ckeditor_uploader',
    'sorl.thumbnail',
    'compressor',

    # Rechargement auto en développement uniquement
    'django_browser_reload',

    'adpme',
]


# ── Middleware ─────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# BrowserReload uniquement en développement
if DEBUG:
    MIDDLEWARE.append('django_browser_reload.middleware.BrowserReloadMiddleware')


ROOT_URLCONF = 'adpme_project.urls'


# ── Templates ──────────────────────────────────────────────────────
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'adpme.context_processors.agence_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'adpme_project.wsgi.application'


# ── Base de données ────────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE':   config('DB_ENGINE'),
        'NAME':     config('DB_NAME'),
        'USER':     config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST':     config('DB_HOST'),
        'PORT':     config('DB_PORT'),
        'OPTIONS': {
            'auth_plugin': config('DB_AUTH_PLUGIN', default=None),
        } if config('DB_AUTH_PLUGIN', default=None) else {}
    }
}


# ── Validation des mots de passe ───────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ── Internationalisation ───────────────────────────────────────────
LANGUAGE_CODE    = 'fr-FR'
TIME_ZONE        = 'Africa/Brazzaville'
USE_I18N         = True
USE_TZ           = True


# ── Fichiers statiques ─────────────────────────────────────────────
STATIC_URL          = '/static/'
STATICFILES_DIRS    = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT         = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]


# ── Fichiers médias ────────────────────────────────────────────────
MEDIA_URL   = '/media/'
MEDIA_ROOT  = BASE_DIR / 'media'


# ── CKEditor ───────────────────────────────────────────────────────
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike'],
            ['NumberedList', 'BulletedList'],
            ['Outdent', 'Indent'],
            ['Link', 'Unlink'],
            ['Image', 'Table'],
            ['Format', 'Styles'],
            ['RemoveFormat'],
            ['Source'],
        ],
        'height': 300,
        'width': '100%',
    }
}


# ── Email ──────────────────────────────────────────────────────────
CONTACT_EMAIL       = config('CONTACT_EMAIL', default='dg-adpme@adpme.cg')
DEFAULT_FROM_EMAIL  = config('DEFAULT_FROM_EMAIL', default='noreply@adpme.cg')

if DEBUG:
    # Développement : affiche les emails dans le terminal
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    # Production : envoi SMTP réel
    EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST          = config('EMAIL_HOST', default='smtp.gmail.com')
    EMAIL_PORT          = config('EMAIL_PORT', default=587, cast=int)
    EMAIL_USE_TLS       = config('EMAIL_USE_TLS', default=True, cast=bool)
    EMAIL_HOST_USER     = config('EMAIL_HOST_USER', default='')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')


# ── Divers ─────────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

