# ==========================================================================
# ADPME Congo — navigation.py — v1
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
            {"titre": "Mot du Ministre", "url": "discours_ministre", "icone": "message"},
        ],
    },
    {
        "id": "services",
        "titre": "Nos services",
        "liens": [
            {"titre": "Information et orientation", "url": "information", "icone": "boussole"},
            {"titre": "Conseil", "url": "conseil", "icone": "ampoule"},
            {"titre": "Accompagnement", "url": "accompagnement", "icone": "poignee"},
            {"titre": "Formation", "url": "formation", "icone": "formation"},
        ],
    },
    {"id": "programmes", "titre": "Programmes", "url": "programme", "icone": "drapeau"},
    {"id": "actualites", "titre": "Actualités", "url": "actualite", "icone": "calendrier",
     "aussi": ("actu_detail",)},
    {"id": "faq", "titre": "FAQ", "url": "faq", "icone": "question"},
]

