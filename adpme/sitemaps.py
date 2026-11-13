# ==========================================================================
# ADPME Congo — sitemaps.py — v1
# Plan du site pour les moteurs de recherche : /sitemap.xml
# Mis à jour tout seul : chaque page, actualité, programme ou opportunité
# publiée dans l'admin y apparaît automatiquement.
# À déclarer une fois dans Google Search Console (phase 6).
# ==========================================================================
from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import BlogActualite, Discours, Offre, Page, Programme
from .navigation import MENU_PRINCIPAL

# Pages des discours : n'apparaissent dans le plan que si le discours est saisi dans l'admin
DISCOURS_ROUTES = {"discours_dg": "dg", "discours_ministre": "ministre"}

# Pages gérées dans l'admin (modèle Page) : identifiant -> nom de route
PAGES_ROUTES = {
    "a-propos": "a_propos",
    "information": "information",
    "conseil": "conseil",
    "accompagnement": "accompagnement",
    "formation": "formation",
}


class _Base(Sitemap):
    # En ligne, toutes les adresses sont annoncées en https
    @property
    def protocol(self):
        return "http" if settings.DEBUG else "https"


class PagesFixesSitemap(_Base):
    """Accueil, pages du menu, contact et rubriques des opportunités."""
    changefreq = "monthly"

    def items(self):
        discours = set(Discours.objects.values_list("type_discours", flat=True))
        routes = ["accueil"]
        for rubrique in MENU_PRINCIPAL:
            for lien in rubrique.get("liens", [rubrique]):
                if lien["url"] in DISCOURS_ROUTES and DISCOURS_ROUTES[lien["url"]] not in discours:
                    continue
                routes.append(lien["url"])
        routes += ["contact"]
        routes += [("offres_type", slug) for slug in Offre.SLUGS_TYPES.values()]
        return routes

    def location(self, item):
        if isinstance(item, tuple):
            return reverse(item[0], args=[item[1]])
        return reverse(item)

    def lastmod(self, item):
        cle = {route: cle for cle, route in PAGES_ROUTES.items()}.get(item)
        if cle:
            page = Page.objects.filter(cle=cle).only("date_maj").first()
            return page.date_maj if page else None
        return None

    def priority(self, item):
        return 1.0 if item == "accueil" else 0.7


class ActualitesSitemap(_Base):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return BlogActualite.objects.filter(published=True).exclude(blog_slug__isnull=True).order_by("-date_publication")

    def location(self, obj):
        return reverse("actu_detail", args=[obj.blog_slug])

    def lastmod(self, obj):
        return obj.last_update


class ProgrammesSitemap(_Base):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Programme.objects.filter(actif=True)

    def location(self, obj):
        return reverse("programme_detail", args=[obj.slug])


class OpportunitesSitemap(_Base):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Offre.objects.filter(actif=True)

    def location(self, obj):
        return reverse("offre_detail", args=[obj.slug])

    def lastmod(self, obj):
        return obj.date_publication


SITEMAPS = {
    "pages": PagesFixesSitemap,
    "actualites": ActualitesSitemap,
    "programmes": ProgrammesSitemap,
    "opportunites": OpportunitesSitemap,
}

