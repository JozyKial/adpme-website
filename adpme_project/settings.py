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
    # Thème de l'administration 
    'unfold',

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
                'adpme.context_processors.navigation',
                'adpme.context_processors.textes_site',
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
STATICFILES_DIRS    = []
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




# ==========================================================================
# Administration : thème Unfold aux couleurs de l'ADPME
# Menu latéral et badge d'environnement : adpme/unfold_config.py
# ==========================================================================
from adpme.unfold_config import NAVIGATION as UNFOLD_NAVIGATION  # noqa: E402

# Après connexion à l'admin, on arrive sur son tableau de bord
LOGIN_REDIRECT_URL = "admin:index"

UNFOLD = {
    "SITE_TITLE": "ADPME Congo — Administration",
    "SITE_HEADER": "ADPME Congo",
    "SITE_SUBHEADER": "Gestion du site web",
    "SITE_URL": "/",
    "SITE_ICON": "adpme.unfold_config.icone",
    "SITE_FAVICONS": [
        {"rel": "icon", "sizes": "32x32", "type": "image/png", "href": "adpme.unfold_config.icone"},
    ],
    "ENVIRONMENT": "adpme.unfold_config.environnement",
    "DASHBOARD_CALLBACK": "adpme.unfold_config.tableau_de_bord",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "BORDER_RADIUS": "8px",
    "COLORS": {
        # Vert ADPME (#336633 = 600)
        "primary": {
            "50": "oklch(97.5% .012 144)",
            "100": "oklch(94% .025 144)",
            "200": "oklch(89% .045 144)",
            "300": "oklch(81% .07 144)",
            "400": "oklch(68% .095 144)",
            "500": "oklch(56% .105 144)",
            "600": "oklch(46.1% .097 143.8)",
            "700": "oklch(38.8% .078 143.9)",
            "800": "oklch(32.8% .063 144)",
            "900": "oklch(27% .05 144)",
            "950": "oklch(20% .04 144)",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": UNFOLD_NAVIGATION,
    },
}


