# ==========================================================================
# ADPME Congo — templatetags/seo.py — v1
# Données structurées schema.org (JSON-LD) lues par Google pour enrichir
# les résultats de recherche. Rien n'est affiché à l'écran.
#   {% load seo %}
#   {% schema_organisation %}                      -> l'agence + le site (base.html)
#   {% schema_fil_ariane titre parent_titre parent_url %}
#   {% schema_article post %}                      -> article d'actualité
#   {% schema_offre_emploi offre %}                -> offre d'emploi ou de stage (Google Jobs)
#   {% schema_faq faqs %}                          -> page des questions fréquentes
# Textes utilisés : admin > Textes du site > Référencement (schema.org).
# Contrôle : https://search.google.com/test/rich-results
# ==========================================================================
import json
from datetime import datetime, time

from django import template
from django.templatetags.static import static
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

from .ui import extrait

register = template.Library()


def _script(donnees):
    """Balise <script type="application/ld+json"> sûre (pas de « </script> » possible dans le contenu)."""
    texte = json.dumps(donnees, ensure_ascii=False, separators=(",", ":"))
    texte = texte.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    return mark_safe(f'<script type="application/ld+json">{texte}</script>')


def _absolu(request, chemin):
    return request.build_absolute_uri(chemin) if request else chemin


def _texte(context, cle):
    from ..textes import defaut
    return (context.get("textes_site") or {}).get(cle) or defaut(cle)


def _organisation(context):
    """Description de l'agence, réutilisée comme éditeur des articles et employeur des offres."""
    request = context.get("request")
    agence = context.get("agence")
    org = {
        "@type": "GovernmentOrganization",
        "@id": _absolu(request, "/") + "#organisation",
        "name": _texte(context, "seo.organisation_nom"),
        "alternateName": _texte(context, "seo.organisation_sigle"),
        "url": _absolu(request, "/"),
        "logo": _absolu(request, static("assets/images/logo/adpme.png")),
    }
    if agence:
        if agence.email_contact:
            org["email"] = agence.email_contact
        if agence.phone:
            org["telephone"] = agence.phone
        if agence.adresse:
            org["address"] = {
                "@type": "PostalAddress",
                "streetAddress": agence.adresse,
                "addressLocality": _texte(context, "seo.ville"),
                "addressCountry": "CG",
            }
    reseaux = [r["url"] for r in context.get("reseaux") or []]
    if reseaux:
        org["sameAs"] = reseaux
    return org


@register.simple_tag(takes_context=True)
def schema_organisation(context):
    request = context.get("request")
    org = _organisation(context)
    site = {
        "@type": "WebSite",
        "@id": _absolu(request, "/") + "#site",
        "name": _texte(context, "seo.organisation_sigle"),
        "url": _absolu(request, "/"),
        "inLanguage": "fr",
        "publisher": {"@id": org["@id"]},
    }
    return _script({"@context": "https://schema.org", "@graph": [org, site]})


@register.simple_tag(takes_context=True)
def schema_fil_ariane(context, titre, parent_titre="", parent_url=""):
    request = context.get("request")
    elements = [("Accueil", "/")]
    if parent_titre and parent_url:
        elements.append((parent_titre, parent_url))
    elements.append((titre, request.path if request else ""))
    return _script({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": str(nom), "item": _absolu(request, url)}
            for i, (nom, url) in enumerate(elements, start=1)
        ],
    })


@register.simple_tag(takes_context=True)
def schema_article(context, post):
    request = context.get("request")
    org = _organisation(context)
    donnees = {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": post.title[:110],
        "description": extrait(post.content, 200),
        "datePublished": post.date_publication.isoformat(),
        "dateModified": timezone.localtime(post.last_update).isoformat() if post.last_update else post.date_publication.isoformat(),
        "mainEntityOfPage": _absolu(request, request.path) if request else "",
        "author": {"@type": "Organization", "name": org["name"], "url": org["url"]},
        "publisher": {"@type": "Organization", "name": org["name"], "logo": {"@type": "ImageObject", "url": org["logo"]}},
        "inLanguage": "fr",
    }
    if post.image:
        donnees["image"] = [_absolu(request, post.image.url)]
    if post.category:
        donnees["articleSection"] = post.category.name
    return _script(donnees)


@register.simple_tag(takes_context=True)
def schema_offre_emploi(context, offre):
    """Offre d'emploi ou de stage encore ouverte : format JobPosting (Google Jobs)."""
    if offre.type_offre != "emploi" or not offre.est_ouverte:
        return ""
    request = context.get("request")
    org = _organisation(context)
    donnees = {
        "@context": "https://schema.org",
        "@type": "JobPosting",
        "title": offre.titre,
        "description": str(offre.contenu) + (str(offre.modalites) if offre.modalites else ""),
        "datePosted": offre.date_publication.isoformat(),
        "hiringOrganization": {"@type": "Organization", "name": org["name"], "sameAs": org["url"], "logo": org["logo"]},
        "jobLocation": {
            "@type": "Place",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": offre.lieu or _texte(context, "seo.ville"),
                "addressCountry": "CG",
            },
        },
        "directApply": False,
        "url": _absolu(request, reverse("offre_detail", args=[offre.slug])),
    }
    if offre.reference:
        donnees["identifier"] = {"@type": "PropertyValue", "name": org["alternateName"], "value": offre.reference}
    if offre.date_limite:
        fin = timezone.make_aware(datetime.combine(offre.date_limite, time(23, 59)))
        donnees["validThrough"] = fin.isoformat()
    return _script(donnees)


@register.simple_tag
def schema_faq(faqs):
    if not faqs:
        return ""
    return _script({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": f.question,
             "acceptedAnswer": {"@type": "Answer", "text": strip_tags(f.reponse)}}
            for f in faqs
        ],
    })

