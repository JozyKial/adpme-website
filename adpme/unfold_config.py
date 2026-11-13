# ==========================================================================
# ADPME Congo — unfold_config.py — v2
# Fonctions appelées par le thème d'administration Unfold (voir UNFOLD dans
# settings.py) : badge d'environnement, icône, menu latéral.
# ==========================================================================
from django.conf import settings
from django.templatetags.static import static
from django.urls import reverse_lazy


def environnement(request):
    """Badge affiché en haut de l'admin : rappelle si l'on travaille en local ou en ligne."""
    if settings.DEBUG:
        return ["Développement (local)", "warning"]
    return ["Site en ligne", "success"]


def icone(request):
    return static("assets/images/adpme-fav.png")


def _lien(titre, icone, modele):
    return {
        "title": titre,
        "icon": icone,  # nom d'icône Material Symbols : https://fonts.google.com/icons
        "link": reverse_lazy(f"admin:adpme_{modele}_changelist"),
    }


NAVIGATION = [
    {
        "title": "Tableau de bord",
        "separator": False,
        "items": [
            {"title": "Accueil de l'administration", "icon": "dashboard", "link": reverse_lazy("admin:index")},
            {"title": "Voir le site", "icon": "public", "link": "/"},
        ],
    },
    {
        "title": "Actualités",
        "separator": True,
        "collapsible": False,
        "items": [
            _lien("Articles", "newspaper", "blogactualite"),
            _lien("Catégories", "sell", "category"),
        ],
    },
    {
        "title": "Page d'accueil",
        "separator": True,
        "collapsible": True,
        "items": [
            _lien("Bandeau (slides)", "view_carousel", "slide"),
            _lien("Blocs éditoriaux", "dashboard_customize", "blocaccueil"),
            _lien("Parcours « Vous êtes… »", "alt_route", "parcours"),
            _lien("Chiffres clés", "monitoring", "chiffrecle"),
            _lien("Partenaires", "handshake", "partenaire"),
        ],
    },
    {
        "title": "Contenus",
        "separator": True,
        "collapsible": True,
        "items": [
            _lien("Pages (agence et services)", "article", "page"),
            _lien("Programmes", "rocket_launch", "programme"),
            _lien("Documents à télécharger", "folder_open", "document"),
            _lien("Questions fréquentes", "help", "faq"),
            _lien("Discours", "record_voice_over", "discours"),
        ],
    },
    {
        "title": "L'agence",
        "separator": True,
        "collapsible": True,
        "items": [
            _lien("Informations et coordonnées", "apartment", "agenceinfo"),
            _lien("Antennes", "location_on", "antenne"),
        ],
    },
    {
        "title": "Accès",
        "separator": True,
        "collapsible": True,
        "items": [
            {"title": "Utilisateurs", "icon": "person", "link": reverse_lazy("admin:auth_user_changelist")},
            {"title": "Groupes et droits", "icon": "group", "link": reverse_lazy("admin:auth_group_changelist")},
        ],
    },
]

