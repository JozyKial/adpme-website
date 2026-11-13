# ==========================================================================
# ADPME Congo — recherche.py — v1
# Moteur de recherche interne du site (/recherche/?q=...).
#   - insensible aux accents et aux majuscules : « formalite » trouve « Formalité » ;
#   - tous les mots importants doivent être présents (« de », « la », « les »… ignorés) ;
#   - les mots sont réduits à leur racine : « formalité » trouve aussi « formalisation »,
#     « entreprises » trouve « entreprise » ;
#   - les résultats dont le titre contient les mots passent en premier ;
#   - un extrait du texte est affiché autour du mot trouvé, surligné.
# Fonctionne avec PostgreSQL comme avec SQLite, sans extension à installer :
# le site compte quelques centaines de contenus, la recherche se fait en Python.
# ==========================================================================
import re
import unicodedata
from html import unescape

from django.urls import NoReverseMatch, reverse
from django.utils.html import escape, strip_tags
from django.utils.safestring import mark_safe

MOTS_IGNORES = {
    "a", "au", "aux", "avec", "ce", "ces", "d", "dans", "de", "des", "du", "en", "et", "l", "la", "le",
    "les", "leur", "leurs", "ou", "par", "pour", "qu", "que", "qui", "sur", "un", "une", "vos", "votre",
}


def _sans_accent(caractere):
    """Lettre de base d'un caractère (é -> e), en gardant exactement un caractère."""
    base = unicodedata.normalize("NFKD", caractere)[:1]
    return base.lower() if base else caractere.lower()


def texte_brut(html):
    """Texte lisible d'un contenu CKEditor (balises retirées, &nbsp; et autres codes convertis)."""
    return " ".join(unescape(strip_tags(str(html or ""))).split())


def normaliser(texte):
    """Minuscules sans accents, même longueur que le texte d'origine (pour retrouver la position)."""
    return "".join(_sans_accent(c) for c in texte)


# Terminaisons retirées pour retrouver la racine d'un mot (du plus long au plus court)
TERMINAISONS = ("ations", "ation", "ements", "ement", "ites", "ite", "ees", "ee", "eurs", "eur",
                "ers", "er", "es", "s", "e")


def racine(mot):
    """Racine simple d'un mot français (au moins 5 lettres conservées)."""
    for fin in TERMINAISONS:
        if mot.endswith(fin) and len(mot) - len(fin) >= 5:
            return mot[: -len(fin)]
    return mot


def mots_recherches(requete):
    mots = re.split(r"[\s'’\-.,;:!?()«»\"]+", normaliser(requete))
    utiles = [m for m in mots if len(m) >= 2 and m not in MOTS_IGNORES]
    return [racine(m) for m in utiles] or [m for m in mots if m]


def score(mots, titre, corps=""):
    """0 si un mot manque ; sinon un score (le titre compte triple)."""
    titre_n, corps_n = normaliser(titre), normaliser(corps)
    total = 0
    for mot in mots:
        dans_titre, dans_corps = titre_n.count(mot), corps_n.count(mot)
        if not dans_titre and not dans_corps:
            return 0
        total += 3 * dans_titre + dans_corps
    return total


def extrait_surligne(texte, mots, longueur=220):
    """Passage du texte autour du premier mot trouvé, mots surlignés par <mark>."""
    if not texte:
        return ""
    texte_n = normaliser(texte)
    positions = [texte_n.find(m) for m in mots if texte_n.find(m) >= 0]
    debut = max(0, min(positions) - longueur // 3) if positions else 0
    fin = min(len(texte), debut + longueur)
    if debut > 0:
        espace = texte.find(" ", debut)
        debut = espace + 1 if 0 <= espace < debut + 30 else debut
    morceau, morceau_n = texte[debut:fin], texte_n[debut:fin]

    # Repérage des zones à surligner sur la version sans accents
    zones = []
    for mot in mots:
        # Le mot entier est surligné, pas seulement sa racine (« accompagn » -> « accompagnement »)
        for trouve in re.finditer(re.escape(mot) + r"\w*", morceau_n):
            zones.append((trouve.start(), trouve.end()))
    zones.sort()
    resultat, curseur = [], 0
    for a, b in zones:
        if a < curseur:
            continue
        resultat.append(escape(morceau[curseur:a]))
        resultat.append(f"<mark>{escape(morceau[a:b])}</mark>")
        curseur = b
    resultat.append(escape(morceau[curseur:]))
    html = "".join(resultat)
    return mark_safe(("… " if debut > 0 else "") + html + (" …" if fin < len(texte) else ""))


def _trier(resultats, limite):
    resultats.sort(key=lambda r: r[0], reverse=True)
    return [objet for _, objet in resultats[:limite]]


def rechercher(requete):
    """Résultats groupés par type de contenu (dictionnaire de listes)."""
    from .models import BlogActualite, Document, FAQ, Offre, Page, Programme
    from .navigation import MENU_PRINCIPAL
    from .sitemaps import PAGES_ROUTES

    mots = mots_recherches(requete)
    vide = {"pages": [], "programmes": [], "actualites": [], "faqs": [], "documents": [], "offres": []}
    if not mots:
        return vide

    # Pages du menu (titre) et pages rédigées dans l'admin (titre + contenu)
    contenus = {PAGES_ROUTES.get(p.cle): p for p in Page.objects.all() if PAGES_ROUTES.get(p.cle)}
    pages = []
    for rubrique in MENU_PRINCIPAL:
        for lien in rubrique.get("liens", [rubrique]):
            page = contenus.get(lien["url"])
            corps = f"{page.intro} {texte_brut(page.contenu)}" if page else ""
            titre = f"{lien['titre']} {page.titre if page else ''}"
            note = score(mots, titre, corps)
            if note:
                try:
                    href = reverse(lien["url"])
                except NoReverseMatch:
                    continue
                pages.append((note, {
                    "titre": lien["titre"],
                    "rubrique": rubrique["titre"] if "liens" in rubrique else "",
                    "href": href,
                    "icone": lien.get("icone", "document"),
                    "extrait": extrait_surligne(corps, mots, 160) if corps else "",
                }))

    programmes = []
    for p in Programme.objects.filter(actif=True):
        corps = f"{p.resume} {p.public_cible} {texte_brut(p.contenu)}"
        note = score(mots, p.titre, corps)
        if note:
            p.extrait = extrait_surligne(corps, mots, 180)
            programmes.append((note, p))

    actualites = []
    for a in BlogActualite.objects.filter(published=True).select_related("category"):
        note = score(mots, a.title, texte_brut(a.content))
        if note:
            actualites.append((note, a))

    faqs = [(score(mots, f.question, f.reponse), f) for f in FAQ.objects.filter(active=True)]
    documents = [(score(mots, d.titre, d.description), d) for d in Document.objects.filter(actif=True)]
    offres = [(score(mots, o.titre, f"{o.resume} {o.reference} {o.lieu} {texte_brut(o.contenu)}"), o)
              for o in Offre.objects.filter(actif=True)]

    return {
        "pages": _trier(pages, 12),
        "programmes": _trier(programmes, 6),
        "actualites": _trier(actualites, 12),
        "faqs": _trier([r for r in faqs if r[0]], 10),
        "documents": _trier([r for r in documents if r[0]], 10),
        "offres": _trier([r for r in offres if r[0]], 10),
    }

