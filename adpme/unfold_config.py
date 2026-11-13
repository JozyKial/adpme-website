# ==========================================================================
# ADPME Congo — unfold_config.py — v3
# Fonctions appelées par le thème d'administration Unfold (voir UNFOLD dans
# settings.py) : badge d'environnement, icône, menu latéral, tableau de bord.
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
        "title": "Textes et listes",
        "separator": True,
        "collapsible": False,
        "items": [
            _lien("Textes du site", "edit_note", "textesite"),
            _lien("Listes (accès rapides, services, étapes)", "format_list_bulleted", "element"),
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



def tableau_de_bord(request, context):
    """Données de la page d'accueil de l'administration (templates/admin/index.html)."""
    from django.db.models import Q
    from django.urls import reverse

    from .models import AgenceInfo, BlocAccueil, BlogActualite, ChiffreCle, Document, FAQ, Programme

    agence = AgenceInfo.objects.first()
    vigilance = []
    if not agence:
        vigilance.append(("Les informations de l'agence ne sont pas encore saisies.", reverse("admin:adpme_agenceinfo_add")))
    else:
        manquants = [nom for nom, valeur in [
            ("téléphone", agence.phone), ("e-mail", agence.email_contact), ("adresse", agence.adresse),
            ("horaires", agence.horaires), ("carte Google Maps", agence.carte_embed_url),
        ] if not valeur]
        if manquants:
            vigilance.append((f"Coordonnées à compléter : {', '.join(manquants)}.",
                              reverse("admin:adpme_agenceinfo_change", args=[agence.pk])))
    sans_image = BlocAccueil.objects.filter(Q(image="") | Q(image__isnull=True), actif=True).count()
    if sans_image:
        vigilance.append((f"{sans_image} bloc(s) de la page d'accueil sans photo.", reverse("admin:adpme_blocaccueil_changelist")))
    if not ChiffreCle.objects.filter(actif=True).exists():
        vigilance.append(("Aucun chiffre clé : la section « En chiffres » est masquée.", reverse("admin:adpme_chiffrecle_add")))
    brouillons = BlogActualite.objects.filter(published=False).count()
    if brouillons:
        vigilance.append((f"{brouillons} article(s) en brouillon, non visibles sur le site.",
                          reverse("admin:adpme_blogactualite_changelist") + "?published__exact=0"))

    context.update({
        "indicateurs": [
            {"titre": "Articles publiés", "valeur": BlogActualite.objects.filter(published=True).count(),
             "lien": reverse("admin:adpme_blogactualite_changelist") + "?published__exact=1", "icone": "newspaper"},
            {"titre": "Brouillons", "valeur": brouillons,
             "lien": reverse("admin:adpme_blogactualite_changelist") + "?published__exact=0", "icone": "edit_document"},
            {"titre": "Programmes publiés", "valeur": Programme.objects.filter(actif=True).count(),
             "lien": reverse("admin:adpme_programme_changelist"), "icone": "rocket_launch"},
            {"titre": "Documents publiés", "valeur": Document.objects.filter(actif=True).count(),
             "lien": reverse("admin:adpme_document_changelist"), "icone": "folder_open"},
            {"titre": "Questions fréquentes", "valeur": FAQ.objects.filter(active=True).count(),
             "lien": reverse("admin:adpme_faq_changelist"), "icone": "help"},
        ],
        "raccourcis": [
            {"titre": "Publier une actualité", "lien": reverse("admin:adpme_blogactualite_add"), "icone": "add_circle"},
            {"titre": "Ajouter un document", "lien": reverse("admin:adpme_document_add"), "icone": "upload_file"},
            {"titre": "Modifier les textes du site", "lien": reverse("admin:adpme_textesite_changelist"), "icone": "edit_note"},
            {"titre": "Modifier une page", "lien": reverse("admin:adpme_page_changelist"), "icone": "article"},
            {"titre": "Voir le site", "lien": "/", "icone": "public"},
        ],
        "derniers_articles": BlogActualite.objects.select_related("category").order_by("-date_publication", "-id")[:6],
        "vigilance": vigilance,
    })
    return context

