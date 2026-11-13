# ==========================================================================
# ADPME Congo — synchronisation.py — v1
# Exécuté automatiquement après chaque `py manage.py migrate` (voir apps.py) :
#   1. crée dans l'admin les « Textes du site » manquants (registre textes.py),
#      met à jour leur page et leur libellé, sans jamais toucher au texte saisi ;
#   2. remplit une seule fois les listes (accès rapides, services, étapes)
#      à partir de navigation.py si elles sont encore vides.
# ==========================================================================


def synchroniser(**kwargs):
    from .models import Element, Page, TexteSite
    from .navigation import ACCES_RAPIDES, ETAPES_PARCOURS, OFFRE_SERVICES
    from .textes import TEXTES

    # 1. Textes du site
    existants = {t.cle: t for t in TexteSite.objects.all()}
    nouveaux = []
    for cle, (page, libelle, valeur) in TEXTES.items():
        texte = existants.get(cle)
        if texte is None:
            nouveaux.append(TexteSite(cle=cle, page=page, libelle=libelle, valeur=valeur))
        elif texte.page != page or texte.libelle != libelle:
            texte.page, texte.libelle = page, libelle
            texte.save(update_fields=["page", "libelle"])
    TexteSite.objects.bulk_create(nouveaux)

    # 2. Listes (une seule fois, si la liste est vide)
    if not Element.objects.filter(liste="acces").exists():
        Element.objects.bulk_create([
            Element(liste="acces", titre=a["titre"], texte=a["desc"], page=a["url"], icone=a["icone"], ordre=i)
            for i, a in enumerate(ACCES_RAPIDES, start=1)
        ])
    if not Element.objects.filter(liste="service").exists():
        intros = dict(Page.objects.exclude(intro="").values_list("cle", "intro"))
        Element.objects.bulk_create([
            Element(liste="service", titre=s["titre"], texte=intros.get(s["page"], s["resume"]),
                    points="\n".join(s["points"]), page=s["url"], icone=s["icone"], ordre=i)
            for i, s in enumerate(OFFRE_SERVICES, start=1)
        ])
    if not Element.objects.filter(liste="etape").exists():
        Element.objects.bulk_create([
            Element(liste="etape", titre=e["titre"], texte=e["texte"], ordre=i)
            for i, e in enumerate(ETAPES_PARCOURS, start=1)
        ])

        