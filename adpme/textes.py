# ==========================================================================
# ADPME Congo — textes.py — v1
# Registre des « Textes du site » modifiables dans l'admin.
#
# Chaque entrée : "clé": (page, libellé affiché dans l'admin, texte par défaut)
#   - Dans un gabarit : {% load ui %} puis {% texte "accueil.cta_titre" %}
#   - Après chaque `py manage.py migrate`, les textes manquants sont créés
#     automatiquement dans l'admin avec leur valeur par défaut. Une valeur déjà
#     modifiée dans l'admin n'est jamais écrasée.
#   - Si un texte est vidé dans l'admin, la valeur par défaut ci-dessous revient.
# ==========================================================================
from .navigation import MENU_PRINCIPAL

PAGES = [
    ("general", "Général (en-tête, pied de page, référencement)"),
    ("menu", "Menu de navigation"),
    ("accueil", "Page d'accueil"),
    ("dispositifs", "Page « Dispositifs d'accompagnement »"),
    ("communs", "Libellés communs (boutons, encadrés)"),
]

TEXTES = {
    # ── Général ──────────────────────────────────────────────────────────
    "general.titre_suffixe": ("general", "Suffixe ajouté au titre des pages (onglet du navigateur)", "ADPME Congo"),
    "general.meta_description": ("general", "Description par défaut pour Google (160 caractères maximum)",
        "L'ADPME accompagne les porteurs d'idées et de projets et les dirigeants de TPME dans la formalisation, "
        "le développement et la pérennisation de leurs entreprises — Brazzaville, République du Congo."),
    "general.partage_titre": ("general", "Titre par défaut lors d'un partage sur les réseaux sociaux",
        "ADPME — Agence de Développement des TPME"),
    "general.partage_description": ("general", "Description par défaut lors d'un partage sur les réseaux sociaux",
        "L'ADPME accompagne les porteurs d'idées et de projets et les dirigeants de TPME dans la formalisation "
        "et le développement de leurs entreprises au Congo."),
    "general.bouton_contact": ("general", "En-tête : bouton de contact", "Nous contacter"),
    "general.recherche_placeholder": ("general", "En-tête : texte d'exemple du champ de recherche",
        "Rechercher une page, une actualité, une question…"),
    "general.menu_aide_titre": ("general", "Menu déroulant : titre de l'encadré d'aide", "Besoin d'un renseignement ?"),
    "general.menu_aide_bouton": ("general", "Menu déroulant : bouton de l'encadré d'aide", "Écrire à l'agence"),
    "general.pied_acces": ("general", "Pied de page : titre de la colonne des liens directs", "Accès directs"),
    "general.pied_qr_titre": ("general", "Pied de page : titre du QR code", "Le site sur mobile"),
    "general.pied_qr_texte": ("general", "Pied de page : texte sous le QR code",
        "Scannez ce code pour ouvrir le site sur votre téléphone."),
    "general.pied_mention": ("general", "Pied de page : mention après le nom de l'agence", "République du Congo"),

    # ── Libellés communs ─────────────────────────────────────────────────
    "communs.aside_titre": ("communs", "Colonne latérale : titre de l'encadré de contact", "Besoin d'un renseignement ?"),
    "communs.aside_bouton": ("communs", "Colonne latérale : bouton de l'encadré de contact", "Nous contacter"),
    "communs.chiffres_surtitre": ("communs", "Bloc « En chiffres » : surtitre", "En chiffres"),
    "communs.chiffres_titre": ("communs", "Bloc « En chiffres » : titre", "L'action de l'agence"),

    # ── Page d'accueil ───────────────────────────────────────────────────
    "accueil.titre_page": ("accueil", "Titre de la page (onglet du navigateur et Google)",
        "ADPME — Agence de Développement des TPME | Congo"),
    "accueil.hero_surtitre": ("accueil", "Bandeau sans slide : surtitre", "République du Congo"),
    "accueil.hero_titre": ("accueil", "Bandeau sans slide : titre",
        "Agence de Développement des Très Petites, Petites et Moyennes Entreprises"),
    "accueil.hero_bouton1": ("accueil", "Bandeau sans slide : premier bouton", "M'informer et m'orienter"),
    "accueil.hero_bouton2": ("accueil", "Bandeau sans slide : second bouton", "Nous contacter"),
    "accueil.acces_titre": ("accueil", "Accès rapides : titre", "Que souhaitez-vous faire ?"),
    "accueil.parcours_surtitre": ("accueil", "Parcours « Vous êtes… » : surtitre", "Votre parcours"),
    "accueil.parcours_titre": ("accueil", "Parcours « Vous êtes… » : titre", "Vous êtes…"),
    "accueil.programmes_surtitre": ("accueil", "Programmes : surtitre", "Nos programmes"),
    "accueil.programmes_titre": ("accueil", "Programmes : titre", "Les programmes portés par l'agence"),
    "accueil.programmes_bouton": ("accueil", "Programmes : bouton", "Tous les programmes"),
    "accueil.mot_lien": ("accueil", "Mot du Directeur général : texte du lien", "Lire le message complet"),
    "accueil.actus_surtitre": ("accueil", "Actualités : surtitre", "Actualités"),
    "accueil.actus_titre": ("accueil", "Actualités : titre", "Les dernières nouvelles de l'agence"),
    "accueil.actus_bouton": ("accueil", "Actualités : bouton", "Toutes les actualités"),
    "accueil.partenaires_surtitre": ("accueil", "Partenaires : surtitre", "Ils nous accompagnent"),
    "accueil.partenaires_titre": ("accueil", "Partenaires : titre", "Nos partenaires"),
    "accueil.cta_titre": ("accueil", "Appel à l'action (bas de page) : titre", "Un projet, une question ?"),
    "accueil.cta_texte": ("accueil", "Appel à l'action : texte",
        "Écrivez-nous, appelez l'agence ou consultez les questions fréquentes."),
    "accueil.cta_bouton1": ("accueil", "Appel à l'action : premier bouton", "Nous contacter"),
    "accueil.cta_bouton2": ("accueil", "Appel à l'action : second bouton", "Consulter la FAQ"),

    # ── Dispositifs d'accompagnement ─────────────────────────────────────
    "dispositifs.titre_page": ("dispositifs", "Titre de la page (onglet du navigateur et Google)",
        "Dispositifs d'accompagnement des TPME au Congo — ADPME"),
    "dispositifs.meta_description": ("dispositifs", "Description pour Google",
        "Information, conseil, accompagnement, formation et programmes : tous les dispositifs de l'ADPME pour "
        "formaliser, structurer et développer votre entreprise au Congo."),
    "dispositifs.titre": ("dispositifs", "Titre principal", "Dispositifs d'accompagnement"),
    "dispositifs.intro": ("dispositifs", "Introduction sous le titre",
        "Information, conseil, accompagnement, formation et programmes : l'ensemble des appuis de l'ADPME pour "
        "formaliser, structurer et développer votre entreprise au Congo."),
    "dispositifs.stat_services": ("dispositifs", "Compteur : libellé des services", "services d'appui"),
    "dispositifs.stat_etapes": ("dispositifs", "Compteur : libellé des étapes", "étapes de parcours"),
    "dispositifs.stat_programmes": ("dispositifs", "Compteur : libellé des programmes", "programmes"),
    "dispositifs.services_surtitre": ("dispositifs", "Offre de services : surtitre", "Notre offre"),
    "dispositifs.services_titre": ("dispositifs", "Offre de services : titre",
        "Des services adaptés à chaque étape de votre projet"),
    "dispositifs.services_intro": ("dispositifs", "Offre de services : introduction",
        "Que vous ayez une idée, un projet en cours ou une entreprise à développer, l'ADPME vous propose des "
        "services non financiers adaptés à votre situation."),
    "dispositifs.etapes_surtitre": ("dispositifs", "Parcours : surtitre", "Votre parcours"),
    "dispositifs.etapes_titre": ("dispositifs", "Parcours : titre", "Un accompagnement en 7 étapes"),
    "dispositifs.etapes_intro": ("dispositifs", "Parcours : introduction",
        "De l'accueil à la consolidation de votre entreprise, un parcours personnalisé selon vos besoins."),
    "dispositifs.etapes_bouton": ("dispositifs", "Parcours : bouton", "Le processus en détail"),
    "dispositifs.programmes_surtitre": ("dispositifs", "Programmes : surtitre", "Programmes"),
    "dispositifs.programmes_titre": ("dispositifs", "Programmes : titre", "Les programmes portés par l'agence"),
    "dispositifs.ressources_surtitre": ("dispositifs", "Ressources : surtitre", "Ressources"),
    "dispositifs.ressources_titre": ("dispositifs", "Ressources : titre", "Pour aller plus loin"),
    "dispositifs.res_formation_titre": ("dispositifs", "Ressource « Formation » : titre", "Formation et animation entrepreneuriale"),
    "dispositifs.res_formation_texte": ("dispositifs", "Ressource « Formation » : texte",
        "Ateliers pratiques, séminaires et formations de proximité pour renforcer vos compétences."),
    "dispositifs.res_documents_titre": ("dispositifs", "Ressource « Documents » : titre", "Documents à télécharger"),
    "dispositifs.res_documents_texte": ("dispositifs", "Ressource « Documents » : texte",
        "Textes, guides pratiques, formulaires et rapports publiés par l'agence."),
    "dispositifs.res_faq_titre": ("dispositifs", "Ressource « FAQ » : titre", "Questions fréquentes"),
    "dispositifs.res_faq_texte": ("dispositifs", "Ressource « FAQ » : texte",
        "Les réponses aux questions les plus souvent posées à l'ADPME."),
    "dispositifs.cta_titre": ("dispositifs", "Appel à l'action : titre", "Prêt à vous faire accompagner ?"),
    "dispositifs.cta_texte": ("dispositifs", "Appel à l'action : texte",
        "Présentez-nous votre projet : l'ADPME vous oriente vers le dispositif le plus adapté."),
    "dispositifs.cta_bouton1": ("dispositifs", "Appel à l'action : premier bouton", "Nous contacter"),
    "dispositifs.cta_bouton2": ("dispositifs", "Appel à l'action : second bouton", "M'informer et m'orienter"),
}


# ── Libellés du menu : générés à partir de navigation.py ────────────────
for _rubrique in MENU_PRINCIPAL:
    if "liens" in _rubrique:
        TEXTES[f"menu.{_rubrique['id']}"] = ("menu", f"Rubrique « {_rubrique['titre']} »", _rubrique["titre"])
        for _lien in _rubrique["liens"]:
            TEXTES[f"menu.{_lien['url']}"] = ("menu", f"{_rubrique['titre']} › {_lien['titre']}", _lien["titre"])
    else:
        TEXTES[f"menu.{_rubrique['url']}"] = ("menu", f"Lien direct « {_rubrique['titre']} »", _rubrique["titre"])


TEXTES["menu.recherche"] = ("menu", "Pied de page › lien vers la recherche", "Recherche")
TEXTES["menu.contact"] = ("menu", "Pied de page › lien vers le contact", "Contact")


def defaut(cle):
    """Texte par défaut d'une clé (chaîne vide si la clé est inconnue)."""
    return TEXTES.get(cle, (None, None, ""))[2]

