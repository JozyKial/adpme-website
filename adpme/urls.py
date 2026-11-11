from django.urls import path, include
from django.conf.urls.static import static
from . import views 

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
    path('actualite/<str:slug>', views.Blog_detail, name="actu_detail"),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('discours-directeur-general/', views.DiscoursDGView, name="discours_dg"),
    path('discours-ministre/', views.DiscoursMinistreView, name="discours_ministre"),
    
    # Refonte v3 — guide des composants (DEBUG uniquement)
    path('styleguide/', views.StyleguideView, name="styleguide"),

        path('recherche/', views.RechercheView, name="recherche"),
    
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
