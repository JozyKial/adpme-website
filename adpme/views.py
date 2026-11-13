# ==========================================================================
# ADPME Congo — views.py — v5
# Vues. Lot 2 : listes (accès rapides, services, étapes) et messages du
# formulaire de contact lus depuis l'admin.
# ==========================================================================
import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import NoReverseMatch, reverse
from django.http import FileResponse, Http404, HttpResponse
from django.db.models import F, Q
from .models import (
    BlogActualite,
    Category,
    FAQ, Discours,
    Slide, Programme, Parcours, ChiffreCle, Partenaire,
    Page, Antenne, Document, BlocAccueil, Element,
)

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
from .textes import texte_admin

from django.core.paginator import Paginator

def _elements(liste):
    """Éléments d'une liste de l'admin (accès rapides, services, étapes), avec leur lien."""
    elements = []
    for e in Element.objects.filter(liste=liste, actif=True):
        try:
            e.href = reverse(e.page) if e.page else ""
        except NoReverseMatch:
            e.href = ""
        elements.append(e)
    return elements


def AccueilView(request):
    """Page d'accueil v3 : chaque bloc ne s'affiche que s'il a du contenu dans l'admin."""
    context = {
        'slides': Slide.objects.filter(actif=True),
        'acces_rapides': _elements("acces"),
        'parcours': Parcours.objects.filter(actif=True).prefetch_related('liens'),
        'programmes': Programme.objects.filter(actif=True, sur_accueil=True)[:6],
        'chiffres': ChiffreCle.objects.filter(actif=True),
        'discours_dg': Discours.objects.filter(type_discours='dg').first(),
        'actualites': (BlogActualite.objects.filter(published=True)
                       .select_related('category')
                       .order_by('-date_publication', '-id')[:3]),
        'partenaires': Partenaire.objects.filter(actif=True),
        'blocs': {b.cle: b for b in BlocAccueil.objects.filter(actif=True)},
    }
    return render(request, "v3/accueil.html", context)


def DispositifsView(request):
    """Vue d'ensemble de l'offre d'accompagnement : services, parcours, programmes, ressources.
    Services et étapes : admin > Listes ; textes : admin > Textes du site."""
    context = {
        'services': _elements("service"),
        'etapes': _elements("etape"),
        'programmes': Programme.objects.filter(actif=True),
        'partenaires': Partenaire.objects.filter(actif=True),
        'rubrique_id': 'services',
    }
    return render(request, "v3/dispositifs.html", context)


def Categorie(request, slug):
    cat = Category.objects.all()
    blog_cat    = Category.objects.filter(slug = slug)
    
    context = {
        'cat' : cat,
        'active_category' : slug,
        'blog_cat' : blog_cat
    }

    return render(request,"adpme/categorie.html", context)


def Blog_detail(request, slug):
    """Article d'actualité. Un brouillon n'est visible que par l'équipe (connectée à l'admin)."""
    articles = BlogActualite.objects.select_related('category', 'author')
    if not request.user.is_staff:
        articles = articles.filter(published=True)
    post = get_object_or_404(articles, blog_slug=slug)

    lies = (BlogActualite.objects.filter(published=True, category=post.category)
            .exclude(id=post.id).order_by('-date_publication')[:3])
    if not lies:
        lies = BlogActualite.objects.filter(published=True).exclude(id=post.id).order_by('-date_publication')[:3]

    context = {
        'post': post,
        'lies': lies,
        'url_absolue': request.build_absolute_uri(),
    }
    return render(request, "v3/actualite_detail.html", context)


def ActualiteView(request):
    """Liste des actualités publiées, filtrable par catégorie (?categorie=slug)."""
    posts_list  = (BlogActualite.objects.filter(published=True)
                   .select_related('category')
                   .order_by('-date_publication', '-id'))
    categories  = Category.objects.filter(category__published=True).distinct().order_by('name')

    categorie_active = None
    slug = request.GET.get('categorie')
    if slug:
        categorie_active = categories.filter(slug=slug).first()
        if categorie_active:
            posts_list = posts_list.filter(category=categorie_active)

    posts = Paginator(posts_list, 9).get_page(request.GET.get('page', 1))
    context = {
        'posts': posts,
        'categories': categories,
        'categorie_active': categorie_active,
        'qs_extra': f"&categorie={categorie_active.slug}" if categorie_active else "",
    }
    return render(request, "v3/actualites.html", context)


def _page_contenu(request, cle, ancien_gabarit, rubrique_id, extra=None):
    """Affiche une page gérée dans l'admin (modèle Page).
    Tant que la page n'existe pas (commande charger_pages pas encore lancée),
    l'ancien gabarit reste affiché : le site n'a jamais de page vide."""
    page = Page.objects.filter(cle=cle).first()
    if page is None:
        return render(request, ancien_gabarit)
    context = {'page': page, 'rubrique_id': rubrique_id}
    if extra:
        context.update(extra)
    return render(request, "v3/page.html", context)


def AproposView(request):
    return _page_contenu(request, "a-propos", "adpme/apropos.html", "agence",
                         {'chiffres': ChiffreCle.objects.filter(actif=True)})

def Info_orientationView(request):
    return _page_contenu(request, "information", "adpme/information.html", "services")

def FormationView(request):
    return _page_contenu(request, "formation", "adpme/formation.html", "services")

def AccompagnementView(request):
    return _page_contenu(request, "accompagnement", "adpme/accompagnement.html", "services")

def ConseilView(request):
    return _page_contenu(request, "conseil", "adpme/conseil.html", "services")


def ProgrammeView(request):
    """Liste des programmes publiés (v3)."""
    context = {'programmes': Programme.objects.filter(actif=True)}
    return render(request, "v3/programmes.html", context)


def ProgrammeDetailView(request, slug):
    programme = get_object_or_404(Programme, slug=slug, actif=True)
    autres = Programme.objects.filter(actif=True).exclude(pk=programme.pk)[:3]
    return render(request, "v3/programme_detail.html", {'programme': programme, 'autres': autres})


def BlogActualiteView(request):
    return render(request,"adpme/BlogActualite.html")

logger = logging.getLogger(__name__)
def ContactView(request):
    form = ContactForm()

    if request.method == 'POST':
        # Piège à robots : ce champ est invisible pour les humains.
        if request.POST.get('site_web'):
            messages.success(request, texte_admin("contact.message_succes"))
            return redirect('contact')

        form = ContactForm(request.POST)
        if form.is_valid():
            nom             = form.cleaned_data['nom']
            email           = form.cleaned_data['email']
            sujet           = form.cleaned_data['sujet']
            message_text    = form.cleaned_data['message']

            try:
                send_mail(
                    subject         = f"[ADPME Contact] {sujet}",
                    message         = f"Message de : {nom} <{email}>\n\n{message_text}",
                    from_email      = settings.DEFAULT_FROM_EMAIL,
                    recipient_list  = [settings.CONTACT_EMAIL],
                    fail_silently   = False,
                )
                messages.success(request, texte_admin("contact.message_succes"))
                return redirect('contact')
            except Exception as e:
                logger.error(f"Erreur envoi email contact : {e}")
                messages.error(request, texte_admin("contact.message_erreur"))

    context = {
        'form': form,
        'antennes': Antenne.objects.filter(actif=True),
    }
    return render(request, "v3/contact.html", context)


def FaqView(request):
    faqs = FAQ.objects.filter(active=True)
    return render(request, "v3/faq.html", {'faqs': faqs, 'rubrique_id': 'ressources'})


def DocumentsView(request):
    """Documents à télécharger, filtrables par catégorie (?categorie=guides)."""
    documents = Document.objects.filter(actif=True)
    presentes = set(documents.values_list('categorie', flat=True))
    categories = [(cle, nom) for cle, nom in Document.CATEGORIES if cle in presentes]

    categorie_active = request.GET.get('categorie')
    if categorie_active in presentes:
        documents = documents.filter(categorie=categorie_active)
    else:
        categorie_active = None

    context = {
        'documents': documents,
        'categories': categories,
        'categorie_active': categorie_active,
        'rubrique_id': 'ressources',
    }
    return render(request, "v3/documents.html", context)


def DiscoursDGView(request):
    discours = get_object_or_404(Discours, type_discours='dg')
    return render(request, "v3/discours.html", {'discours': discours, 'rubrique_id': 'agence'})

def DiscoursMinistreView(request):
    discours = get_object_or_404(Discours, type_discours='ministre')
    return render(request, "v3/discours.html", {'discours': discours, 'rubrique_id': 'agence'})




# ── Refonte v3 : guide des composants (local uniquement) ──────────────
def StyleguideView(request):
    """Page de contrôle visuel des composants v3. 404 en production."""
    if not settings.DEBUG:
        raise Http404()
    from .templatetags.ui import ICONES, ICONES_PLEINES

    couleurs = [
        ("Vert ADPME", "--vert-700"), ("Vert foncé", "--vert-800"),
        ("Vert clair", "--vert-100"), ("Vert très clair", "--vert-50"),
        ("Violet logo", "--violet-500"), ("Violet texte", "--violet-700"),
        ("Violet clair", "--violet-100"), ("Violet très clair", "--violet-50"),
        ("Encre (titres)", "--encre"), ("Texte", "--texte"),
        ("Texte doux", "--texte-doux"), ("Fond alterné", "--fond-alt"),
    ]
    context = {
        'couleurs': couleurs,
        'posts': BlogActualite.objects.filter(published=True).select_related('category')[:3],
        'faqs': FAQ.objects.filter(active=True)[:4],
        'form': ContactForm(),
        'icones': list(ICONES) + list(ICONES_PLEINES),
    }
    return render(request, "v3/styleguide.html", context)





# ── Refonte v3 : recherche (version simple, enrichie en phase 5) ──────
def RechercheView(request):
    """Recherche dans les pages du menu, les actualités publiées et la FAQ."""
    from .navigation import MENU_PRINCIPAL

    q = request.GET.get('q', '').strip()[:100]
    pages, actualites, faqs, documents = [], [], [], []

    if len(q) >= 2:
        terme = q.lower()
        for rubrique in MENU_PRINCIPAL:
            for lien in rubrique.get('liens', [rubrique]):
                if terme in lien['titre'].lower() or terme in rubrique['titre'].lower():
                    pages.append({
                        'titre': lien['titre'],
                        'rubrique': rubrique['titre'] if 'liens' in rubrique else '',
                        'href': reverse(lien['url']),
                        'icone': lien.get('icone', 'document'),
                    })
        actualites = (BlogActualite.objects
                      .filter(published=True)
                      .filter(Q(title__icontains=q) | Q(content__icontains=q))
                      .select_related('category')[:12])
        faqs = (FAQ.objects
                .filter(active=True)
                .filter(Q(question__icontains=q) | Q(reponse__icontains=q))[:10])
        documents = (Document.objects
                     .filter(actif=True)
                     .filter(Q(titre__icontains=q) | Q(description__icontains=q))[:10])

    context = {
        'q': q,
        'pages': pages,
        'actualites': actualites,
        'faqs': faqs,
        'documents': documents,
        'total': len(pages) + len(actualites) + len(faqs) + len(documents),
    }
    return render(request, 'v3/recherche.html', context)

