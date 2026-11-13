# ==========================================================================
# ADPME Congo — templatetags/ui.py — v3
# ==========================================================================
from functools import lru_cache
from html import unescape
from django import template
from django.utils.html import format_html, mark_safe, strip_tags

register = template.Library()

ICONES = {
    "telephone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "email": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "lieu": '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "horloge": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "recherche": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
    "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
    "fermer": '<path d="M18 6 6 18M6 6l12 12"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "chevron-bas": '<path d="m6 9 6 6 6-6"/>',
    "chevron-droite": '<path d="m9 18 6-6-6-6"/>',
    "chevron-gauche": '<path d="m15 18-6-6 6-6"/>',
    "fleche-droite": '<path d="M5 12h14M12 5l7 7-7 7"/>',
    "fleche-haut": '<path d="M12 19V5M5 12l7-7 7 7"/>',
    "lien-externe": '<path d="M15 3h6v6M10 14 21 3M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "telecharger": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/>',
    "document": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/>',
    "calendrier": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
    "utilisateurs": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    "utilisateur": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "mallette": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
    "formation": '<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/>',
    "ampoule": '<path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.1V17h6v-.2c0-.8.4-1.6 1-2.1A7 7 0 0 0 12 2z"/>',
    "boussole": '<circle cx="12" cy="12" r="10"/><path d="m16.2 7.8-2.1 6.3-6.3 2.1 2.1-6.3z"/>',
    "batiment": '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/>',
    "graphique": '<path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/>',
    "monnaie": '<circle cx="12" cy="12" r="10"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8M12 18V6"/>',
    "poignee": '<path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.9-3.9a3 3 0 0 0-4.2 0l-.9.9a1 1 0 1 1-3-3l2.8-2.8a5.8 5.8 0 0 1 7.1-.9l.5.3a4 4 0 0 0 2.6.6H21"/><path d="m21 3 1 11h-2M3 3 2 14l6.5 6.5a1 1 0 1 0 3-3M3 4h8"/>',
    "drapeau": '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1zM4 22v-7"/>',
    "question": '<circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3M12 17h.01"/>',
    "message": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "whatsapp": '<path d="M3 21l1.65-4.65A9 9 0 1 1 7.7 19.4z"/><path d="M9 9.2c0 3 2.8 5.8 5.8 5.8l.9-1.3-1.8-.9-.9.7a4.4 4.4 0 0 1-2.3-2.3l.7-.9-.9-1.8z"/>',
}

# Logos remplis (réseaux sociaux)
ICONES_PLEINES = {
    "facebook": '<path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H8v4h2v8h4v-8h3l1-4h-4V8.5c0-.3.2-.5.5-.5z"/>',
    "linkedin": '<path d="M4 9h4v12H4zM6 3a2 2 0 1 1 0 4 2 2 0 0 1 0-4zM10 9h3.8v1.7A4.2 4.2 0 0 1 17.5 9C21 9 22 11.2 22 14.3V21h-4v-6c0-1.5-.3-3-2.2-3s-1.9 1.4-1.9 3v6H10z"/>',
    "youtube": '<path fill-rule="evenodd" d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.8 15.1V8.9l5.7 3.1z"/>',
    "x-twitter": '<path d="M3 3h5.5l4 5.6L17.3 3H20l-6.2 7.3L21 21h-5.5l-4.3-6-5.1 6H3.4l6.6-7.7z"/>',
    "instagram": '<path fill-rule="evenodd" d="M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5zm0 2a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3zm5 3.5a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9zm0 2a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM17.5 5.3a1.2 1.2 0 1 1 0 2.4 1.2 1.2 0 0 1 0-2.4z"/>',
}


@register.simple_tag
def icon(nom, label="", classe=""):
    """Renvoie une icône SVG en ligne. Icône inconnue -> chaîne vide."""
    if nom in ICONES:
        contenu, css = ICONES[nom], "icon"
    elif nom in ICONES_PLEINES:
        contenu, css = ICONES_PLEINES[nom], "icon icon--plein"
    else:
        return ""
    if classe:
        css = f"{css} {classe}"
    if label:
        attributs = format_html('role="img" aria-label="{}"', label)
    else:
        attributs = mark_safe('aria-hidden="true" focusable="false"')
    return format_html(
        '<svg class="{}" viewBox="0 0 24 24" {}>{}</svg>',
        css, attributs, mark_safe(contenu),
    )


@register.filter
def tel_lien(numero):
    """'+242 06 123 45 67' -> '+242061234567' pour les liens tel: et wa.me."""
    if not numero:
        return ""
    return "".join(c for c in str(numero) if c.isdigit() or c == "+")




@register.filter
def wa_lien(numero):
    """'+242 06 123 45 67' -> '242061234567' (format attendu par https://wa.me/)."""
    return "".join(c for c in str(numero or "") if c.isdigit())


@lru_cache(maxsize=32)
def _qr_svg(donnees):
    import segno
    return segno.make(donnees, error="m").svg_inline(
        scale=1, border=2, dark="#17201a", light="#ffffff",
        omitsize=True, svgclass="qr__svg", lineclass=None,
    )


@register.simple_tag
def qr_svg(donnees, label="QR code"):
    """QR code en SVG (net à toutes les tailles). Vide si segno n'est pas installé."""
    if not donnees:
        return ""
    try:
        svg = _qr_svg(str(donnees))
    except ImportError:
        return ""
    return format_html('<span class="qr" role="img" aria-label="{}">{}</span>', label, mark_safe(svg))




@register.filter
def extrait(html, longueur=180):
    """Résumé lisible d'un contenu CKEditor : retire les balises, convertit les
    codes HTML (&nbsp; &rsquo; &eacute;…) en vrais caractères, supprime les
    espaces superflus et coupe proprement sur un mot."""
    texte = unescape(strip_tags(str(html or "")))
    texte = " ".join(texte.split())
    longueur = int(longueur)
    if len(texte) <= longueur:
        return texte
    coupe = texte[:longueur].rsplit(" ", 1)[0].rstrip(" ,;:.—-")
    return coupe + "…"



