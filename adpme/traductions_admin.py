# ==========================================================================
# ADPME Congo — traductions_admin.py — v1
# Traduction française des textes du thème d'administration Unfold, qui n'est
# livré qu'en anglais. Le fichier de traduction (locale/fr/LC_MESSAGES/django.mo)
# est généré automatiquement à chaque `py manage.py migrate`, ou à la demande
# avec `py manage.py traduire_admin`.
# Pour corriger une traduction : modifier la valeur à droite, puis relancer
# l'une de ces deux commandes et redémarrer le serveur.
# ==========================================================================
import struct
from pathlib import Path

TRADUCTIONS = {
    # ── Navigation et recherche ──────────────────────────────────────────
    "Search apps and models...": "Rechercher…",
    "Type to search": "Tapez pour rechercher",
    "Recent searches": "Recherches récentes",
    "No results found": "Aucun résultat",
    "Nothing matched your search": "Aucun résultat pour cette recherche",
    "All applications": "Toutes les rubriques",
    "Toggle sidebar": "Afficher ou masquer le menu",
    "Toggle dark/light mode": "Mode clair / sombre",
    "Dark": "Sombre",
    "Light": "Clair",
    "System": "Système",
    "Return to site": "Retour au site",
    "Welcome": "Bienvenue",
    "Welcome back to": "Bienvenue sur",
    "Forgotten your password or username?": "Mot de passe ou identifiant oublié ?",
    "Toggle password visibility": "Afficher ou masquer le mot de passe",
    "You have been successfully logged out from the administration": "Vous êtes bien déconnecté de l'administration",
    "Go back": "Retour",
    "Navigate": "Naviguer",
    "Open command tool": "Ouvrir la recherche rapide",
    "Open shortcuts list": "Afficher les raccourcis clavier",
    "Available shortcuts": "Raccourcis disponibles",
    "Global shortcuts": "Raccourcis généraux",
    "Changelist shortcuts": "Raccourcis des listes",
    "Command tool shortcuts": "Raccourcis de la recherche rapide",
    "Open selection": "Ouvrir la sélection",
    "Open selection in new tab": "Ouvrir la sélection dans un nouvel onglet",

    # ── Listes, filtres et actions ───────────────────────────────────────
    "Filters": "Filtres",
    "Apply Filters": "Appliquer les filtres",
    "Reset filters": "Réinitialiser les filtres",
    "Toggle filter": "Afficher ou masquer le filtre",
    "Date from": "Du",
    "Date to": "Au",
    "From": "De",
    "To": "À",
    "Action": "Action",
    "Select action": "Choisir une action",
    "Select action to run": "Choisir l'action à exécuter",
    "Run": "Exécuter",
    "Select": "Choisir",
    "Select value": "Choisir une valeur",
    "Select record": "Choisir un élément",
    "Select format": "Choisir un format",
    "Select currency": "Choisir une devise",
    "This page yielded into no results. Create a new item or reset your filters.":
        "Aucun élément à afficher. Ajoutez un élément ou réinitialisez les filtres.",
    "No data": "Aucune donnée",
    "Not enough data.": "Pas assez de données.",
    "Create new record": "Créer un élément",
    "Add new item": "Ajouter un élément",
    "Add row": "Ajouter une ligne",
    "New": "Nouveau",
    "Edit": "Modifier",
    "Update": "Mettre à jour",
    "Submit": "Valider",
    "Cancel": "Annuler",
    "Click to cancel": "Cliquer pour annuler",
    "Previous": "Précédent",
    "Next": "Suivant",
    "Collapse": "Replier",
    "Default": "Par défaut",
    "Reset to default": "Revenir à la valeur par défaut",
    "True": "Oui",
    "False": "Non",
    "Name": "Nom",
    "Date": "Date",
    "Value": "Valeur",
    "Field": "Champ",
    "Object": "Objet",
    "Row": "Ligne",
    "General": "Général",
    "This item will be deleted.": "Cet élément sera supprimé.",
    "hide warning": "masquer l'avertissement",
    "You can not create nested object without parent": "Impossible de créer un sous-élément sans élément parent",
    "%(class_name)s %(instance)s": "%(class_name)s %(instance)s",

    # ── Fichiers et images ───────────────────────────────────────────────
    "Choose file to upload": "Choisir un fichier",
    "Current file": "Fichier actuel",
    "Click to download": "Cliquer pour télécharger",
    "Image preview": "Aperçu de l'image",
    "Record picture": "Prendre une photo",
    "Enter an URL": "Saisir une adresse web",

    # ── Éditeur de texte ─────────────────────────────────────────────────
    "Paragraph": "Paragraphe",
    "Heading": "Titre",
    "Bold": "Gras",
    "Italic": "Italique",
    "Underlined": "Souligné",
    "Strike": "Barré",
    "Link": "Lien",
    "Unlink": "Retirer le lien",
    "Quote": "Citation",
    "Code": "Code",
    "Ordered list": "Liste numérotée",
    "Unordered list": "Liste à puces",
    "Indent increase": "Augmenter le retrait",
    "Indent decrease": "Diminuer le retrait",
    "Undo": "Annuler",
    "Redo": "Rétablir",
    "Line number": "Numéro de ligne",

    # ── Utilisateurs et droits ───────────────────────────────────────────
    "After you've created a user, you’ll be able to edit more user options.":
        "Une fois l'utilisateur créé, vous pourrez modifier ses autres options.",
    "Manage user": "Gérer l'utilisateur",
    "Manage group": "Gérer le groupe",
    "Permissions": "Droits",
    "User permissions": "Droits de l'utilisateur",
    "Group permissions": "Droits du groupe",
    "Object permissions": "Droits sur les éléments",
    "Group": "Groupe",
    "You are currently working on behalf of <em>%(user)s</em>.":
        "Vous travaillez actuellement au nom de <em>%(user)s</em>.",
    "impersonate": "se connecter en tant que",
    "impersonate %(username)s": "se connecter en tant que %(username)s",
    "stop impersonating": "revenir à mon compte",

    # ── Historique des modifications ─────────────────────────────────────
    "Change History": "Historique des modifications",
    "Changes": "Modifications",
    "Changed by": "Modifié par",
    "Change reason": "Motif de la modification",
    "Comment": "Commentaire",
    "Old value": "Ancienne valeur",
    "New value": "Nouvelle valeur",
    "Revert": "Restaurer",
    "This object doesn't have a change history.": "Cet élément n'a pas d'historique de modifications.",
    "Choose a date from the list below to revert to a previous version of this object":
        "Choisissez une date ci-dessous pour restaurer une version précédente de cet élément",
    "Press the 'Revert' button below to revert to this version of the object.":
        "Cliquez sur « Restaurer » ci-dessous pour revenir à cette version de l'élément.",
    "Press the 'Change History' button below to edit the history.":
        "Cliquez sur « Historique des modifications » ci-dessous pour modifier l'historique.",
    "View traceback": "Voir le détail de l'erreur",

    # ── Import / export ──────────────────────────────────────────────────
    "Import": "Importer",
    "Export": "Exporter",
    "Confirm import": "Confirmer l'import",
    "Skipped": "Ignoré",
    "Non field specific": "Erreur générale",
    "Some rows failed to validate": "Certaines lignes contiennent des erreurs",
    "Dataset not found. No action performed.": "Données introuvables. Aucune action effectuée.",
    "This importer will import the following fields: ": "Les champs suivants seront importés : ",
    "This exporter will export the following fields: ": "Les champs suivants seront exportés : ",
    "This exporter will export the following fields": "Les champs suivants seront exportés",
    "Below is a preview of data to be imported. If you are satisfied with the results, click 'Confirm import'":
        "Voici un aperçu des données à importer. Si elles vous conviennent, cliquez sur « Confirmer l'import »",
    "Please correct these errors in your data where possible, then reupload it using the form above.":
        "Corrigez ces erreurs dans vos données, puis importez-les de nouveau avec le formulaire ci-dessus.",
}


def _fichier_mo(traductions):
    """Construit le contenu d'un fichier .mo (format GNU gettext)."""
    entete = "Content-Type: text/plain; charset=UTF-8\nPlural-Forms: nplurals=2; plural=(n > 1);\n"
    messages = {"": entete, **{k: v for k, v in traductions.items() if k}}
    cles = sorted(messages)
    ids = [c.encode("utf-8") for c in cles]
    textes = [messages[c].encode("utf-8") for c in cles]

    n = len(cles)
    debut_ids = 7 * 4                      # en-tête : 7 entiers de 4 octets
    debut_textes = debut_ids + n * 8       # table des identifiants
    debut_donnees = debut_textes + n * 8   # table des traductions

    donnees, table_ids, table_textes = b"", [], []
    for chaine, table in [(c, table_ids) for c in ids] + [(t, table_textes) for t in textes]:
        table.append((len(chaine), debut_donnees + len(donnees)))
        donnees += chaine + b"\0"

    contenu = struct.pack("<7I", 0x950412DE, 0, n, debut_ids, debut_textes, 0, 0)
    for longueur, position in table_ids + table_textes:
        contenu += struct.pack("<2I", longueur, position)
    return contenu + donnees


def generer_catalogue():
    """Écrit locale/fr/LC_MESSAGES/django.mo (dossier LOCALE_PATHS des réglages)."""
    from django.conf import settings

    dossiers = getattr(settings, "LOCALE_PATHS", [])
    if not dossiers:
        return None
    chemin = Path(dossiers[0]) / "fr" / "LC_MESSAGES" / "django.mo"
    chemin.parent.mkdir(parents=True, exist_ok=True)
    contenu = _fichier_mo(TRADUCTIONS)
    if not chemin.exists() or chemin.read_bytes() != contenu:
        chemin.write_bytes(contenu)
    return chemin

