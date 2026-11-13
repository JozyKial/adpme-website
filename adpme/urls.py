# ==========================================================================
# ADPME Congo — urls.py — v3
# Adresses du site. Phase 4c : opportunités et lettre d'information.
# Phase 5 : plan du site (/sitemap.xml) et /robots.txt.
# ==========================================================================
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from .sitemaps import SITEMAPS

from adpme_project import settings

urlpatterns = [
    #path('admin/',admin.site.urls),
    # Accueil & Infos
    path('',views.AccueilView, name="accueil"),
    path('a-propos/', views.AproposView, name='a_propos'),
    path('programme/', views.ProgrammeView, name="programme"),
    path('programme/<slug:slug>/', views.ProgrammeDetailView, name="programme_detail"),
    path('actualite/', views.ActualiteView,name="actualite"),
    path('contact/', views.ContactView,name="contact"),
    path('conseil/', views.ConseilView, name="conseil"),
    path('information/', views.Info_orientationView, name="information"),
    path('accompagnement/', views.AccompagnementView, name="accompagnement"),
    path('formation/', views.FormationView, name="formation"),
    path('faq/', views.FaqView, name="faq"),
    path('documents/', views.DocumentsView, name="documents"),
    path('recherche/', views.RechercheView, name="recherche"),
    path('dispositifs-accompagnement/', views.DispositifsView, name="dispositifs"),
    path('actualite/<str:slug>', views.Blog_detail, name="actu_detail"),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('discours-directeur-general/', views.DiscoursDGView, name="discours_dg"),
    path('discours-ministre/', views.DiscoursMinistreView, name="discours_ministre"),

    # Refonte v3 — Phase 4c : opportunités et lettre d'information
    path('opportunites/', views.OffresView, name="offres"),
    path('opportunites/<slug:type_slug>/', views.OffresView, name="offres_type"),
    path('opportunites/offre/<slug:slug>/', views.OffreDetailView, name="offre_detail"),
    path('lettre-information/inscription/', views.NewsletterInscriptionView, name="newsletter_inscription"),
    path('lettre-information/desinscription/<uuid:jeton>/', views.NewsletterDesinscriptionView, name="newsletter_desinscription"),
    
    # Refonte v3 — Phase 5 : référencement
    path('sitemap.xml', sitemap, {'sitemaps': SITEMAPS}, name="sitemap"),
    path('robots.txt', views.RobotsView, name="robots"),

    # Refonte v3 — guide des composants (DEBUG uniquement)
    path('styleguide/', views.StyleguideView, name="styleguide"),

    
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    