# ==========================================================================
# ADPME Congo — context_processors.py — v3
# Variables disponibles dans TOUS les gabarits :
#   agence          -> fiche AgenceInfo (admin)
#   reseaux         -> liens sociaux renseignés, prêts à afficher
#   menu_principal  -> menu (adpme/navigation.py) avec URL, état actif et
#                      libellés modifiés dans l'admin (Textes du site > Menu)
#   textes_site     -> textes modifiés dans l'admin, lus par {% texte "…" %}
# ==========================================================================
from django.urls import NoReverseMatch, reverse

from .models import AgenceInfo, TexteSite
from .navigation import MENU_PRINCIPAL

# clé dans le JSON liens_sociaux -> (libellé, icône)
RESEAUX = {
    "facebook": ("Facebook", "facebook"),
    "linkedin": ("LinkedIn", "linkedin"),
    "youtube": ("YouTube", "youtube"),
    "twitter": ("X (Twitter)", "x-twitter"),
    "x": ("X", "x-twitter"),
    "instagram": ("Instagram", "instagram"),
}


def agence_info(request):
    agence = AgenceInfo.objects.first()
    reseaux = []
    liens = getattr(agence, "liens_sociaux", None)
    if isinstance(liens, dict):
        for cle, url in liens.items():
            cle = str(cle).lower().strip()
            if cle in RESEAUX and url:
                libelle, icone = RESEAUX[cle]
                reseaux.append({"libelle": libelle, "icone": icone, "url": url})
    return {"agence": agence, "reseaux": reseaux}


def _textes(request):
    """Textes de l'admin, lus une seule fois par page affichée."""
    if not hasattr(request, "_textes_site"):
        request._textes_site = {
            cle: valeur for cle, valeur in TexteSite.objects.values_list("cle", "valeur") if valeur.strip()
        }
    return request._textes_site


def textes_site(request):
    return {"textes_site": _textes(request)}


def _url(nom):
    try:
        return reverse(nom)
    except NoReverseMatch:
        return "#"


def navigation(request):
    match = getattr(request, "resolver_match", None)
    page = match.url_name if match else None

    textes = _textes(request)
    menu = []
    for rubrique in MENU_PRINCIPAL:
        entree = dict(rubrique)
        if "liens" in rubrique:
            entree["titre"] = textes.get(f"menu.{rubrique['id']}", rubrique["titre"])
            entree["liens"] = [
                {**lien, "titre": textes.get(f"menu.{lien['url']}", lien["titre"]),
                 "href": _url(lien["url"]), "actif": lien["url"] == page}
                for lien in rubrique["liens"]
            ]
            entree["actif"] = any(l["actif"] for l in entree["liens"])
        else:
            entree["titre"] = textes.get(f"menu.{rubrique['url']}", rubrique["titre"])
            entree["href"] = _url(rubrique["url"])
            entree["actif"] = page == rubrique["url"] or page in rubrique.get("aussi", ())
        menu.append(entree)
    return {"menu_principal": menu}

