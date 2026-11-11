# ==========================================================================
# ADPME Congo — context_processors.py — v2
# Variables disponibles dans TOUS les gabarits :
#   agence          -> fiche AgenceInfo (admin)
#   reseaux         -> liens sociaux renseignés, prêts à afficher
#   menu_principal  -> menu (adpme/navigation.py) avec URL et état actif
# ==========================================================================
from django.urls import NoReverseMatch, reverse

from .models import AgenceInfo
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


def _url(nom):
    try:
        return reverse(nom)
    except NoReverseMatch:
        return "#"


def navigation(request):
    match = getattr(request, "resolver_match", None)
    page = match.url_name if match else None

    menu = []
    for rubrique in MENU_PRINCIPAL:
        entree = dict(rubrique)
        if "liens" in rubrique:
            entree["liens"] = [
                {**lien, "href": _url(lien["url"]), "actif": lien["url"] == page}
                for lien in rubrique["liens"]
            ]
            entree["actif"] = any(l["actif"] for l in entree["liens"])
        else:
            entree["href"] = _url(rubrique["url"])
            entree["actif"] = page == rubrique["url"] or page in rubrique.get("aussi", ())
        menu.append(entree)
    return {"menu_principal": menu}


