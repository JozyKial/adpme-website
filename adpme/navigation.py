# ==========================================================================
# ADPME Congo — navigation.py — v7
# Menu principal du site : C'EST ICI qu'on modifie le méga-menu ET les
# colonnes du footer (une seule source pour les deux).
#
#   - Une rubrique avec "liens" devient un méga-menu (et une colonne du footer).
#   - Une rubrique avec "url" devient un lien direct.
#   - "url" = nom de route Django (name="..." dans adpme/urls.py).
#   - "icone" = nom d'une icône de adpme/templatetags/ui.py.
#   - "aussi" = autres routes qui allument la rubrique (ex. détail d'actualité).
# ==========================================================================

MENU_PRINCIPAL = [
    {
        "id": "agence",
        "titre": "L'Agence",
        "liens": [
            {"titre": "Présentation", "url": "a_propos", "icone": "batiment"},
            {"titre": "Mot du Directeur général", "url": "discours_dg", "icone": "message"},
            {"titre": "Mot de la Ministre", "url": "discours_ministre", "icone": "message"},
        ],
    },
    {
        "id": "services",
        "titre": "Nos services",
        "liens": [
            {"titre": "Dispositifs d'accompagnement", "url": "dispositifs", "icone": "utilisateurs"},
            {"titre": "Information et orientation", "url": "information", "icone": "boussole"},
            {"titre": "Conseil", "url": "conseil", "icone": "ampoule"},
            {"titre": "Accompagnement", "url": "accompagnement", "icone": "poignee"},
            {"titre": "Formation", "url": "formation", "icone": "formation"},
        ],
    },
    {"id": "programmes", "titre": "Programmes", "url": "programme", "icone": "drapeau"},
    {"id": "actualites", "titre": "Actualités", "url": "actualite", "icone": "calendrier",
     "aussi": ("actu_detail",)},
    {"id": "opportunites", "titre": "Opportunités", "url": "offres", "icone": "mallette",
     "aussi": ("offres_type", "offre_detail")},
    {
        "id": "ressources",
        "titre": "Ressources",
        "liens": [
            {"titre": "Questions fréquentes", "url": "faq", "icone": "question"},
            {"titre": "Documents à télécharger", "url": "documents", "icone": "document"},
        ],
    },
]


# --------------------------------------------------------------------------
# Accès rapides de la page d'accueil (« Que souhaitez-vous faire ? »)
#   titre = le besoin exprimé par le visiteur ; desc = la page où il arrive.
# --------------------------------------------------------------------------
ACCES_RAPIDES = [
    {"titre": "M'informer et m'orienter", "desc": "Information et orientation", "url": "information", "icone": "boussole"},
    {"titre": "Obtenir un conseil", "desc": "Conseil", "url": "conseil", "icone": "ampoule"},
    {"titre": "Être accompagné", "desc": "Accompagnement", "url": "accompagnement", "icone": "poignee"},
    {"titre": "Me former", "desc": "Formation", "url": "formation", "icone": "formation"},
    {"titre": "Découvrir les programmes", "desc": "Programmes", "url": "programme", "icone": "drapeau"},
    {"titre": "Contacter l'agence", "desc": "Contact", "url": "contact", "icone": "message"},
]


# --------------------------------------------------------------------------
# Page « Dispositifs d'accompagnement »
#   OFFRE_SERVICES : les 4 services (l'introduction vient de la Page de l'admin
#   si elle existe ; sinon « resume » est utilisé).
#   ETAPES_PARCOURS : le processus d'accompagnement en 7 étapes.
# --------------------------------------------------------------------------
OFFRE_SERVICES = [
    {
        "titre": "Information et orientation", "url": "information", "page": "information", "icone": "boussole",
        "resume": "Trouver le bon interlocuteur et le bon dispositif pour votre projet.",
        "points": ["Opportunités économiques", "Formalisation des entreprises",
                   "Mécanismes de financement", "Programmes de formation et d'accompagnement"],
    },
    {
        "titre": "Conseil", "url": "conseil", "page": "conseil", "icone": "ampoule",
        "resume": "Des échanges personnalisés pour structurer et sécuriser votre activité.",
        "points": ["Clarification de l'idée de projet", "Analyse de la viabilité",
                   "Organisation interne", "Décisions stratégiques"],
    },
    {
        "titre": "Accompagnement", "url": "accompagnement", "page": "accompagnement", "icone": "poignee",
        "resume": "Un suivi structuré, de la formalisation à la consolidation de l'entreprise.",
        "points": ["Diagnostic de l'entreprise", "Plan d'affaires et formalisation",
                   "Accès aux financements et aux dispositifs", "Suivi et consolidation"],
    },
    {
        "titre": "Formation et animation", "url": "formation", "page": "formation", "icone": "formation",
        "resume": "Renforcer les compétences des porteurs de projets et des dirigeants de TPME.",
        "points": ["Culture entrepreneuriale", "Gestion d'entreprise",
                   "Accès au financement", "Ateliers et formations de proximité"],
    },
]

ETAPES_PARCOURS = [
    {"titre": "Accueil et orientation", "texte": "Identification de vos besoins et orientation vers les dispositifs adaptés."},
    {"titre": "Diagnostic", "texte": "Évaluation de la maturité de l'entreprise et définition d'un parcours personnalisé."},
    {"titre": "Conseil et structuration", "texte": "Plan d'affaires, organisation de l'activité, modèle économique."},
    {"titre": "Formation", "texte": "Renforcement des compétences entrepreneuriales, techniques et managériales."},
    {"titre": "Formalisation et accès aux dispositifs", "texte": "Démarches de formalisation, financements et programmes d'appui."},
    {"titre": "Suivi de l'entreprise", "texte": "Suivi technique pour anticiper les difficultés et consolider l'activité."},
    {"titre": "Croissance et pérennisation", "texte": "Productivité, innovation, accès aux marchés et compétitivité."},
]
